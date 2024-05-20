import xml.sax
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
start_time_sax = datetime.now()
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.counts = defaultdict(int)
        self.current_namespace_buffer = []

    def startElement(self, name, attrs):
        if name == 'namespace':
            self.current_namespace_buffer = []  

    def characters(self, content):
        if self.current_namespace_buffer is not None:
            self.current_namespace_buffer.append(content)  

    def endElement(self, name):
        if name == 'namespace':
            self.current_namespace = ''.join(self.current_namespace_buffer).strip() 
            if self.current_namespace in ['molecular_function', 'biological_process', 'cellular_component']:
                self.counts[self.current_namespace] += 1
            self.current_namespace_buffer = None  
            self.current_namespace = None

handler = GOHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('C:/Users/20815/Desktop/IBI1_2023-24/Practical14/go_obo.xml')
end_time_sax = datetime.now()
sax_duration = end_time_sax - start_time_sax
print(f"SAX API took: {sax_duration}")

ontologies = list(handler.counts.keys())
frequencies = list(handler.counts.values())

plt.figure(figsize=(10, 5))
plt.bar(ontologies, frequencies)
plt.xlabel('Ontologies')
plt.ylabel('Term Frequency')
plt.title('GO Terms Distribution by Ontology (SAX)')
plt.show()
# SAX API took: 0:00:01.986772
# SAX API is faster.
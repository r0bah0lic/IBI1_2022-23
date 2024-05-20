import xml.etree.ElementTree as ET
import datetime
import matplotlib.pyplot as plt

counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
tree = ET.parse('C:/Users/20815/Desktop/IBI1_2023-24/Practical14/go_obo.xml')
root = tree.getroot()

for term in root.findall('term'):
    namespace = term.find('namespace').text
    if namespace in counts:
        counts[namespace] += 1
for ontology, count in counts.items():
    print(f"{ontology}: {count} terms")

start_time_dom = datetime.datetime.now()

end_time_dom = datetime.datetime.now()
dom_duration = end_time_dom - start_time_dom
print(f"DOM API took: {dom_duration}")

import matplotlib.pyplot as plt

ontologies = list(counts.keys())
frequencies = list(counts.values())

plt.figure(figsize=(10, 5))
plt.bar(ontologies, frequencies)
plt.xlabel('Ontologies')
plt.ylabel('Term Frequency')
plt.title('GO Terms Distribution by Ontology (DOM)')
plt.show()

# molecular_function: 12154 terms
# biological_process: 30794 terms
# cellular_component: 4392 terms
# DOM API took: 0:00:00 , this may mean that it was too fast to measure and is faster than SAX
database=open(r'C:\Users\20815\Desktop\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')  #open the file
result=open(r'C:\Users\20815\Desktop\IBI1_2023-24\Practical8\duplicate_genes.fa','w')  #locate the final file
import re
description=re.compile(r'^>(\w+)_.+$')  #search for the description line that starts with >
whether_duplicate=False #judge whether the part is duplicated
for line in database:
    current_description=description.match(line)  #match the line with the description regex
    if current_description:  #if the line is description line
        if 'duplication' in line:
            gene_name=current_description.group(1)  #get the gene name
            simplified_sequence=f">{gene_name}\n"
            result.write(simplified_sequence)  # write the simplified sequences into output file
            whether_duplicate=True  #confirm the line the lines after this line are duplicated part
        else:
            whether_duplicate=False  #this is not duplicated part
    else:  #this line is sequence
        if whether_duplicate:  #if this line is in duplicated part
            result.write(line)  #write the dupilated sequence into the output file
database.close()
result.close()  

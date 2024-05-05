import re
def count_repeat_duplicate_genes():
    repeat_pattern = input("Please enter one of the repetitive sequences ('GTGTGT' or 'GTCTGT'): ")
    output_file = f"{repeat_pattern}_duplicate_genes.fa"
    with open(r'C:\Users\20815\Desktop\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as fasta_in, open(output_file, 'w') as fasta_out:
        current_description = ''  # Initialize variables
        current_sequence = ''
        description_regex = re.compile(r'^>(\w+)_.*')
        # Loop through the input file
        for line in fasta_in:
            if line.startswith('>'):  # New gene description
                if current_sequence:  # If we have processed a previous gene
                    # Count the occurrences of the repeat pattern
                    repeat_count = current_sequence.count(repeat_pattern)
                    # Write the simplified sequence to the output file
                    simplified_description = f">{description_regex.match(current_description).group(1)}_{repeat_count}"
                    fasta_out.write(simplified_description + '\n')
                    fasta_out.write(current_sequence + '\n')
                current_description = line.strip()
                current_sequence = ''
            else:
                current_sequence += line.strip()

        # Process the last gene
        if current_sequence:
            repeat_count = current_sequence.count(repeat_pattern)
            if description_match := description_regex.match(current_description):
                gene_name = description_match.group(1)
                simplified_description = f">{description_regex.match(current_description).group(1)}_{repeat_count}"
                fasta_out.write(simplified_description + '\n')
                fasta_out.write(current_sequence + '\n')
count_repeat_duplicate_genes()
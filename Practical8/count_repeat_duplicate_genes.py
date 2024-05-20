import re
def count_repeat_in_sequence(sequence, repeat):
    """Count occurrences of a repeat in a sequence."""
    return sequence.count(repeat)
def process_file(input_filename, output_filename, repeat_sequence):
    database = open(input_filename, 'r')
    result = open(output_filename, 'w')
    description_pattern = re.compile(r'^>(\w+)_.+$')
    gene_name = ""
    sequence = ""
    repeat_count = 0
    for line in database:
        current_description = description_pattern.match(line)
        if current_description:# Process previous gene's sequence
            if gene_name:
                repeat_count = count_repeat_in_sequence(sequence, repeat_sequence)
                if repeat_count > 0:
                    simplified_sequence = f">{gene_name}_{repeat_count}\n{sequence}\n"
                    result.write(simplified_sequence)
            gene_name = current_description.group(1)# Start processing new gene
            sequence = ""
        elif line.strip():  # Only add non-empty lines to the sequence (excluding newlines)
            sequence += line.strip()
    repeat_count = count_repeat_in_sequence(sequence, repeat_sequence)# Process the last gene after the loop ends
    if repeat_count > 0:
        simplified_sequence = f">{gene_name}_{repeat_count}\n{sequence}\n"
        result.write(simplified_sequence)
    database.close()
    result.close()
if __name__ == "__main__":
    repeat_options = ['GTGTGT', 'GTCTGT']
    selected_repeat = input("Please input one of the two repetitive sequences ('GTGTGT' or 'GTCTGT'): ").strip()
    while selected_repeat not in repeat_options:
        print("Invalid input. Please choose either 'GTGTGT' or 'GTCTGT'.")
        selected_repeat = input("Please input one of the two repetitive sequences ('GTGTGT' or 'GTCTGT'): ").strip()
    input_file = r'C:\Users\20815\Desktop\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = f"{selected_repeat}_duplicate_genes.fa"
    process_file(input_file, output_file, selected_repeat)
    print(f"Processing completed. Output saved to '{output_file}'.")
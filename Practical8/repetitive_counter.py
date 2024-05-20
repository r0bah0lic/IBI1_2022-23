seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeat_patterns = ['GTGTGT', 'GTCTGT']
repeats_count = {}
for pattern in repeat_patterns:
    length = len(pattern)
    count = 0
    i = 0
    while True:
        found = seq.find(pattern, i)
        if found == -1:
            break
        count += 1
        i = found + 1  
    repeats_count[pattern] = count
for a, b in repeats_count.items():
    print('pattern', a, 'is repeated', b, 'times')
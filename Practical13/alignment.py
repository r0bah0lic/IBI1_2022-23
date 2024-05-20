BLOSUM62 = '''A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split('\n')

for i in range(len(BLOSUM62)):
    BLOSUM62[i] = BLOSUM62[i].split()

m={}
for i in range(len(BLOSUM62)):
    for j in range(1, len(BLOSUM62[0])):
        m[BLOSUM62[i][0] + '\t' + BLOSUM62[j-1][0]] = BLOSUM62[i][j]
def read_sequence(filename):
    header = ''
    sequence = ''
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                header = line  # Store the header but don't add it to the sequence
            else:
                sequence += line  # Only add non-header lines to the sequence
    return sequence
# Read sequences with corrected paths and ensuring they are valid
seq1 = read_sequence('C:\\Users\\20815\\Desktop\\IBI1_2023-24\\Practical13\\SLC6A4_HUMAN (1).fa')
seq2 = read_sequence('C:\\Users\\20815\\Desktop\\IBI1_2023-24\\Practical13\\SLC6A4_MOUSE (1).fa')
seq3 = read_sequence('C:\\Users\\20815\\Desktop\\IBI1_2023-24\\Practical13\\SLC6A4_RAT (1).fa')
BLOSUM62_dict = {}
sum=0
def align_score(seq1, seq2, BLOSUM62_dict):
    t = [[0]]
    for n in range(1, len(seq2)+1):
        t[0].append(n*(-5))
    for i in range(1, len(seq1)+1):
        t.append([i*(-5)] + [0]*len(seq2))
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                t[i][j] = t[i-1][j-1] + int(m[seq1[i-1]+'\t'+seq2[j-1]])
            else:
                t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(m[seq1[i-1]+'\t'+seq2[j-1]]))
    return (t[len(seq1)][len(seq2)])
def calculate_identity(seq1, seq2):
    identical = len([1 for a, b in zip(seq1, seq2) if a == b])
    return (identical / len(seq1)) * 100 if seq1 else 0
score1 = align_score(seq1, seq2, BLOSUM62_dict)
score2 = align_score(seq2, seq3, BLOSUM62_dict)
score3 = align_score(seq1, seq3, BLOSUM62_dict)
identity1 = calculate_identity(seq1, seq2)
identity2 = calculate_identity(seq2, seq3)
identity3 = calculate_identity(seq1, seq3)
# Improved output with sequence headers included
print('seq1 and seq2: Alignment Score=',score1, 'Identity=',identity1)
print('seq2 and seq3: Alignment Score=',score2, 'Identity=',identity2)
print('seq1 and seq3: Alignment Score=',score3, 'Identity=',identity3)
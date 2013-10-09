
peptide = "QWERB"
difference_amino_acid = set()

for letter in peptide:
    difference_amino_acid.add(letter)

letters = []
for letter in difference_amino_acid:
    letters.append(letter)

def combinate(peptides, letters):
    tmp = []
    results = []
    for i in peptides:
        for j in letters:
            if not j in i:
                tmp.append(i + j)
    if len(tmp[0]) < len(letters):
         results = combinate(tmp, letters)
    for i in peptides:
        results.append(i)
    return results

tmp = combinate(letters, letters)
result = set()

for i in tmp:
    result.add(''.join(sorted(i)))






total_mass = 1024

peptide_mass = dict()
peptide_mass['G'] = 57
peptide_mass['A'] = 71
peptide_mass['S'] = 87
peptide_mass['P'] = 97
peptide_mass['V'] = 99
peptide_mass['T'] = 101
peptide_mass['C'] = 103
peptide_mass['I'] = 113
peptide_mass['L'] = 113
peptide_mass['N'] = 114
peptide_mass['D'] = 115
peptide_mass['K'] = 128
peptide_mass['Q'] = 128
peptide_mass['E'] = 129
peptide_mass['M'] = 131
peptide_mass['H'] = 137
peptide_mass['F'] = 147
peptide_mass['R'] = 156
peptide_mass['Y'] = 163
peptide_mass['W'] = 186

mass = 0
maximal_len = 0
min_mass = 57

while (mass < total_mass):
    mass = mass + peptide_mass['G']
    maximal_len = maximal_len + 1

maximal_len = maximal_len - 1

def add(word, mass):
    results = 0
    if mass < min_mass:
        return 0
    if mass == 0:
        return 1
    for item in peptide_mass:
        results = results + add(word + item, mass - peptide_mass[item])
    return results

results = add('G', 1024)

print(results)
print(mass)
print(maximal_len)


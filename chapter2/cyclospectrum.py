
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

peptide = "IRGWEWVPFLCVT"

def get_slices(peptide, k):
    result = []
    if k == len(peptide):
        result.append(peptide)
    else:
        for i in range(len(peptide)):
            tmp = peptide[i:min(len(peptide), i + k)] + peptide[0:max(0, i + k - len(peptide))]
            result.append(tmp)
    if k > 1:
        tmp = get_slices(peptide, k - 1)
        for item in tmp:
            result.append(item)
    return result

def get_mass(item):
    mass = 0
    for letter in item:
        mass = mass + peptide_mass[letter]
    return mass

slices = get_slices(peptide[::-1], len(peptide))

given_masses = []
for item in slices:
    given_masses.append(get_mass(item))
given_masses.append(0)
given_masses = sorted(given_masses)

str_given_masses = []
for item in given_masses:
    str_given_masses.append(str(item))

f = open('C:/projects/test.txt', 'w')
print(' '.join(str_given_masses), file=f)
f.close()
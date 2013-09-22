
import operator

dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

kmers = []
kmers_frequently = dict()

def check_pattern(substring, pattern, d):
    errors = 0
    for i in range(len(pattern)):
        if pattern[i] != substring[i]:
            errors = errors + 1
    if errors > d:
        return False
    return True

#incorrect! need to check all kmers 4^k
for i in range(len(dna) - k):
    if (dna[i:i+k] in kmers) == False:
        kmers.append(dna[i:i+k])

for pattern in kmers:
    count = 0
    for i in range(len(dna) - k):
        if check_pattern(dna[i:i+k], pattern, d):
            count = count + 1
    kmers_frequently[pattern] = count

sorted_kmers = sorted(kmers_frequently.items(), key=operator.itemgetter(1), reverse=True)

max_count = sorted_kmers[0][1]
result = []

#print(sorted_kmers)

for kmer in sorted_kmers:
    if kmer[1] < max_count:
        break
    else:
        result.append(kmer[0])

print(" ".join(result))

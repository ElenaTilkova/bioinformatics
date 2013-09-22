
import operator

dna = "GGGGGGCGAACACAACGACGAAAACGGCGCGAAAACACGGGGCGACGACACGGGGCGCGCGCGCGACGAACAAGGCGGGAACGCGAGGCGACCGAAAAAAAACAAAACGAAAGGACCGAACAACGAAACGAACGAAAAACGGGACCGAAGGACAAAAAAGGCGCGACGACGCGGGCGAGGGGCGGGCGACGACACACACCGAGGACGGGGAACGACGAGGCGAAAAACCGAACGGAAACGGCG"
k = 9
d = 2

def check_pattern(substring, pattern, d):
    errors = 0
    for i in range(len(pattern)):
        if pattern[i] != substring[i]:
            errors = errors + 1
    if errors > d:
        return False
    return True

def combinations(k):
    results = []
    kmers = None
    if k > 1:
        kmers = combinations(k - 1)
        k = k - 1
    else:
        return ['A', 'T', 'G', 'C']
    for kmer in kmers:
        results.append('A' + kmer)
        results.append('T' + kmer)
        results.append('G' + kmer)
        results.append('C' + kmer)
    return results

def reverse_pattern(pattern):
    result = ""
    for letter in pattern:
        if letter == "A":
            result = result + "T"
        elif letter == "T":
            result = result + "A"
        elif letter == "C":
            result = result + "G"
        elif letter == "G":
            result = result + "C"
    return result[::-1]

kmers_frequently = dict()
kmers_frequently_with_reverse = dict()
kmers = combinations(k)

for pattern in kmers:
    count = 0
    for i in range(len(dna) - k):
        if check_pattern(dna[i:i+k], pattern, d):
            count = count + 1
    kmers_frequently[pattern] = count

for pattern in kmers:
    complementary_kmer = reverse_pattern(pattern)
    kmers_frequently_with_reverse[pattern] = kmers_frequently[pattern] + kmers_frequently[complementary_kmer]

sorted_kmers = sorted(kmers_frequently_with_reverse.items(), key=operator.itemgetter(1), reverse=True)

max_count = sorted_kmers[0][1]
result = []

for kmer in sorted_kmers:
    if kmer[1] < max_count:
        break
    else:
        result.append(kmer[0])

print(" ".join(result))

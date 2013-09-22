
pattern = "CTTGATCAT"
complement_pattern = ""

for letter in pattern:
    if letter == "A":
        complement_pattern = complement_pattern + "T"
    elif letter == "T":
        complement_pattern = complement_pattern + "A"
    elif letter == "C":
        complement_pattern = complement_pattern + "G"
    elif letter == "G":
        complement_pattern = complement_pattern + "C"

complement_pattern = complement_pattern[::-1]

length = len(pattern)

poses = []

for i in range(len(genome) - length):
    if pattern == genome[i:i+length]:
        poses.append(str(i))
    elif complement_pattern == genome[i:i+length]:
        poses.append(str(i))

print(" ".join(poses))
        
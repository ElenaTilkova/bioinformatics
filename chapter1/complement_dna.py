
pattern = "TCTTGATCA"
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

result = result[::-1]

print(len(pattern))
print(len(result))
print(result)
#complementary strand


import copy

message = "53‡‡†305))6·THE26)H‡.)H‡)TE06·THE†E^60))E5T161T:‡·E†E3(EE)5·†TH6(TEE·96·?TE)·‡(THE5)T5·†2:·‡(TH956·2(5·—H)E^E·TH0692E5)T)6†E)H‡‡T1(‡9THE0E1TE:E‡1THE†E5TH)HE5†52EE06·E1(‡9THET(EETH(‡?3HTHE)H‡T1‡(T:1EET‡?T"

values = dict()

codes = ['0', '1', '2', '3', '5', '6', '7', '9', '‡', '†',
         ')', '.', '·', '^', ':', '(', '?']


def replace_letters(letters):
    decoded_message = copy.deepcopy(message)
    for letter in letters:
        decoded_message = decoded_message.replace(letter, letters[letter])
    return decoded_message

summa = 0

for code in codes:
    count = 0
    for letter in message:
        if code == letter:
            count = count + 1
    values[code] = count
    summa = summa + count / len(message)
    print(code + ": " + str(count / len(message)))

print("sum: " + str(summa))

new_letters = {'‡' : 'O', ')': 'S', '·': 'N', '5' : 'A', '6' : 'I', '(' : 'R',
               '1' : 'F', '†': 'D', '0': 'L', '9' : 'M', '2' : 'B', ':' : 'Y',
               '3' : 'G', '?' : 'U', '^' : 'V', '—' : 'C', '.' : 'P'}

new_message = replace_letters(new_letters)
print(new_message)

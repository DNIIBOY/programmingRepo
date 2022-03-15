with open("task2_compact.txt", "r") as f:
    ciphertext = f.read()

print("first part of ciphertext",ciphertext[:10])

dicty = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,
"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,
"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,
"V":21,"W":22,"X":23,"Y":24,"Z":25}

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def countFreq(listOfChars):
	freqs = [0 for i in range(26)]
	for char in listOfChars:
		freqs[dicty[char]] += 1
	return freqs

keylen = 5
sublists = [[] for i in range(keylen)]

# Split ciphertext into sublists
counter = 0
for char in ciphertext:
	if char != "\n":
		sublists[counter].append(char)
		counter = (counter + 1) % keylen
print([sublist[:10] for sublist in sublists])


# For each sublist: Guess E, record shift, and perform shift on sublist
shiftedlists = []
shifts = []
for sublist in sublists:
	n = len(sublist)
	maxi = max(countFreq(sublist))
	print("Frequency of E-guess",maxi/n)
	newE = countFreq(sublist).index(maxi)
	shift = newE-dicty["E"]
	shifts.append(shift)
	shiftedList = []
	for char in sublist:
		charindex = dicty[char]
		correctindex = (charindex - shift) % 26
		correctchar = Alphabet[correctindex]
		shiftedList.append(correctchar)
	shiftedlists.append(shiftedList)

# What message does that give?
message = ""
for i in range(20):
	char = shiftedlists[i % keylen][i//keylen]
	message = message + char

print("message",message)


# Apply shift to original text
with open("task2.txt", "r") as f:
    ciphertext = f.read()

message = ""
counter = 0
for char in ciphertext:
	if char in alphabet:
		charindex = alphabet.index(char)
		correctindex = (charindex - shifts[counter]) % 26
		correctchar = alphabet[correctindex]
		message += correctchar
		counter = (counter + 1) % keylen
	elif char in Alphabet:
		charindex = Alphabet.index(char)
		correctindex = (charindex - shifts[counter]) % 26
		correctchar = Alphabet[correctindex]
		message += correctchar
		counter = (counter + 1) % keylen
	else:
		message += char

print(message)

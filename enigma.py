import pickle

alphabet = ' .abcdefghijklmnopqrstuvwxyz'

f = open('./wheels', 'rb')
rotor1, rotor2, rotor3 = pickle.load(f)
f.close()

#print("Your settings:\n\trotor1: %s\n\trotor2: %s\n\trotor3: %s" % (rotor1, rotor2, rotor3))

def reflector(char):
	return alphabet[len(alphabet)-alphabet.find(char)-1]


def enigma_one_char(char):
	char1 = rotor1[alphabet.find(char)]
	char2 = rotor2[alphabet.find(char1)]
	char3 = rotor3[alphabet.find(char2)]
	reflected = reflector(char3)
	char3 = alphabet[rotor3.find(reflected)]
	char2 = alphabet[rotor2.find(char3)]
	char1 = alphabet[rotor1.find(char2)]

	return char1


def rotate_rotors():
	global rotor1, rotor2, rotor3
	rotor1 = rotor1[1:] + rotor1[0]
	if state % 28:
		rotor2 = rotor2[1:] + rotor2[0]
	if state % (28*28):
		rotor3 = rotor3 [1:] + rotor3[0] 


plain = input("[in]:")

cipher = ''
state = 0


for char in plain:
	state += 1
	cipher += enigma_one_char(char)
	rotate_rotors()


print(f"[out]:{cipher}")

import pickle

alphabet = ' .abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+-={}[]<>?/\\|,\'\":;'
all_chars = alphabet + numbers + symbols

f = open('./wheels', 'rb')
rotor1, rotor2, rotor3 = pickle.load(f)
f.close()

#print("Your settings:\n\trotor1: %s\n\trotor2: %s\n\trotor3: %s" % (rotor1, rotor2, rotor3))

def reflector(char):
	return all_chars[len(all_chars)-all_chars.find(char)-1]


def enigma_one_char(char):
	char1 = rotor1[all_chars.find(char)]
	char2 = rotor2[all_chars.find(char1)]
	char3 = rotor3[all_chars.find(char2)]
	reflected = reflector(char3)
	char3 = all_chars[rotor3.find(reflected)]
	char2 = all_chars[rotor2.find(char3)]
	char1 = all_chars[rotor1.find(char2)]

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

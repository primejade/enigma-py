import random
import pickle


alphabet = ' .abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+-={}[]<>?/\\|,\'\":;'
all_chars = alphabet + numbers + symbols

#print(len(all_chars))
#print(all_chars)

rotor1 = list(all_chars)
random.shuffle(rotor1)
rotor1 = ''.join(rotor1)

rotor2 = list(all_chars)
random.shuffle(rotor2)
rotor2 = ''.join(rotor2)

rotor3 = list(all_chars)
random.shuffle(rotor3)
rotor3 = ''.join(rotor3)



f = open('./wheels', 'wb')
pickle.dump((rotor1, rotor2, rotor3), f)
f.close()

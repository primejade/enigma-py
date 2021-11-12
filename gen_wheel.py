import random
import pickle


alphabet = ' .abcdefghijklmnopqrstuvwxyz'

rotor1 = list(alphabet)
random.shuffle(rotor1)
rotor1 = ''.join(rotor1)

rotor2 = list(alphabet)
random.shuffle(rotor2)
rotor2 = ''.join(rotor2)

rotor3 = list(alphabet)
random.shuffle(rotor3)
rotor3 = ''.join(rotor3)



f = open('./wheels', 'wb')
pickle.dump((rotor1, rotor2, rotor3), f)
f.close()

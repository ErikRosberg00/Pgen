import random
import string

def rndpwd(stringLength=16):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Ditt lösenord är ", rndpwd() )

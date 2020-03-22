import random
import string

Length = int(input("Hur många karaktärer ska ditt lösenord ha "))   
def Rndpwd():
    Pwdcrs = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(Pwdcrs) for i in range(Length))

print ("Ditt lösenord är", Rndpwd() )
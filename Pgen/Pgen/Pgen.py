import random
import string

print("Hur många karaktärer ska ditt lösenord ha")
Length = int(input())
print(Length)

def Rndpwd():
    Pwdcrs = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(Pwdcrs) for i in range(Length))

print ("Lösenord ", Rndpwd() )


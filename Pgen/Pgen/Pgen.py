import random
import string

while True:
    def rndpwd():
        while True:
            Length = input("Hur många karaktärer ska ditt lösenord ha ")
            try:
                Length = int(Length)
                break
            except ValueError:
              print("inte ett nummer försök igen")

        letters = string.ascii_letters + string.digits + string.punctuation

        return ''.join(random.choice(letters) for i in range(Length))
    clear
    print ("Ditt lösenord är " )
    print (rndpwd())
    print ( )
    print ("Vill du generera ett nytt lösen ord  ")
    if input("y / n ") == "n":
        break


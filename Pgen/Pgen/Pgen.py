import random
import string
import sys

def main():
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
    print ("Ditt lösenord är " )
    print (rndpwd())
    print ( )
    print ("Vill du generera ett nytt lösen ord  ")
    def jaynay():
        print ("Y / N")
        x = input()
        if x == "n" or "N":
            print ("programet stänger")
            exit(0)
        elif x == "y" or "Y":
             main()
        else:
            jaynay()
    jaynay()
main()


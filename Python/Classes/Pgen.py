import random
import sys
import string


class Pgen(object):
    """description of class"""


def Pgen():
    def RndPwd():
        while True:
            Length = input("Hur många karaktärer ska ditt lösenord ha ")
            try:
                Length = int(Length)
                break
            except ValueError:
                print("inte ett nummer försök igen")

        Letters = string.ascii_letters + string.digits + string.punctuation

        return ''.join(random.choice(Letters) for i in range(Length))
    print("Ditt lösenord är ")
    print(RndPwd())
    print()
    print("Vill du generera ett nytt lösen ord  ")

    def YN():
        print("Y / N")
        Redo = input()
        if Redo == "n" or "N":
            print("programet stänger")
            exit(0)
        elif Redo == "y" or "Y":
            Pgen()
        else:
            YN()
    YN()


Pgen()

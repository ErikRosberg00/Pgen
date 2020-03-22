import random
import string


def rndpwd():
    print("din input length")

    while True:
        Length = input()
        try:
            Length = int(Length)
            break
        except ValueError:
          ("inte ett numer försök igen")

    letters = string.ascii_letters + string.digits + string.punctuation


    return ''.join(random.choice(letters) for i in range(Length))

print ("Ditt lösenord är ", rndpwd() )

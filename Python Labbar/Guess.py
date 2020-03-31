import random
rndnum = random.randint(1,100)
vinst = False
Rundor =0
while vinst==False:
    gissning = input("Välj ett nummer mellan 1 och 100 ")
    Rundor +=1
    if rndnum==int(gissning):
        print("Grattis!")
        print("Du klarade spelet på : ",Rundor)
        vinst == True
        break
    else:
     if rndnum>int(gissning):
        print("Gissa högre")
     else:
        print("Gissa lägre")
class Pcrypt(object):
    """description of class"""
    def main():
	password = "1234"
	f = open("test/pwd.txt","w+") #Kan fixa så att pwd är en variabel dvs att du kan få ändra namnet (a = lägga till w = skriva om) mapp/fil.txt gör så användaren kan välja

	for i in range(10):
	     f.write("password %d\r\n" % (i+1)) # Skapar text strängar i filen, kan göra en password list som printas här efter den gått igenom en krypterings algoritm
	f.close() 

	f = open("test/pwd.txt", "r") #Printar ut den öppnade filen i terminal
	print(f.read())

if __name__ == '__main__':
	main()



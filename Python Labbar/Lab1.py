def main():
	Createpassword()
	passwordcheck2()


def Createpassword():
	Password = input("Skriv in ett lösenord " )
	print(Password)
	return Password


def passwordcheck():
	WrongPwd = 4
	while WrongPwd > 3:
		WrongPwd -= 1 
		Password = Createpassword
		print("Test PWDCHECK")
		PasswordCheck = input("Skriv in ditt valda lösenord " )
		if PasswordCheck == Createpassword:
			print("lyckats")
			exit(10)
		else:
			print("Fel lösenord du har", WrongPwd,"försök kvar")


def passwordcheck2():
	WrongPwd = 4

	Password = Createpassword
	while PasswordCheck !=  Createpassword:
		WrongPwd -= 1 
		PasswordCheck = input("Skriv in ditt valda lösenord " )
		print("Fel lösenord du har", WrongPwd,"försök kvar")		
	else:
		print("lyckats")
		exit(10)			

if __name__ == '__main__':
	main()

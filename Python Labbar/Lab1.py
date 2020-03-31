def main():
	passwordcheck()


def Createpassword():
	Password = input("Skriv in ett lösenord")
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

			

if __name__ == '__main__':
	Createpassword()
	main()
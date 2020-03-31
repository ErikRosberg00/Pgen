def main():
	SwitchExample(argument)

	
def varif():
	x,y =8,4
	
	if(x < y):
		st= "x is less than y"
	else:
		x -= 1
	print (x)


def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))

if __name__ == '__main__':
	main()
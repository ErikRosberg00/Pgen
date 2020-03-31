def main():
    varloop()


def loop1():
    i = 1
    while i < 6:
      print(i)
      i += 1
    else:
      print("i is no longer less than 6")

def loop2():
    i = 0
    while i < 6:
      i += 1
      if i == 3:
        continue
      print(i)

def loop3():
    i = 1
    while i < 6:
      print(i)
      if i == 3:
        break
      i += 1

def varloop():
    i = 0
    a = "Variable"
    while i < 6:
     i += 1
     print(a+str(i))


if __name__ == '__main__':
	main()




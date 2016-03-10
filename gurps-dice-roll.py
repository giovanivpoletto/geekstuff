import random
option="f"
while option != "e":
	try:
		option=input("choose your option: r to roll ou e to exit: ")
		if option=="r":
			result=random.randint(3,18)
			if result==3:
				print(result,"-  Critical Success!")
			elif result==18:
				print(result,"-  Critical Failure!")
			else:
				print(result)
		elif option=="e":
			print("Bye!")
		else:
			print("Choose again.")
	except:
		print("Bad Option")

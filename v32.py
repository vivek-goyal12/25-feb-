#write a program to impliment the walking interview

l=[]
while True:
	print("press 1 for input detailf of person")
	print("press 2 fo  finding the name of  person of that turn ")
	print("press 3 for ending the interview") 
	i=int(input("enter the  press key according the requirement "))
	if (i==1):
		name =str(input("enter the name of person"))
		l.append(name)
	elif i==2:
		if len(l)>0:
			print(l.pop(0))
		else:
			print("there is no person for interview")
	elif i==3:
		print("the interview has finished ")
		break
	else:
		print("enter press key is wrong , pls try again later")
	

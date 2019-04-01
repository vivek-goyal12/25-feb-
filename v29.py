str = input("enter a string")
o1=""
o2=""
for i in range(0,len(str)):
	x=ord(str[i])
	if x>64 and x<91:
		o1=o1+str[i]
		
	else:
		o2=o2+str[i]
print(o1)
print(o2)

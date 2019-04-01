str = input("enter a string")
s1=""
for i in range(0,len(str)):
	x=ord(str[i])
	if x%2==0:
		s1=s1+"#"
	else:
		s1=s1+str[i]
print(s1)

		
	


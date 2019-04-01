str = input("enter a string")
m=int(input("enter first index"))
n=int(input("enter last index of sub string"))
i=len(str)
if m>-i and n<=i:
	sub = str[m:n]
	print(str[m:n])
else:
	print("enter index is not correct")


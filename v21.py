#program of factorial number
n = int(input("enter a number"))
temp = n
def fact(n):
	if n==1 or n==0 :
		return 1
	return n*fact(n-1)
print("the fact of %d is"%n,fact(n))	


#c
def fab(n):
	n1 = 0
	n2 = 1
	n = n1+n2
	n1 = n2
	n2=n
	return fab(n)
print(fab(n))


a = int(input("enter the first side  a ="))
b = int(input("enter the second side b ="))
c = int(input("enter the third side  c ="))
if a+b>c and b+c>a and c+a>b:
	if a==b or b==c or c==a:
		print("isoscales")
	elif a*a +b*b == c*c:
		print("right")
	else:
		print("scalene")
else:
	print("invalid")

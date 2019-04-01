n = int(input("enter the money ="))
n = n-100
t = n//2000
n = n%2000
f = n//500
n = n%500
h = n//100
sum = t+f+h+1
print(sum)

#n is name of chidren
# m is name of gift
n=[]
m=[]
for i in range (0,10):
	n.append(input("enter the name of child"))
for i in range(0,10):
	m.append(input("enter the gift name"))
i=0
while i<10:
	i=i+1 
	print("the child name is",n.pop(0), "and got the gift name is",m.pop(-1))



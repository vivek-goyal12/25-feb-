c=0
for i in range(0,1000000):
	s=str(i)
	if len(s)!=0:
		s="0"*(6-len(s))+s
	sum1=int(s[0]) +int(s[1]) +int(s[2])
	sum2=int(s[3]) +int(s[4]) +int(s[5])
	if sum1==sum2:
		c=c+1
		#print(s,end=" ")
print("total count=",c)

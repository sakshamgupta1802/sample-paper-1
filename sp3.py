import math
d=[]
a=list(map(int,input().split()))
for i in a :
	d.append(math.factorial(i))
print((*d),sep=',')
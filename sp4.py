import math
d=list(map(int,input().split(',')))
q=[]
c=50
h=30
for i in d:
	b=math.sqrt((2*c*i)/h)
	q.append(round(b))
print(*q,sep=',')
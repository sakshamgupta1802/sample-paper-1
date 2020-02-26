a=list(map(int,input().split(',')))
b=[]
for i in range(a[0],a[-1]):
		if i not in a:
			b.append(i)
print(b)
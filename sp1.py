b=[]
for i in range(2000,3201):
	if i % 7 and i%5 !=0:
		b.append(i)
print((*b),sep=',')
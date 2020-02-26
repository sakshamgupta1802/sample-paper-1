a=input().lower()
for i in range(97,123):
	if chr(i) not in a:
		print("not a panagram")
		break
else:
	print("panagram")
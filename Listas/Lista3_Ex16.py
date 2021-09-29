a = 0
b = 0

while(b < 500):
	print(b)
	b = b + a
	a = b - a
	if(b == 0):
		b = b + 1

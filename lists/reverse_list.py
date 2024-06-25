print('''Running ''' + __file__ )
L = [1,2,3,4,5]
temp = []

length = len(L) - 1
counter = 0
while counter <= length:
	calc = length - counter
	temp.append(L[calc])
	counter += 1
	print(temp)
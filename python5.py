#Loops and iterations

nums = [1, 2, 3, 4, 5]

for num in nums:
	print(num)

#Break statement

for num in nums:
	if num == 3:
		print('Found')
		break
	print(num) #Wont be run because of break

#Continue statement
	
for num in nums:
	if num == 3:
		print('Found')
		continue
	print(num) 

#Nested loops

for num in nums:
	for letter in 'abc':
		print(num, letter)


#Range

for i in range(10):
	print(i)

#Specify starting value

for i in range(1, 11):
	print(i)

#While loops

x = 0

while x < 10:
	print(x)
	x += 1


#Use of break to exit infinite while loop

x = 0

while True:
	if x == 5:
		break
	print(x)
	x += 1





















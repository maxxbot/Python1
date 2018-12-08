#Conditionals and booleans

#Conditional will be executed if statement after if is true
if True:
	print('Conditional was True')

#Wont print because conditional is false
if False:
	print('Conditional was True')
	
language = 'Python'
if language == 'Python':
	print('Conditional was True')

#Else statement

if language == 'Python':
	print('Language is Python')
else:
	print('No Match')

language = 'Java'
if language == 'Python':
	print('Language is Python')
else:
	print('No Match')

#Elif

language = 'Java'
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('No Match')

#Boolean operations

user = 'Admin'
loggin_in = True

if user == 'Admin' and loggin_in:
	print('Admin Page')
else:
	print('Bad Creds')

loggin_in = False

if user == 'Admin' and loggin_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not loggin_in:
	print('Please Log In')
else:
	print('Welcome')

#Object identity, tests to see if objects are same in memory

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))

b = a
print(a is b)



























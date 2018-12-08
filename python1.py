message = 'Hello World'

message2 = """Jeb!
is
a
MESS"""

print('Hello World')
print(message)
print(message2)
print(len(message2))
print(message2[0])
print(message2[0:4])
print(message2[:4])

#Print message all lower case
print(message2.lower())

#Print message all upper case
print(message2.upper())

#Print times letter or phrase appears
print(message2.count('e'))

#Print index of letter or phrase
print(message2.find('MESS'))

#Find and replace method
message3 = message2.replace('MESS','WASTE')
print(message3)

#String concatenate 

greeting = 'Hello'
name = 'Michael'
print(greeting + ', ' + name)

#Formatted string

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#F string

message = f'{greeting}, {name}. Welcome!'
print(message)



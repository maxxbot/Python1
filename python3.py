#Working with Key-Value Pairs

#Create a Key-Value pair
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

#Print value associated with particular key
print(student['name'])

#Get method
print(student.get('name'))
print(student.get('Jeb!'))

#Default value for keys that don't exist
print(student.get('Jeb!','Not found'))

#Add new entry
student['phone'] = '555-5555'
print(student['phone'])

#Update method
student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)

#Delete key-value pair
del student['age']
print(student)

#Pop method
student['age'] = 25
age = student.pop('age')
print(age)

#Keys and values methods
print(student.keys())
print(student.values())

#Print keys and values with loop
for key, value in student.items():
	print(key, value)






























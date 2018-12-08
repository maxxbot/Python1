#Functions

def hello_func():
	print('Hello Function')
	
print(hello_func)

hello_func()

#Add a return

def hello_func():
	return 'Hello Function'
	
zuck = hello_func()

print(zuck)

#Return can use data type methods

print(hello_func().upper())


#Pass an argument

def hello_func(greeting):
	return '{} Function.'.format(greeting)
	
zuck = hello_func('Jeb!')
print(zuck)

#Add default value

def hello_func(greeting, name = 'You'):
	return '{} {}'.format(greeting, name)

zuck = hello_func('Jeb!')
print(zuck)

#Keyword arguments

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

student_info('Math','Art', name = 'John', age = '22')

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
	
courses = ['Math', 'Art']
info = {'name':'John', 'Age':22}


student_info(courses, info)
student_info(*courses, **info)







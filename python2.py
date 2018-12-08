#Create a list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

#Show list length
print(len(courses))

#Print first value of list
print(courses[0])

#Use -1 index to get the last item
print(courses[-1])

#Print a range of list items
print(courses[0:3])

#Add item to list
courses.append('Art')
print(courses)

#Remove item from list
courses.remove('Art')

#Insert item in list
courses.insert(3,'Art')
print(courses)

#Pop off last item
courses.append('Art')
print(courses)
popped = courses.pop()
print(courses)
print(popped)

#Reverse list order
courses.reverse()
print(courses)

#Sort list in alphabetical order
courses.sort()
print(courses)

#Reverse order sort
courses.sort(reverse=True)
print(courses)

#Return sorted list
sortedlist = sorted(courses)
print(sortedlist)

#Min or max values of list
print(min(courses))
print(max(courses))

#Find index of item in list
print(courses.index('Art'))

#Find if item is in list
print('Math' in courses)

#Print list with for loop
for item in courses:
	print(item)

#Print index and value with enumerate function
for course in enumerate(courses):
	print(course)

for course in enumerate(courses, start=1):
	print(course)


#Turn list into string with join function

course_str = ', '.join(courses)
print(course_str)

course_jeb = 'Jeb!'.join(courses)
print(course_jeb)

#Turn string into list
new_list = course_str.split(', ')
print(new_list)

#Lists - mutable
#Tuples - not mutable

tuple_1 = ('Jeb!', 'is', 'a', 'MESS')
#tuple_1[3] = 'WASTE' - this line will throw an error

print(tuple_1)

#Set - unordered and no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
print('Math' in cs_courses)

#Intersection and difference method
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Sets are more performant for these sorts of operations than lists/tuples







































































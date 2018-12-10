#Import modules and exploring standard library

import python7 as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')

print(index)

#import function only 

from python7 import find_index as fi

print(fi(courses, 'Math'))

#Sys path

import sys 

print(sys.path)

#Standard library modules

import random

random_course = random.choice(courses)

print(random_course)

#Math module

import math
import numpy

rads = math.radians(90)

print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2018))

#OS module gives access to operating system

import os

print(os.getcwd())

#Show location of module

print(os.__file__)







































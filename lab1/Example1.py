#Example 1
print("Hello, World!")

#Example 2
if 5 > 2:
    print("Five is greater than two!")

#Example 3
if 5 > 2:
    print("Five is greater than two!")  
if 5 > 2:
    print("Five is greater than two!")

#Example 4
x = 5
y = "Hello, World!"

#Example 5
#This is a comment.
print("Hello, World!")

#Example 6
print("Hello, World!") #This is a comment

#Example 7
#print("Hello, World!")
print("Cheers, Mate!")

#Example 8
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#Example 9
"""
This is a comment
written in 
more than just one line
"""
print("Hello, World!")

#Example 10
x = 5
y = "John"
print(x)
print(y)

#Example 11
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Example 12
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Example 13
x = 5
y = "John"
print(type(x))
print(type(y))

#Example 14
x = "John"
# is the same as
x = 'John'

#Example 15
a = 4
A = "Sally"
#A will not overwrite a

#Example 16
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example 17
"""
2myvar = "John"
my-var = "John"
my var = "John"
Wroong Variavble Names
"""

#Example 18
# Ways to write long names
myVariableName = "John" #Camel Case
MyVariableName = "John" #Pascal case
my_variable_name = "John" #Snake Case
#Example 19
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example 20
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example 21
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Example 22
x = "Python is awesome"
print(x)

#Example 23
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Example 24
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example 25
x = 5
y = 10
print(x + y)

#Example 26
x = 5
y = "John"
print(x + y)

#Example 27
x = 5
y = "John"
print(x, y)

#Example 28
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example 29
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Example 30
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example 31
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example 32
x = 5
print(type(x))

#Example 33
x = "Hello World"	#str
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#Example 34
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Example 35
print(type(x))
print(type(y))
print(type(z))

#Example 36
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Example 37
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Example 38
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Example 39
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Example 40
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Example 41
import random

print(random.randrange(1, 10))

#Example 42
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Example 43
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Example 44
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Example 45
print("Hello")
print('Hello')

#Example 46
a = "Hello"
print(a)

#Example 47
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example 48
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example 49
a = "Hello, World!"
print(a[1])

#Example 50
for x in "banana":
  print(x)

#Example 51
a = "Hello, World!"
print(len(a))

#Example 52
txt = "The best things in life are free!"
print("free" in txt)

#Example 53
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Example 54
txt = "The best things in life are free!"
print("expensive" not in txt)

#Example 55
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Example 56
b = "Hello, World!"
print(b[2:5])
#Example 57

b = "Hello, World!"
print(b[:5])

#Example 58
b = "Hello, World!"
print(b[2:])

#Example 59
b = "Hello, World!"
print(b[-5:-2])

#Example 60
a = "Hello, World!"
print(a.upper())

#Example 61
a = "Hello, World!"
print(a.lower())

#Example 62
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Example 63
a = "Hello, World!"
print(a.replace("H", "J"))

#Example 64
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Example 65
a = "Hello"
b = "World"
c = a + b
print(c)

#Example 66
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Example 67
age = 36
txt = "My name is John, I am " + age
print(txt)

#Example 68
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example 69
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example 70
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Example 71
txt = "We are the so-called \"Vikings\" from the north."

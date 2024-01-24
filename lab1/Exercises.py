#Syntax
#Exercise1
print("Hello World")
#Exercise2
if 5 > 2:
    print("YES")

#Comments
#Exercise3
#This is a comment
#Exercise4
"""
This is a comment
written in 
more than just one line
"""

#Variables
#Exercise5
carname = "Volvo"
#Exercise6
x = 50
#Exercise7
x = 5
y = 10
print(x+y)
#Exercise8
x = 5
y = 10
z = x + y
print(z)
#Exercise9
x, y, z = "Orange", "Banana", "Cherry"
#Exercise10
x = y = z = "Orange"
#Exercise11
def myfunc():
    global x
    x = "fantastic"

#Data Types
#Exercise12
x = 5
print(type(x))
#Exercise13
x = "Hello World"
print(type(x))
#Exercise14
x = 20.5
print(type(x))
#Exercise15
x = ["apple", "banana", "cherry"]
print(type(x))
#Exercise16
x = ("apple", "banana", "cherry")
print(type(x))
#Exercise17
x = {"name" : "John", "age" : 36}
print(type(x))
#Exercise18
x = True
print(type(x))

#Numbers
#Exercise 19
x = 5
x = float(x)
#Exercise 20
x = 5.5
x = int(x)
#Exercise 21
x = 5
x = complex(x)

#Strings
#Exercise 22
x = "Hello World"
print(len(x))
#Exercise 23
txt = "Hello World"
x = txt[0]
#Exercise 24
txt = "Hello World"
x = txt[2:5]
#Exercise 25
txt = " Hello World "
x = txt.strip()
#Exercise 26
txt = "Hello World"
txt = txt.upper()
#Exercise 27
txt = "Hello World"
txt = txt.lower()
#Exercise 28
txt = "Hello World"
txt = txt.replace(("H"), ("J"))
#Exercise 29
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

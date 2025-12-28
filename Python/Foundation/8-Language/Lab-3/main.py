#variables , constants ,Identifiers/Names
# A variable is a named location in memory that stores a value which can be changed during program execution.
# A constant is a named location in memory that stores a value which cannot be changed once assigned.
# An identifier (or name) is a name used to identify a variable, constant, function, or other entities in a program.

#variable example for data type change
x = 10          # x is an integer variable
print(type(x))       # Output: <class 'int'>
x = "Hello"    # x is now a string variable
print(type(x))      # Output: <class 'str'>

#when assign data type to variable can have a compiler error but runns fine.
#because here python is  dynamically type language .
a:int = 5         # a is an integer variable
print(type(a))      # Output: <class 'int'>
a = 3.14       # a is now a float variable
print(type(a))      # Output: <class 'float'>

#even if python is dynamically typed language it can't do implicit type conversion between Stringh and other data types.
b = "ijse"
c = 10 
print(b+c) # This will raise a TypeError



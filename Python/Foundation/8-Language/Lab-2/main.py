# Class example
class MyClass:
    # I'm in the MyClass class block
    # still in the MyClass class block
    pass
    # still in the MyClass class block

# now I'm in the module block

# Function example
def my_function():
    # I'm in the my_function function block
    pass
    # still in the my_function function block

    def MyInnerFunction():
        # I'm in the MyInnerFunction function block
        pass
        # still in the MyInnerFunction function block

    # now I'm back in my_function function block

# now I'm back in the module block

# -------------------------------
# Integer Data Types (int)

# Binary Integer Literal (0-1)
print(0b1010)  # Output: 10
print(0B1010)  # Output: 10

# Octal Integer Literal (0-7)
print(0o12)    # Output: 10
print(0O12)    # Output: 10

# Hexadecimal Integer Literal (0-9, A-F)
print(0xA)     # Output: 10
print(0XA)     # Output: 10

# Decimal Integer Literal (0-9)
print(10)      # Output: 10
print(-10)     # Output: -10

# Floating-Point Data Types (float)
print(10.5)    # Output: 10.5 

# Example - 37
print(0b100101)  # Output: 37
print(0o45)      # Output: 37
print(0x25)      # Output: 37
print(37)        # Output: 37

print("-------------------------------------")

# Real Number Data Types (float)
# Scientific Notation
print(3.14e2)    # Output: 314.0
print(-3.14e2)   # Output: -314.0
print(3.14E2)    # Output: 314.0
print(-3.14E2)   # Output: -314.0
print(3.14e-2)   # Output: 0.0314
print(-3.14e-2)  # Output: -0.0314
print(3.14E-2)   # Output: 0.0314
print(-3.14E-2)  # Output: -0.0314

# IEEE 754 Standard for Floating-Point Arithmetic
print(0.3 - 0.2)  # Output: 0.09999999999999998
print(0.5 - 0.3)  # Output: 0.2

print("-------------------------------------")

# String Data Types (str)
# Single Quotes
print('Hello, World!')  # Output: Hello, World!

# Double Quotes
print("Hello, World!")  # Output: Hello, World!

# Triple Quotes (multi-line strings)
print('''Hello,
how are you?
World!''')

# Mix of quotes
print("what is 'AI' & 'ML'")
print('what is "AI" & "ML"')

# Escape Sequences
print('It\'s a beautiful day!')  # Output: It's a beautiful day!
print("He said, \"Hello!\"")     # Output: He said, "Hello!"
print("Line1\nLine2")            # Output: Line1
                                  #         Line2
print("Column1\tColumn2")        # Output: Column1    Column2
print("Backslash: \\")            # Output: Backslash: \
print("Carriage Return\rTest")    # Output: Testriage Return
print("Backspace\bTest")         # Output: BackspacTest
print("Form Feed\fTest")         # Output: Form Feed
print("Vertical Tab\vTest")      # Output: Vertical Tab
print("Unicode Character: \u03A9")  # Output: Unicode Character: Ω
print("Unicode Character: \U0001F600")  # Output: Unicode Character:

#String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2 + "!"
print(result)  # Output: Hello, World!
# String Repetition
print("Ha" * 3)  # Output: HaHaHa
# String Slicing
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:])   # Output: World!
#formatted String Literals (f-strings)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age + 20} years old.")  # Output: My name is Alice and I am 50 years old.
# Raw Strings
print(r"C:\Users\Name")  # Output: C:\Users\Name
print(R"C:\Users\Name")  # Output: C:\Users\Name
# Byte Strings
byte_str = b"Hello, World!"
print(byte_str)  # Output: b'Hello, World!'

# None
print(None)

# Python Tuple
print((10, 20, 30))

# Python List
print([10, 20, 30])

# Python Set
print({1, 2, 2, 3})  # duplicates removed

# Python Dictionary, Python Map
print({
    'id': 'C001',
    'name': 'Kasun'
})

print(... ,type(...),type(Ellipsis))  # Output: <class 'ellipsis'>


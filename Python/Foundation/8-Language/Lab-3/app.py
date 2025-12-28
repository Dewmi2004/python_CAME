# 1 - Explicit type conversion between incompatible data types
x = 10
y = "ijse"
print(str(x) + y)  # Convert int to str before concatenation
# Output: 10ijse

# 2 - Using a variable without type annotation (Pyright is fine)
x = 10
print(x, type(x))  # Output: 10 <class 'int'>
x = "ijse"
print(x, type(x))  # Output: ijse <class 'str'>

# 3 - Using type-annotated variable correctly
a: int = 5
print(a, type(a))  # Output: 5 <class 'int'>
# a = "came"  # ❌ Pyright error: cannot assign str to int

# Correct way: either change the type annotation or use a separate variable
b: str = "came"
print(b, type(b))  # Output: came <class 'str'>

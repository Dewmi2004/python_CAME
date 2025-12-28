print('binary comparison operators in python')
#Value = String Representation
x=10
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x} , {repr(x)}')

x=5.2
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=True
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=None
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=...
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=NotImplemented
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

#Value != String Representation

x="IJSE"
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=(5,2)
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x=[5,2]
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x={5,2}
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

x={'id':5,'name':'abc'}
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')



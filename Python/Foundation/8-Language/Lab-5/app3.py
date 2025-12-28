print('binary comparison operators in python')
class Customer:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'Customer'
x=Customer('C001','John Doe')
print(f'Identity={id(x)} ,Data Type={type(x)},String representation ={x}, {repr(x)}')

print('========================================================================')


print('Let\'s expose the value for value comparison operators in python')
class Student:
    def __init__(self, id:int, name:str , marks:int):
        self.id = id
        self.name = name
        self.marks = marks

#This is how we override the String Representation  of the object

    def __repr__(self) -> str:
            # return 'Student'
            return str(['id=',self.id, 'name=',self.name, 'marks=',self.marks])
    def __gt__(self, other:Student)->bool:
        return  self.marks > other.marks
    def __ge__(self, other:Student)->bool:
        return  self.marks >= other.marks

    
s1 = Student(1,'John Doe',85)
s2 = Student(2,'krisha Doe',75)
print(s1 > s2)  # output: True as 85 > 75
print(s1 >= s2)  # output: True as 85 >= 75



# print(s1>s2)  
# This will give error as '>' not supported between instances of 'Student' and 'Student'

#To overcome this we need to override the comparison operator methods
# object.__lt__(self, other)
# object.__le__(self, other)
# object.__eq__(self, other)
# object.__ne__(self, other)
# object.__gt__(self, other)
# object.__ge__(self, other)

# if an object is implemented rich comparison methods then value comparison operators works with the object 
#else it will give error(TypeError)

# print(10 >12) #Rich comparison works as int class has implemented __gt__ method
# print(10 <12) #Rich comparison works as int class has implemented __lt__ method
# print(s1 == s2)  #Rich comparison works as __eq__ is implemented by default in object class
# print(s1 != s2)  #Rich comparison works as __ne__ is implemented by default in object class

# print(s1 > s2)  #TypeError: '>' not supported between instances of 'Student' and 'Student'
# print(s1<s2)   #TypeError: '<' not supported between instances of 'Student' and 'Student'
# print(s1>=s2)  #TypeError: '>=' not supported between instances of 'Student' and 'Student'
# print(s1<=s2)  #TypeError: '<=' not supported between instances of 'Student' and 'Student'



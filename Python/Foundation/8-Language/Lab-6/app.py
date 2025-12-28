x = 10 + 15
#print(x)
#print(x= 10 + 15)

x=10 + 15
if x > 20:print("x is greater than 20")

x = 10 + 15
#if (x= 10 + 15)> 20:print("x is greater than 20")#not a expression

if (x:= 10 + 15)> 20:print("x is greater than 20")#it is a expression

y = 10
a = (x := y + 5)

x= 5
y = 10 + 12 if x>3 else x - 3
print(y)

print(2 if 10 else 3)
print(2 if "hello" else 3)
print(2 if [1,2,3] else 3)
print(2 if {1: 'a'} else 3)
print(2 if 0.01 else 3)

print("---falsy values---")



print(2 if 0 else 3)
print(2 if "" else 3)
print(2 if [] else 3)
print(2 if None else 3)
print(2 if {} else 3)
print(2 if () else 3)
print(2 if 0.0 else 3)

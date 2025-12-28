#----------------------lambda expression---------------------

# python interpreter persepective : this is an annonymous function 


z = lambda a,b,c : a + b + c
print(z(10,20,30))#call expression
print(z(5,15,25))

#immediate invocation expression
# python programmer perspective : this is  an annonymous function

y =(lambda a,b,c : a+b+c)(10,20,30)
print(y)

x = 3
print(x:=((lambda x,y :x-y)(y = x , x= (3+4)))+5+x)
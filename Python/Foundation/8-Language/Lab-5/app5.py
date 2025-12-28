print('Evaluating of built-in types Rich Comparison methods in python')

#with boolean values
print(f'True > False : {True > False}') # 1>0  # output: True
print(f'True < False : {True < False}') # 0<1  # output: False
print(f'True >= False : {True >= False}')# 1>=0  # output: True
print(f'True <= False : {True <= False}') # 0<=1  # output: False
print(f'True == False : {True == False}') # 1==0  # output: False
print(f'True != False : {True != False}') # 1!=0 # output: True

#with string values => Note: String comparisons are based on lexicographical order (dictionary order) using Unicode values of characters.
                            # first character of first word is compared to first character of second word.
                            
print(f'"apple" > "banana" : {"apple" > "banana"}') # output: False as 'a' has lower unicode value than 'b'
print(f'"apple" < "banana" : {"apple" < "banana"}') # output: True as 'a' has lower unicode value than 'b'
print(f'"apple" >= "banana" : {"apple" >= "banana"}') # output: False as 'a' has lower unicode value than 'b'
print(f'"apple" <= "banana" : {"apple" <= "banana"}') # output: True as 'a' has lower unicode value than 'b'
print(f'"apple" == "banana" : {"apple" == "banana"}') # output: False
print(f'"apple" != "banana" : {"apple" != "banana"}') # output: True

#with integer values
print(f'10 > 5 : {10 > 5}')  # output: True
print(f'10 < 5 : {10 < 5}')  # output: False
print(f'10 >= 5 : {10 >= 5}') # output: True
print(f'10 <= 5 : {10 <= 5}') # output: False
print(f'10 == 5 : {10 == 5}') # output: False
print(f'10 != 5 : {10 != 5}') # output: True

#with float values
print(f'10.5 > 5.2 : {10.5 > 5.2}')  # output: True
print(f'10.5 < 5.2 : {10.5 < 5.2}')  # output: False
print(f'10.5 >= 5.2 : {10.5 >= 5.2}') # output: True
print(f'10.5 <= 5.2 : {10.5 <= 5.2}') # output: False
print(f'10.5 == 5.2 : {10.5 == 5.2}') # output: False
print(f'10.5 != 5.2 : {10.5 != 5.2}') # output: True

#with tuple values
print(f'(1, 2, 3) > (1, 2, 2) : {(1, 2, 3) > (1, 2, 2)}')  # output: True
print(f'(1, 2, 3) < (1, 2, 2) : {(1, 2, 3) < (1, 2, 2)}')  # output: False
print(f'(1, 2, 3) >= (1, 2, 2) : {(1, 2, 3) >= (1, 2, 2)}') # output: True
print(f'(1, 2, 3) <= (1, 2, 2) : {(1, 2, 3) <= (1, 2, 2)}') # output: False
print(f'(1, 2, 3) == (1, 2, 2) : {(1, 2, 3) == (1, 2, 2)}') # output: False
print(f'(1, 2, 3) != (1, 2, 2) : {(1, 2, 3) != (1, 2, 2)}') # output: True

#with list values
print(f'[1, 2, 3] > [1, 2, 2] : {[1, 2, 3] > [1, 2, 2]}')  # output: True
print(f'[1, 2, 3] < [1, 2, 2] : {[1, 2, 3] < [1, 2, 2]}')  # output: False
print(f'[1, 2, 3] >= [1, 2, 2] : {[1, 2, 3] >= [1, 2, 2]}') # output: True
print(f'[1, 2, 3] <= [1, 2, 2] : {[1, 2, 3] <= [1, 2, 2]}') # output: False
print(f'[1, 2, 3] == [1, 2, 2] : {[1, 2, 3] == [1, 2, 2]}') # output: False
print(f'[1, 2, 3] != [1, 2, 2] : {[1, 2, 3] != [1, 2, 2]}') # output: True

#with map values => # Note: Other comparisons with dict (like <, >, <=, >=) will raise TypeError in Python 3.

print(f'{{"a":1, "b":2}} == {{"a":1, "b":2}} : {{"a":1, "b":2} == {"a":1, "b":2}}')  # output: True
print(f'{{"a":1, "b":2}} != {{"a":1, "b":2}} : {{"a":1, "b":2} != {"a":1, "b":2}}')  # output: False

#with set values => Note: Other comparisons with set (like <, >, <=, >=) will raise TypeError in Python 3.
print(f'{{1, 2, 3}} == {{1, 2, 3}} : {{1, 2, 3} == {1, 2, 3}}')  # output: True
print(f'{{1, 2, 3}} != {{1, 2, 3}} : {{1, 2, 3} != {1, 2, 3}}')  # output: False


#with None values => Note: Other comparisons with None (like <, >, <=, >=) will raise TypeError in Python 3.
print(f'None == None : {None == None}')  # output: True
print(f'None != None : {None != None}')  # output: False
print(f'None is None : {None is None}')  # output: True
print(f'None is not None : {None is not None}')  # output: False

#with NotImplemented values => Note: Other comparisons with NotImplemented (like <, >, <=, >=) will raise TypeError.
print(f'NotImplemented == NotImplemented : {NotImplemented == NotImplemented}')  # output: True
print(f'NotImplemented != NotImplemented : {NotImplemented != NotImplemented}')  # output: False
print(f'NotImplemented is NotImplemented : {NotImplemented is NotImplemented}')  # output: True 
print(f'NotImplemented is not NotImplemented : {NotImplemented is not NotImplemented}')  # output: False

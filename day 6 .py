'''
Tuple
------

-->Tuple is a collection of different data types that represent by() and the items in tuple is seperated by comma..
'''

so = (3,"Python",[4,8],(5,4),1)
print(so[3])

so = (10,20,30,40)
any=(50,60,70)
print(so+any)

'''
Dictionary
----------
-->Dict is a collection of key : value pair, where keys are immutable such as (string,int and tuple) and values are any data type and this is represented by {} brackets
Methods
------

key()---> this is method is used to access only keys in the dictionary
syntax--> dict.keys()
'''
my = {"Name":"Layya","age":22,"Edu":"B.Tech"}
print(my.keys())    
'''
values()
'''
my = {"Name":"Layya","age":22,"Edu" :"B.Tech"}
print(my.values())   

'''
items()
-->this method is used to access key: value pair in the dictionary
'''
my = {"Name":"Layya","age":22,"Edu" :"B.Tech"}
print(my.items())   

'''
clear()-->this method is used to delete all the items in the dict
syntax --> dict.clear()
'''
my.clear()
print(any)

'''
update-->this method is used to add new (key : value) into the
dictionary
syntax-->dict.update{(key:value)}
'''
my = {"Name":"Layya","age":22,"Edu":"B.Tech"}
my.update({"role":"python developer"})
print(my)

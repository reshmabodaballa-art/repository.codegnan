'''
print statement
---------
--> this print statement shows output on the screen

return statement
------------
--> this return sends a value back to the caller or calling for the program to reuse

'''

def great(name):
    print(f"hello {name}")
    result =great("bob")
    print(result)
    
'''
in-built functions:

1.len()
----
--> this is used to find out the lengh/number of values present in the itterables.
2.max()
--> this is used to get the maximum value
--> couldn't use different data type in one time we get error
example1:
str = "python is a 54 programming language"
print(max(str)) # get error
example2:
m = ["python",44,33,455,"program"]
print(max(m))
3.min()
-----
--> this used to get the minimum value.
4.type()
--> find the which data type is stored in the variable.

5.range()

6.recursive
--> A recursive function calls itself until a base case is stops it

'''
list = [1,2,3,4,5]
print(max(list))

list = [1,2,3,4,5]
for i in list:
    print(i)
    
str = "python is a programming language"
print(max(str))

list = [1,2,3,4,5]
print(min(list))
      
def Fact(num):
    if num == 0 or num == 1:
        return 1
    return num * Fact(num-1)
print(Fact(6))

num = 5
for i in range(1,11):
    print(num, "x", i,"=", num*i)
    
num = 5
for i in range(1,11):    
    print(f"{num} x {i} = {num*i}")


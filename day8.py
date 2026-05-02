'''
user input
--> int data type

an = int(input("Enter the number: "))
print(type(an))
--> string data type

any = input("Enter the word: ")
print(type(any))

--> split funtion
a,b = map(int,input("enter two numbers: ").split())
print(a)
print(type(a))
print(b)
print(type(b))

--> list data type
sn = list(map(int,input("Enter the number: ").split()))
print(type(sn))
print(sn)

---> tuple data type
sn = tuple(map(int,input("Enter the number: ").split()))
print(type(sn))
print(sn)

if condition
--> this is used to check condition is true or not

else condition



eval()
-->
'''
# input int()
an = int(input("Enter the number: "))
print(type(an))

# input str()
any = input("Enter the word: ")
print(type(any))

# split()
a,b = map(int,input("enter two numbers: ").split())
print(a)
print(type(a))
print(b)
print(type(b))

# list()
sn = list(map(int,input("Enter the number: ").split()))
print(type(sn))
print(sn)

# tuple()
sn = tuple(map(int,input("Enter the number: ").split()))
print(type(sn))
print(sn)

# f function
a = 33
b = 6
print("added a and b the result is",a+b)
print(f"added a and b the result is",a+b)
print("a+b = ",a+b)
print(f"a+b ={a+b}")
print(f"{a} + {b}={a+b}")

# if condition
an = 9
if an > 9:
    print(f"an is greater then {9}")

# else condition   
an = 9
if an > 9:
    print(f"an is greater then {9}")
else:
    print(f"an is not greater then {9}")

# example
so = 4
if so == 4:
    print(f"so is equal to {4}")
else:
    print(f"so is not greater then {4}")

# eval()
a = eval(input("Enter :"))
print(type(a))
print(a)
v = eval(input("Enter :"))
print(type(v))
print(v)

num = 7
num_2 = 23
if num > num_2:
    print(f"{num} is greater then {num_2}")
else:
    print(f"{num} is less than {num_2}")

# examples
age = 6
if age >= 18:
    print(f"you are eligible to vote")
else:
    print(f"you have to wait {18-age} more years")

age =int(input("Enter your age:"))
if age >= 18:
    print(f"you are eligible to vote")
else:
    print(f"you have to wait {18-age} more years")


result =int(input("enter your marks:"))
if result >= 35:
    print(f"you are pass")
else:
    print(f"you are not pass")























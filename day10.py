'''
While statement
-------
--> This while statement will keep on excuting untill unless condition becomes true

range()
--------
--> This range() will generate squence numbers upto the limit
Synatax
---> range(starting,ending,step)

'''
# while statement
v = 1
while v <= 5:
    print(v)
    v += 1

# range()    
choice_u = int(input("enter the limit:"))
for j in range(100, choice_u):
    print(j)

choice_u = int(input("enter the limit:"))
for j in range(100, choice_u,2):
    print(j)

for i in range(2,101):
    if i % 2 == 0:
        print(f"{i} is even number")
else:
    print(f"{i} is odd number")

'''
Control statements
1.break
--------
--> This break statement will exit if the condition becomes true, and never execute/enter into next loops

2. continue:
--> this statement will skip that particular itteration and goes to next itteration

3. pass
--> pass is space holder, holds the space not to get any syntax error 


nested loop
--->  A loop inside the loop is called nested loop

'''

any = ["reshma","laya","sarayu","anusha"]
for i in any:
    if i == "sarayu":
       break
    print(i)

# continue
any = ["reshma","laya","sarayu","anusha"]
for i in any:
    if i == "laya":
        continue
    print(i)

# pass          
a = 9
b = 90
if a >= b:
    pass

# prime num
num = 23
count = 0
for an in range(1,num+1):
    if num % an == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

for j in range(2,100):
    count = 0
    for an in range(1,j+1):
        if j % an == 0:
            count += 2
    if count == 2:
        print(f"{j} is a prime")
    else:
        print(f"{j} is not a prime")





































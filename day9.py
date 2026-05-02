'''
elif statement

---> this statement gives more options to get result of that program
example:
'''
marks_stu = int(input("Enter your marks:"))
if marks_stu >= 90:
    print("A+")
elif marks_stu >= 80:
    print("A")
elif marks_stu >= 70:
    print("B+")
elif marks_stu >= 60:
    print("B")
elif marks_stu >= 50:
    print("C+")
else:
    print("Failed")

'''
nested if statement

---> if statemnt in side another if statement is called nested if statement

'''
# example
user_SBI_info={"ATM PIN": "7700"}
user_pin = input("Enter your ATM: ")
if len(user_pin) == 4:
    if user_pin in user_SBI_info["ATM PIN"]:
        print("Welcome to SBI ATM")
    else:
        print("please enter the correct pin")
else:
    print("please enter 4 digit pin")

'''
for loop
---> A for statement is used to iterate over items like (string,list,tuple) with fixed number of itterations 

'''
# example
any = [16,21,35,43]
for j in any:
    print(j)

'''
else statement in for
---> After completing all itterations this else statement will excute 
'''

any = [6,1,5,4]
for j in any:
    print(j)
else:
    print("Loop finished")

# example

so = "madam"
empty = ""
for j in so:
    empty = j + empty
if empty == so:
    print("Palindrom")
else:
    print("not a Palindrom")

'''
while statement
-----


'''













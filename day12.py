'''
remove duplicates in list

'''
so = eval(input("Enter items of list: "))
empty = []
for i in so:
    if i not in empty:
        empty.append(i)
print(empty)        

'''
find second maximum number in list
'''

num = [1,2,3,4,5]
max1 = 0  # assume verey small number
max2 = 0 
for i in num:
    if i > max1:
        max2 = max1
        max1 = i
print(f"{max2} is the second maximum in the list {num}")


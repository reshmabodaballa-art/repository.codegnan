'''
Set data type
-->Set is collection of unordered elements or unique elements unlike list or tuple set is not permit duplicates in side.

Methods
------
add()
--> This method is used to add new item into the set
syntax--> Variable_name.add(item)
'''
'''
remove()
-->this method is used to delete an item in the set
syntax-->variable_name.remove(value)
'''
'''
pop()
--->This is also used to delete element in the set, but we can not specify the element
syntax-->variable_name.pop(no arguments)
'''
'''
clear()
-->this method is used to delete all elements in the set
syntax--> variable_name.clear()
'''
'''
update()
--> same like add but this method will add more than one element
syntax--> variable_name.update([element])
'''
'''
union()
--->this method will return a set all elements from both sets ,but not duplicates
syntax-->set_1.union(set_2) or set_1| set_2
'''

'''
intersection()
-->this method will give only the common elements from both sets
syntax-->set_1.intersection(set_2) or set_1 & set_2

'''

'''
difference()
-->this method is used to get the different elements from both sets
syntax-->set1.difference(set_2) or set_1-set_2
'''
'''
type conversions
-->converting one data type into another data type 
'''
# add()
sn={1,2,3,6}
sn.add(4)
print(sn)

#remove()

sn={1,2,3,6}
sn.add(74)
print(sn)
sn.remove(3)
print(sn)

#pop()
sn={1,2,3,6}
sn.pop()
print(sn)

#clear()

sn={1,2,3,6}
sn.clear()
print(sn)

#update()

sn={1,2,3,4,5}
sn.update([6,7,9])
print(sn)

#union()
sn={1,2,3,4,5,6}
vn={2,4,6}
print(sn.union(vn))

#intersection()
sn={1,2,3,4,5,6}
vn={3,4,5}
print(sn.intersection(vn))
print(sn&vn)

#difference()
sn={1,2,3,4,5,6}
vn={3,4,5}
print(sn.difference(vn))
print(sn-vn)

#int-->string and float
a=8
b=str(8)
c=float(a)
print(c)

#float-->string and int
z=56.78
d=int(z)
g=str(z)
print(g)
print(type(g))

#string-->int,float,list,tuple
c="67"
i=tuple(c)
print(i)
print(type(i))

#
r=[1,2]
u=tuple(r)
print(u)
print(type(u))

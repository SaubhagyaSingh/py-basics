list1 = ['a', 1, 'b', 2]
print(list1)
list1.append('c')  # used to add single elements in a list
print(list1)
list1.extend([3, 'e', 5])  # used to add multiple values
print(list1)
list1.insert(6, ['d', 4])  # inserts at a specific index
print(list1)
list1.pop()
print(list1)
list1.remove('b')
print(list1)
del list1[2]
del list1[5]
print(list1)
list1.extend([2])#numbers need to be added with []
print(list1)

list1.clear()
print(list1)

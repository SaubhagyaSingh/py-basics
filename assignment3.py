even, odd = 0, 0
list1 = []
for i in range(0, 9):
    b = int(input("enter element {} ".format(i+1)))
    if b % 2 == 0:
        even += 1
    else:
        odd += 1
    list1.append(b)

print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print(len(list1))
num = int(input("enter the number to know its frequency "))
print(list1.count(num))

list2 = [1, 3, 5, 7]
list3 = list1+list2
print("The  total number of odd elements in list1 are:", odd)
print("The total number of even elements in list1 are:", even)

print(sorted(list3))

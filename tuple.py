# this is a tuple as its inside parenthesis and not brackets
coordinates = (4, 5)
nottuple = [2, 5]
print(nottuple[1])  # this is a list as it uses brackets
print(coordinates[0])
nottuple[1] = 6
print(nottuple[1])  # the values can be changed in lists
# coordinates[1]=7           wont work........
# print(coordinates[1])          values wont change in the case of tuples
boing = (1, 2, 4, "btech", "timewaste", "lmao", ["demn", "bro"], "lmao")
# boing[4] = "timeuse"
print(boing[3:])
boing[6][0] = "damn"
print(boing[0])
print(boing[3:])
boing2 = ("hehehaha",)
boing = boing+boing2
print(boing[3:])
boing = boing+("huhuhu",)
print(boing[3:])
print(boing.count("lmao"))
print(zip(boing, boing2))
bt = dict(zip(boing, boing2))
print(bt)
list1 = {"name", "age"}
list2 = {"nandan", "old enough to die"}
bt2 = dict(zip(list1, list2))
print(bt2)
print(sorted(bt2.values()))
print(sorted(bt2.keys()))

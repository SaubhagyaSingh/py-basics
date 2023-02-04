def casecounter(str):
    print("Entered string is:", str)
    upper = 0
    lower = 0
    for i in str:
        if i.islower():
            lower = lower+1
        elif i.isupper():
            upper = upper+1
    print("The total number of uppercase letters are : ", upper)
    print("The total number of lowercase letters are : ", lower)


x = str(input("enter  any string : "))
casecounter(x)

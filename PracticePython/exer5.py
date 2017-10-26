import random

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    m= ['paul', 'bob', 'tom', 'peter']
    n= ['mary', 'bob']
    r= []

    c= []

    for i in a:
        if (i in b) == True and (i in c) == False:
            c.append(i)
        c.sort()

    """for j in b:
        if (j in c) == False:
            c.append(j)
    c.sort()"""

    print(c)

    for i in n:
        if (i in m) == True and (i in r) == False:
            r.append(i)

    """for j in m:
        if (j in r) == False:
            r.append(j)"""

    #r.sort()
    print(r)

    #num_a = int(input("Please enter "))
    print("********BONUS*********")

    num1 = int(input("Please choose a number to create first list: "))
    num2 = int(input("Please choose a number to create second list: "))

    num1ListRange = list(range(1, num1 + 1))
    num2ListRange = list(range(1, num2 + 1))

    divisorList = []

    for number in num2ListRange:
        if num2 % number == 0:
            divisorList.append(number)

    print("First list is:")
    print(num1ListRange)
    print("\n Second list is:")
    print(divisorList)

    commonList = []

    for x in num1ListRange:
        if (x in divisorList) == True and (x in commonList) == False:
            commonList.append(x)

    print ("\n\nCommon List is" )
    print (commonList)
    print ("\n\n")

    list1 = random.sample(range(20), 13)
    list2 = random.sample(range(20), 13)
    ran = []
    print ("Random List 1:")
    print(list1)
    print ("Random List 2:", list2)

    for y in list1:
        for z in list2:
            if y == z:
                ran.append(y)
    #ran.sort()

    print ("The commmon values: ", ran)


main()

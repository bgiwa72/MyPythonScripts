def main():

    target = int (input("Please enter a number: "))
    i=0
    d1 = []
    while (i < target):
        i = i + 1
        if target%i == 0:
            d1.append(i)

    print (d1)

def alt_main():
    num = int(input("Please choose a number to divide: "))

    listRange = list(range(1, num + 1))

    divisorList = []

    for number in listRange:
        if num % number == 0:
            divisorList.append(number)

    print(divisorList)



main()

alt_main()



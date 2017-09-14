import sys

def main():
    reqNum = int(input ("Please enter a number:"))
    num = int(input("Please enter number to check: "))
    check = int (input("Please enter divisor number: "))
    if (reqNum)%2 == 0:
        if reqNum%4 == 0:
            print ("Your number %r is a multiple of 4" %reqNum)
        else:
            print("Your number %r is an even number!!!" %reqNum)

    elif reqNum%2 == 1:
        print("Your number %r is an odd number!!!" %reqNum)
    else:
        print("Invalid entry!!!")
        sys.exit()

    if check == 0:
        print("Invalid divisor number!!!")
        sys.exit()

    elif num%check == 0:
        print("%r is a factor of %r" %(check,num))
    else:
        print("%r is NOT a factor of %r" %(check, num))

main()

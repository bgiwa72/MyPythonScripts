import datetime

curDate = datetime.datetime.now()
print(curDate)

def centSub(var1):
    result = 100 - var1
    return result

def calcYear(y):
    z=curDate.year+y
    return z


def main():
    name = input("Please enter your name: \n")
    age = int(input("Please enter your age: "))
    print curDate
    print curDate.year
    print curDate.month
    print curDate.day
    print curDate.ctime()
    x=centSub(age)
    year=calcYear(x)
    #print("Hi " + name + " !!!")
    #print("You will turn 100 years in " + str(curDate.year + age))
    #print("You will turn 100 years in " + str(year))
    msg1 = "Hi " + name + " !!!\n"
    msg2 = "You will turn 100 years in " + str(year) + " \n"
    print(msg1)
    print(msg2)
    factor = int(input("Please enter a positive number: "))
    if factor < 1:
        print ("Invalid number!!!")
    else:
        msg1 = "Hi " + name + " !!!\n"
        msg2 = "You will turn 100 years in " + str(year) + " \n"
        print ((factor)*msg1)
        print ((factor)*msg2)


main()
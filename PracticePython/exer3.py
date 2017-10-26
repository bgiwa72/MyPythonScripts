
def main():
    a = [1,1,2, 3, 5, 8, 13, 21, 34, 55, 89]
    print a
    a2 = []
    j=0
    for i in a:
        if (i<5):
           a2.append(i)
    print(a2)
    #print a[:4]
    print([i for i in a if i < 5])
    num = int(input("Please enter an integer: "))
    a3 = []
    for i in a:
        if (i<num):
            a3.append(i)
    print(a3)

main()
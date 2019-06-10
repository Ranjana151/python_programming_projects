# pattern print program based on user input

while(True):
    n = int(input("Enter 1 or 0"))
    if n==1:

        n1=int(input("Enter the numbers of steps u want to print "))

        for i in range(0,n1):
            for j in range(i):
                print('*',end="")
            print('')

    elif n==0:
        n2 = int(input("Enter the numbers of steps u want to print "))

        for i in range(n2,0,-1):
            for j in range(i):
                print("*", end="")
            print('')
    else:
        print("Invalid input")
        break


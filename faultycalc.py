print("Welcome in faulty calculator")

while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    ch=int(input("Enter the operator\n"))
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    if (ch==1 and a==76 and b==5):
        print("85")
    elif(ch==2 and a==100 and b==40):
        print("50")
    else:
        if(ch==1):

            res=a+b
            print(res)
        elif(ch==2):

            res = a -b
            print(res)
        elif(ch==3):
            res=a*b
            print(res)
        elif(ch==4):
            res=a/b
            print(res)




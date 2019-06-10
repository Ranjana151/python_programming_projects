#Health Management System
import datetime
def gettime():
    return datetime.datetime.now()
while(True):
    print("1.For write")
    print("2.For retrive")
    n = int(input())

    if n==1:
        print("f For food")
        print("e For excise")
        n2=(input())
        if n2=="f":
            print("Enter 1 for sunny ")
            print("Enter 2 for sagar ")
            print("Enter 3 for aman ")
            name = int(input())
            if name == 1:
                food = input("Enter the morning food\n")
                food1=input("Enter the afternoon food\n")
                food2=input("Enter the evening snacks\n")
                food3=input("Enter the night food\n")
                with open("sunny.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + food + "\n")
                    f.write(str([str(gettime())]) + ":" + food1 + "\n")
                    f.write(str([str(gettime())]) + ":" + food2 + "\n")
                    f.write(str([str(gettime())]) + ":" + food3 + "\n")
                    print("Write sucessfully")
            elif name == 2:
                food = input("Enter the food\n")
                food1 = input("Enter the afternoon food\n")
                food2 = input("Enter the evening snacks\n")
                food3 = input("Enter the night food\n")
                with open("sagar.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + food + "\n")
                    f.write(str([str(gettime())]) + ":" + food1 + "\n")
                    f.write(str([str(gettime())]) + ":" + food2 + "\n")
                    f.write(str([str(gettime())]) + ":" + food3 + "\n")
                    print("Write sucessfully")
            elif name == 3:
                food= input("Enter the food\n")
                food1 = input("Enter the afternoon food\n")
                food2 = input("Enter the evening snacks\n")
                food3 = input("Enter the night food\n")

                with open("aman.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + food + "\n")
                    f.write(str([str(gettime())]) + ":" + food1 + "\n")
                    f.write(str([str(gettime())]) + ":" + food2 + "\n")
                    f.write(str([str(gettime())]) + ":" + food3 + "\n")
                    print("Write sucessfully")
            else:
                print("Invalid input")

        elif(n2=="e"):

            print("Enter 1 for sunny ")
            print("Enter 2 for sagar ")
            print("Enter 3 for aman ")
            name=int(input())
            if name==1:
                excise=input("Enter the excise\n")
                with open("sunny_ex.txt","a") as f:
                    f.write(str([str(gettime())])+":" +excise+"\n")
                    print("Write sucessfully")
            elif name==2:
                excise = input("Enter the excise\n")
                with open("sagar_ex.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + excise + "\n")
                    print("Write sucessfully")
            elif name==3:
                excise = input("Enter the excise\n")
                with open("aman_ex.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + excise + "\n")
                    print("Write sucessfully")
            else:
                print("Invalid input")




    elif n==2:
        print("press 1 for retrive food file")
        print("press 2 for retrive excise file")
        n3=int(input())
        if n3==1:
            print("Enter 1 for sunny retrive")
            print("Enter 2 for sagar retrive ")
            print("Enter 3 for aman retrive ")
            name = int(input())
            if name==1:
                with open("sunny.txt","r") as f:
                    for i in f:
                        print(i,end="")
            elif name==2:
                with open("sagar.txt","r") as f:
                    for i in f:
                        print(i,end="")

            elif name == 3:
                with open("aman.txt", "r") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("Invalid input")
        elif n3==2:
            print("Enter 1 for sunny retrive")
            print("Enter 2 for sagar retrive ")
            print("Enter 3 for aman retrive ")
            name = int(input())
            if name == 1:
                with open("sunny_ex.txt", "r") as f:
                    for i in f:
                        print(i, end="")
            elif name == 2:
                with open("sagar_ex.txt", "r") as f:
                    for i in f:
                        print(i, end="")

            elif name == 3:
                with open("aman_ex.txt", "r") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("Invalid input")

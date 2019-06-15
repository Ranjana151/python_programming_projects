# fun Game
import random
Number_Of_chances=10
No_of_points_gamer=0
No_of_points_computer=0

while (Number_Of_chances>0):
    print("Total no. of chances is 10")
    print("Enter 1 to choose snake")
    print("Enter 2 to choose water")
    print("Enter 3 to choose gun")
    n=int(input())
    list=['snake','water','gun']
    computer_choose=random.choice(list)
    if(n==1 and computer_choose=="water"):
        print("Computer Choose", computer_choose)
        print("You choose snake")
        print("You won")
        Number_Of_chances=Number_Of_chances-1
        No_of_points_gamer=No_of_points_gamer+1
        print("Total Number of points of You is ",No_of_points_gamer)
        print("Total Number of points of computer is ",No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)

    elif(n==1 and computer_choose=="gun"):
        print("Computer Choose", computer_choose)
        print("You choose snake")
        print("Computer won ")
        Number_Of_chances = Number_Of_chances - 1
        No_of_points_computer = No_of_points_computer + 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)
    elif (n == 1 and computer_choose == "snake"):
        print("Computer Choose", computer_choose)
        print("You choose snake")
        print("Tie ")
        Number_Of_chances = Number_Of_chances - 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are",Number_Of_chances)

    elif (n == 3 and computer_choose == "snake"):
        print("Computer Choose", computer_choose)
        print("You choose gun")
        print("You won")
        Number_Of_chances = Number_Of_chances - 1
        No_of_points_gamer = No_of_points_gamer + 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)


    elif (n ==3 and computer_choose == "water"):
        print("Computer Choose", computer_choose)
        print("You choose snake")
        print("You won")
        Number_Of_chances = Number_Of_chances - 1
        No_of_points_gamer = No_of_points_gamer + 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)




    elif (n ==3 and computer_choose == "gun"):
        print("Computer Choose", computer_choose)
        print("You choose gun")
        print("Tie ")
        Number_Of_chances = Number_Of_chances - 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)


    elif (n ==2 and computer_choose == "snake"):
        print("Computer Choose", computer_choose)
        print("You choose water")
        print("Computer won ")
        Number_Of_chances = Number_Of_chances - 1
        No_of_points_computer = No_of_points_computer + 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)

    elif (n ==2 and computer_choose == "gun"):
        print("Computer Choose", computer_choose)
        print("You choose water")
        print("You won")
        Number_Of_chances = Number_Of_chances - 1
        No_of_points_gamer = No_of_points_gamer + 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are", Number_Of_chances)


    elif (n ==2 and computer_choose == "water"):
        print("Computer Choose", computer_choose)
        print("You choose water")
        print("Tie ")
        Number_Of_chances = Number_Of_chances - 1
        print("Total Number of points of You is ", No_of_points_gamer)
        print("Total Number of points of computer is ", No_of_points_computer)
        print("Total number of chances left are",Number_Of_chances)
    else:
        print("Invalid Input")
if(No_of_points_computer>No_of_points_gamer):
    print("You loss this game:Better Luck for next time")
elif(No_of_points_computer<No_of_points_gamer):
    print("You won ")
elif(No_of_points_gamer==No_of_points_computer):
    print("Tie")






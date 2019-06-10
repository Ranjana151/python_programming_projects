n=20
Number_of_chances=4

while(Number_of_chances>=1):
    gu=int(input("Guess the number\n"))


    if gu>25:
        print("Less the number")
        Number_of_chances =Number_of_chances-1
        print("Number of chances remaining",Number_of_chances)
    elif gu>20 and gu<=25:
        print("Just near the guess less the number")
        Number_of_chances = Number_of_chances - 1
        print("Number of chances remaining", Number_of_chances)
    elif gu<20:
        print("Increase the number")
        Number_of_chances = Number_of_chances - 1
        print("Number of chances remaining", Number_of_chances)

    elif gu==20:
        print("Right Answer")
        break
    elif(Number_of_chances==0):
        print("Game over")
        break

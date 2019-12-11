import random                                                                                                  
You=int(input("Enter your choice \n 1.Rock\n 2.Sciccor\n 3.Paper\n"))
computer =random.randrange(1,3)

if((You==1 and computer==2) or (You==2 and computer==3) or (You==3 and computer==1)) :
    print("Computer Choice:",computer)
    print("Your Choice:",You)
    print("You have won")
elif You==computer:
    print("Computer Choice:",computer)
    print("Your Choice:",You)
    print("Its a tire")    
else:
    print("Computer Choice:",computer)
    print("Your Choice:",You)
    print("You lost,,maybe try again")
print(computer)

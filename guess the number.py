from random import randrange
def function(guessed,irand):
    if (guessed < irand):
        return 0;
    elif (guessed > irand):
        return 1;
    else:
        return 2;

print("Lets start the game")
irand=randrange(1,101)

while(1):
    guessed=int(input("Guess the number"))
    check=function(guessed,irand)
    if(check==0):
        print("The number guessed is less than the actual number")
    elif(check==1):
        print("The number guessed is more than the actual number")
    else:
        print("U guessed it right")
        break
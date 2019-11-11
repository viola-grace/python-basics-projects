from random import randrange
ch=input("Shall we roll the die? -y/n")
fix=int(input("Fix the number u wanna reach,lets see how many tries u take! "))
print("u fixed",fix)
chance=0
while(1):
    if(ch=='y'):
        chance=chance+1
        print("Roll ",chance)
        irand=randrange(1,7)
        print(irand)
        if (irand == fix):
            print("Yes,u won by", chance, "chances")
            break
        ch = input("Shall we roll the die again? -y/n")
    else:
        break

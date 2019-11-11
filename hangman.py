from random import randrange

print("HANGMAN")
mylist=["keyboard","mirror","apple","grapes","ladder","bedspread","faucet","leakage"]

irand=randrange(0,8)

choosenstr=mylist[irand]
len=len(choosenstr)
life=10
flg=0
count=0
res=[]
ind=0

for i in range(0,len):
    res.append("*")

while(life>0):
    ch=input("Enter a character ")
    for i in range(0,len):
        if(ch == choosenstr[i]):
            ind=i;
            if(res[ind]=='*'):
                res[ind]=ch
                count+=1
                flg=1
    if (count == len):
        break
    if(flg!=1):
        life-=1
    flg=0
    print(res)
    print("You have %d lives left" % (life))

print(res)

if(count == len):
    print("You won")
else:
    print("You lost")

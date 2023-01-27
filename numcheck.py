# check 10 numbers from user

def posneg(n):
    if(n>0):
        print(n," is positive")
    elif(n<0):
        print(n," is negative")
    elif(n==0):
        print("Number is ZERO neither +ve or -ve")

def oddeven(n):
    if(n%2==0):
        print(n," is even")
    else:
        print(n,
              " is odd")
def occ(n,l):
    count = 0
    
    for a in l:
        if(n == a):
            count+=1
            continue
        else:
            continue
    print("number of times ",n," comes = ",count)


listnm = []
for i in range(0,5):
    num = int(input("Enter the integer"))
    listnm.extend([num])
    
for j in listnm:
    posneg(j)
    print("---------------------")
    oddeven(j)
    print("---------------------")
    occ(j,listnm)
    print("*********************")
    print("*********************")

    

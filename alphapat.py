# alphabet pattern
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = int(input("Enter the number of rows : "))
count = 0
for a in range(0,r):
    print('')
    for b in range(0,a):
        if(count>25):
            count = (count%25)-1
        print(s[count],end='')
        count+=1
        

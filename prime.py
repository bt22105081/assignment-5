# print prime numbers for given range

rs = int(input("Enter the range starting"))
re = int(input("Enter the range ending"))
for num in range (rs,re+1):
    if(num ==1):
        continue
    for i in range(2,num):
        if((num%i) == 0):
            break
    
    else:
        print(num)
    

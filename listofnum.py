# print list of numbers in a range and divisible by a number

rs = int(input("Enter the range starting : "))
re = int(input("Enter the range ending : "))
d = int(input("Enter the number to check divisibility : "))

for i in range(rs,re):
    if(i%d ==0):
        print(i)
    else:
        continue


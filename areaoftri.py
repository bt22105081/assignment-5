# calculate area of triangle with heron's formula

a = int(input("Enter the first side "))
b = int(input("Enter the second side "))
c = int(input("Enter the third side "))
if(a+b>c or a+c>b or b+c>a):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("The area of triangle = ",area)
else:
    print("Triangle not possible with the given sides")

    


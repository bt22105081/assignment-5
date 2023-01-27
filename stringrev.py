# reverse a string

s = input("Enter the string : ")
srev = ""

for a in range(len(s)-1,-1,-1):
    srev = srev + s[a]

print("reverse string\n ",srev)

    

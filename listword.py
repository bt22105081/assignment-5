# number of occurences of a word in a list

n = int(input("Enter the number of elements in the list : "))
lis = []
for a in range(0,n):
    ele = input("Enter the word : ")
    lis.extend([ele])
    
giv = input("Enter the word to be checked : ")

count = 0
for b in lis:
    if(giv == b):
        count+=1
print("The number of times ",giv," comes in the list = ",count)
              

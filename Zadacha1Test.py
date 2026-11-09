n=int(input("Enter a whole number: "))
totalNums=0
sumN=0
avr=0.0
if(n<=0):
    print("Invalid amount!")
for i in range (n):
    number=int(input("Enter number: "))
    if(number%3==0):
        totalNums+=1
    else:
        if(number>0):
            sumN+=number
avr=sumN/n
print("Numbers that are divisible by 3: ", totalNums)
if(sumN==0):
    print("There are no positive numbers")
else:
    print("The avrage of the positive numbers is: ", sumN)
    

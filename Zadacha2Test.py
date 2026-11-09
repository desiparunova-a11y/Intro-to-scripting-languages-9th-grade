smallest=0
negCount=0
numCount=0
narastvaniq=0
for i in range(100000):
    number=int(input("Enter number: "))
    numCount+=1
    lastNum=number
    if(number==0):
        print("Nqma danni")
        break
    else:
        if(number<smallest):
            smallest=number
        if(number<0):
            negCount+=1
    if(lastNum>number):
        narastvaniq+=1
percentage=(numCount//negCount)/100
print("The amount of narastwaniq is: ", narastvaniq)
print("The per cent of negative numbers is: ", percentage)
print("The smallest number is: ", smallest)
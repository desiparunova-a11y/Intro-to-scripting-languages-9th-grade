a=int(input("Enter a: "))
b=int(input("Enter b: "))
sumOfDividers=0
izobilniC=0
if (a>b):
    temp=a
    a=b
    b=temp
for i in range(a, b):
    number=i
    temp=number
    for k in range (number):
        if(k!=number):
            if(number%k==0):
                sumOfDividers+=k
    if(temp==sumOfDividers):
        print(temp)
    else:
        print("There are none svirsheni chisla")
        if(sumOfDividers>temp):
            izobilniC+=1
print("The amount of izobilni chisla is: ", izobilniC)
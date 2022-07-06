
print("QUESTION 1 :")
x = int(input("ENTER A NUMBER : "))
y = int(input("ENTER ANOTHER NUMBER : "))
z = int(input("ENTER ANOTHER NUMBER : "))
avg = (x+y+z)/3
print(avg)



print("QUESTION 2 :")
gross_income = int(input("ENTER GROSS INCOME : "))
dependents = int(input("ENTER NUMBER OF DEPENDENTS : "))
taxable_inc = gross_income - 10000 - 3000*dependents
Tax = taxable_inc*0.2
print(Tax)

#ques 3

#taking input of seconds as s
s=int(input("Number of Seconds: "))
#converting the seconds to minutes
minutes= s//60
seconds= s%60
print(minutes, "min", seconds, "sec")


# ques 4
print(str(25 + int('25') + int(25.0)))

import math
#we will use while loop here
for x in range(0,360,15)
     print(x , '--',round(math.sin(x*3.1415/180),4) ,round(math.cos(x*3.1415/180),4),end=" " '\n') 
     x+=15

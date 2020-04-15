"""

# Assignments - 4

Take the age as input from the user and print whether he is a infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen 
"""
age=int(input("Enter age : "))
if(age<1):
    print("infant")
if(1<=age<18):
    print("child")
if(18<=age<60):
    print("adult")
elif(age>=60):
    print("senior citizen")
"""
# Assignments - 1
Name: 
    Adult Body Mass Index Calculator         
Filename:
    bmi_cal.py
Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
    Take the height and weight of the user from input 
Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""   

height=float(input("Enter your height in cm:: "))
weight=float(input("Enter your weight in kg :: "))
BMI= weight/ ((height/100)**2)
print("\nBody mass index is ",BMI)

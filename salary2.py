"""

# Assignments - 6

Name: 
    Clean the Messy salary from list        
Filename:
    salary2.py
Problem Statement:
    salaries = ['$876,001', '$543,903', '$2453,896'] 
    Clean the Messy salaries into integers for Data Processing
    Remove the $
    Remove the ,
    Convert into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We canuse the int() typecast to convert into integer
"""
sal=[]
salaries = ['$876,001', '$543,903', '$2453,896'] 
for x in salaries:
    sal.append(x.replace('$',''))
print(sal)
salaries.clear()
for x in sal:
    item=int(x.replace(',',''))
    salaries.append(item)
print(salaries)

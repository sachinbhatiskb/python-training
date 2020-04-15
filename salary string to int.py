"""
# Assignments - 3
# Clean the Messy salary into integers for Data Processing
salary = '$876,001' 

Hint:
    Remove the $
    Remove the ,
    Convert into integer
"""

salary = '$876,001' 
s1=salary.replace('$','')
list1=s1.split(',')
s=''.join(list1)
sal=int(salary.replace(',', '').replace('$', ''))
print(sal)
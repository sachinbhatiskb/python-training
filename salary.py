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
sal=int(salary.replace(',', '').replace('$', ''))
print(sal)
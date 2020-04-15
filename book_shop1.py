"""

# Day 4
# Assignments - 8
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number    Book Title              Author      Quantity    Price per Item
    34587           Learning Python         Mark Lutz   4           40.95
    98762           Programming Python      Mark Lutz   5           56.80
    77226           Head First Python       Paul Barry  3           32.95
    88112           Einführung in Python3   Bernd Klein 3           24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
    The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
    
    

  Hint: 
    Write a Python program using lambda and map.
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]

"""



orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]
list1=[]
list2=[]
list3=[]
list4=[]
list6=[]

for item in orders:
    list1.append(int(item[0]))
for item in orders:
    for x in item:
        if(type(x)==int):
            list2.append(x)
for item in orders:
    for x in item:
        if(type(x)==float):
            list3.append(x)
list4 = [ list2[i] * list3[i] for i in range (0,len(list2))] 
def listOfTuples(list1, list4): 
    return list(map(lambda x, y:(x,y), list1, list4)) 

for item in list4:
    if item<100:
        item=item+10
    list6.append(item)
    
list5=listOfTuples(list1, list4)
print(list5)
print("\nThe product should be increased by 10 INR if the value of the order is smaller than 100.00 INR.\n")

list7=listOfTuples(list1, list6)
print(list7)
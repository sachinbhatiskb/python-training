#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 07:26:52 2020

@author: sachinbhati
"""


"""

# Day 5

# Assignments - 9

Name: 
    Supermarket      
Filename:
    supermarket.py 
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Sample Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
""" 

from collections import OrderedDict,defaultdict
od = OrderedDict()
m = defaultdict(list)
for i in xrange(input("no.  of  items")):
    k = input("Enter item and price ").split()
    k[0] = ' '.join(k[0:len(k)-1])
    k[1] = int(k[len(k)-1])
    k = k[0:2]
    m[k[0]].append(k[1])
    od[k[0]] = i

for i in od:
    print i,sum(m[i])
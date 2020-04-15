"""
# Assignments - 2
Name: 
    Ride Cost Calculator         
Filename:
    ridecost_cal.py
Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office.
    Take the distance travelled, cost of diesel and Fuel Average from input 
"""
Disel_cost=float(input("Cost of Disel per litre in RS : "))
distance_travelled=float(input("Distance travelled in KM : "))
fuel_average=float(input("vehicle Fuel Average in KM/Litre : "))
ride_cost= distance_travelled*(Disel_cost/fuel_average)
print("\nride cost is ",ride_cost)

hr=int(input("Period of the earth’s rotation in Hours (Integer only)::"))
lat=float(input("Value of Longitude up to 2 place of decimal:: "))
lat=float("%.2f"%lat)
h,m=divmod(hr*lat, 360)
m=(m*60)/360
def calculateAngle(h,  m):
    hour_angle = int(0.5 * (h*60 + m))
    minute_angle = int( 6*m)
    angle = abs(int(hour_angle - minute_angle))
    angle = min(360-angle, angle)
    print(angle)

calculateAngle(h,m)
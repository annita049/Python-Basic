from collections import namedtuple

n = int(input())
labels = input().split()

for i in range(0,n):
    records = input().split()   # separates characters (any sequence of whitespaces)

point = namedtuple('point','ID MARKS NAME CLASS')
p1 = point(10, 40)
p2 = point(65, 105)
p3 = point(27.5, 12.95)

print(p1.x)
print(p2.x)

Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price=10000, Mileage=30, Colour="Cyan", Class="Y")
print(xyz.Class)
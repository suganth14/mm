import math

def fn(x0):
    return abs(math.sin(x0**2)/float(math.sin(5*x0)))

l = 0
r = 1
h = (r-l)/float(100000)
x = l
area = 0

while(x<r):
  x+=h
  area+=(fn(x)*h)

print("Integration value : ",area)


def randomnumber():
  m = 101
  c = 17
  a = 79
  res = [12]

  while len(res)-1!=n:
    si = (a*res[-1]+c)%m
    res.append(si)
  return res

def piEst():
  import random

  pointsInside = 0
  total = 0

  x_low,x_high = -1,1
  y_low,y_high = -1,1
  Radius = 1
  Center = (0,0)

  def isInside(x,y):
      if (x-Center[0])**2 + (y-Center[1])**2 <=Radius:
          return True
      return False

  for i in range(1000000):
      x = random.uniform(x_low,x_high)
      y = random.uniform(y_low,y_high)
      if(isInside(x,y)):
          pointsInside+=1
      total+=1

  print(pointsInside*4.0/(total))
piEst()


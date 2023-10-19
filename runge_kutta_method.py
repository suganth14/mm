import math

def integration_fn(x,y):
  return (-2)*y + pow(x,3) * math.exp(-2 * x)


# print(integration_fn(0,1))

def Runge_Kutta(x,y,h):
  print(" --------- for x = ",x," ------------")
  k1 = integration_fn(x,y)
  print("k1: ",k1)
  k2 = integration_fn((x + h/2), (y + h*k1/2))
  k3 = integration_fn((x + h/2), (y + h*k2/2))
  k4 = integration_fn((x + h), (y + h*k3))

  y1 = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
  return y1

h = 0.1
y = [1]
x = [0.1,0.2]

for i in range(len(x)):
  y_temp = Runge_Kutta(x[0]*i*h,y[-1],h)
  y.append(y_temp)

print(y)


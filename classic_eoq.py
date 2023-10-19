import math

D = 100
K = 100
h = 0.02
L = 12

y_star = (2*K*D/h)**0.5
t0 = y_star/D #cycle length

if(L>t0):
  n = math.floor(L/t0)
  le = L - n*t0
  print("Reorder point thus occurs when inventory model drops to : ",le*D)
else:
  print("Reorder point thus occurs when inventory model drops to : ",L*D)

TCU_y = K*D/y_star + h*y_star/2
print("Inventory cost associated with the proposed policy is : ",TCU_y)
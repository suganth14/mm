import heapq

def col_min(col,cost_mat):
  heap_arr = []
  for i in range(len(cost_mat)):
    heapq.heappush(heap_arr,(cost_mat[i][col],i))
  return heap_arr

def transportation():
  cost_mat = [[float('inf') for i in range(len(regular) + 1)] for j in range(2*len(regular))]

  j = 0
  for i in range(len(cost_mat)):
    j = i//2
    k = 0
    while j<len(cost_mat[0]):
      if(j==len(cost_mat[0])-1):
        cost_mat[i][-1] = 0
        break
      if(i%2==0):
        cost_mat[i][j] = reg_cost + k*holding_cost
      else:
        cost_mat[i][j] = overtime_cost + k*holding_cost
      j+=1
      k+=1

  for cost in cost_mat:
    print(cost)
  print()

  demand_mat = [[0 for i in range(len(cost_mat[0]))] for j in range(len(cost_mat))]
  for i in range(len(demand)):
    col_min_arr = col_min(i,cost_mat)
    while(demand[i]>0):
      curr_min = heapq.heappop(col_min_arr)
      min_index = curr_min[1]
      row_sum = sum([val for val in demand_mat[min_index] if val>=0])
      if min_index%2==0:
        avail = regular[min_index//2] - row_sum
        ans = min(avail,demand[i])
        demand[i]-=ans
        demand_mat[min_index][i] = ans
      else:
        avail = overtime[min_index//2] - row_sum
        ans = min(avail,demand[i])
        demand[i]-=ans
        demand_mat[min_index][i] = ans

  demand_mat[-1][-1] = cumulative_supply - cumulative_demand
  for row in demand_mat:
    print(row)


regular = [90,100,120,110]
overtime = [50,60,80,70]
demand = [100,190,210,160]
reg_cost = 6
overtime_cost = 9
holding_cost = 0.1

isPossible = True
cumulative_supply = 0
cumulative_demand = 0

for i in range(len(regular)):
  cumulative_supply += regular[i] + overtime[i]
  cumulative_demand += demand[i]
  isPossible = isPossible and cumulative_supply>=cumulative_demand

if(not isPossible):
  print("Not Possible")
else:
  transportation()
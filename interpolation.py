#  Forward Interpolation
def u_cal(u, n):
	temp = u;
	for i in range(1, n):
		temp = temp * (u - i);
	return temp;

def fact(n):
	f = 1;
	for i in range(2, n + 1):
		f *= i;
	return f;

n = 4;
x = [ 45, 50, 55, 60 ];

y = [[0 for i in range(n)]
		for j in range(n)];
y[0][0] = 0.7071;
y[1][0] = 0.7660;
y[2][0] = 0.8192;
y[3][0] = 0.8660;

for i in range(1, n):
	for j in range(n - i):
		y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

value = 52;

sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1,n):
	sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,"is", round(sum, 6));

#  Backward Interpolation
def u_cal_b(u, n):
    temp = u
    for i in range(n):
        temp = temp * (u + i)
    return temp

n = 5
x = [1891, 1901, 1911, 1921, 1931]
y = [[0.0 for _ in range(n)] for __ in range(n)]
y[0][0] = 46
y[1][0] = 66
y[2][0] = 81
y[3][0] = 93
y[4][0] = 101

for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

value = 1925
sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
    sum = sum + (u_cal_b(u, i) * y[n - 1][i]) / fact(i)

print("\n Value at", value,  "is", sum)

# linear interpolation
import pandas as pd
def interpolate(coalDf):
  df = coalDf.copy()
  df['Date'] = pd.to_datetime(df['Date'])
  df = df.set_index('Date').resample('D')
  df = df.re
  df.interpolate(method='linear')
  fig = go.Figure(data=[go.Scatter(x = df['Date'], y = coalDf['High']),go.Scatter(x = df['Date'], y = df['High'])])
  fig.show()

# interpolate(coalDf)
df = coalDf.copy()
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date').resample('D')
# df = df.re
# df.interpolate(method='linear')
print(df)
# fig = go.Figure(data=[go.Scatter(x = df['Date'], y = coalDf['High']),go.Scatter(x = df['Date'], y = df['High'])])
# fig.show()


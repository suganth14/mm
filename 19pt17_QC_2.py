txt1 = "ACAGTCGAACGGTTTCCACA"
txt2 = "ACCGTCCGCTTCGCCTAAGG"

MATCH = 1
MISMATCH = -1
GAP = -2

mat = [[float('-inf') for i in range(len(txt1) + 1)] for j in range(len(txt2) + 1)]

mat[0][0] = 0
for i in range(1,len(mat[0])):
  mat[0][i] = mat[0][i-1] + GAP
for i in range(1,len(mat)):
  mat[i][0] = mat[i-1][0] + GAP

for i in range(1,len(mat)):
  for j in range(1,len(mat[0])):
    if(txt1[j-1]==txt2[i-1]):
      mat[i][j] = max(mat[i-1][j-1] + MATCH, mat[i-1][j] + GAP ,mat[i][j-1] + GAP)
    else:
      mat[i][j] = max(mat[i-1][j-1] + MISMATCH, mat[i-1][j] + GAP ,mat[i][j-1] + GAP)

for ele in mat:
  print(ele)

ans_1 = ""
ans_2 = ""
i = len(mat)-1   
j = len(mat[0])-1 

while(i!=0 or j!=0):
  if(txt1[j-1]==txt2[i-1]):
    ans_2+=txt2[i-1]
    ans_1+=txt1[j-1]
    j-=1
    i-=1
  elif(mat[i][j-1]>mat[i-1][j]):
    ans_2+="-"
    ans_1+=txt1[j-1]
    j-=1
  else:
    ans_2+=txt2[i-1]
    ans_1+="-"
    i-=1
print(ans_1[::-1])
print(ans_2[::-1])
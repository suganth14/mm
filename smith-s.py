txt1 = "ATGCT"
txt2 = "AGCT"

MATCH = 1
MISMATCH = -1
GAP = -2
max_val = -1
max_ind = None

mat = [[0 for i in range(len(txt1) + 1)] for j in range(len(txt2) + 1)]

for i in range(1,len(mat)):
  for j in range(1,len(mat[0])):
    if(txt1[j-1]==txt2[i-1]):
      mat[i][j] = max(mat[i-1][j-1] + MATCH, mat[i-1][j] + GAP ,mat[i][j-1] + GAP)
    else:
      mat[i][j] = max(mat[i-1][j-1] + MISMATCH, mat[i-1][j] + GAP ,mat[i][j-1] + GAP)
    mat[i][j] = max(mat[i][j],0)
    if(mat[i][j]>max_val):
      max_val = mat[i][j]
      max_ind = i

print(txt2[max_ind-max_val:max_ind])
import numpy as np
def maxIndex(list2d):
  flatList = [el for row in list2d for el in row]
  print(flatList)
  maxIndex = flatList.index(max(flatList))

  print(maxIndex)

  rowNo = int(maxIndex/len(list2d[0]))
  colNo = maxIndex%len(list2d[0])

  return rowNo, colNo

def smithWaterman(seq1: str, seq2: str, matchScore: int, misMatch: int, gapScore: int):

  l1, l2 = len(seq1), len(seq2)

  arr = [[0 for i in range(l2+1)] for j in range(l1+1)]
  for j in range(l2+1):
    arr[0][j] = gapScore * (j)
  for i in range(l1+1):
    arr[i][0] = gapScore * (i)

  for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
      arr[i][j] = max([
          arr[i-1][j] + gapScore,
          arr[i][j-1] + gapScore,
          arr[i-1][j-1] + (matchScore if seq1[i-1] == seq2[j-1] else misMatch),
          0
        ])

  print('Matrix: \n', np.matrix(arr))

  path, trace = [], []
  modSeq1, modSeq2 = '', ''

  i, j = maxIndex(arr)

  while arr[i][j] != 0:
    path.append(arr[i][j])

    if seq1[i-1] == seq2[j-1]:
      # match
      i -= 1
      j -= 1
      modSeq1 += seq1[i]
      modSeq2 += seq2[j]
      trace.append('M')
    else:
      # choose max neighbour
      left = arr[i][j-1]
      top = arr[i-1][j]
      diag = arr[i-1][j-1]

      if left > top and left > diag:
        j -= 1
        modSeq1 += '-'
        modSeq2 += seq2[j]
        trace.append('<')

      elif top > left and top > diag:
        i -= 1
        modSeq1 += seq1[i]
        modSeq2 += '-'
        trace.append('^')

      else:
          i -= 1
          j -= 1
          modSeq1 += seq1[i]
          modSeq2 += seq2[j]
          trace.append('M')

  print(f'Retrace scores: {path[::-1]}')

  return modSeq1[::-1], modSeq2[::-1]

if __name__ == '__main__':
  str1 = 'AGCT'
  str2 = 'ATGCT'

  matchScore = 1
  misMatchScore = -1
  gapPenalty = -2

  s1, s2 = smithWaterman(str1, str2, matchScore, misMatchScore, gapPenalty)
  print(f'\nSmith Waterman: {s1} & {s2}')
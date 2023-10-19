import numpy as np

def needlemanWunsch(seq1: str, seq2: str, matchScore: int, misMatch: int, gapScore: int):

  l1, l2 = len(seq1), len(seq2)

  # Empty array => l1 * l2
  arr = [[0 for i in range(l2+1)] for j in range(l1+1)]
  # First row
  for j in range(l2+1):
    arr[0][j] = gapScore * (j)
  # First col
  for i in range(l1+1):
    arr[i][0] = gapScore * (i)

  # Matrix construction
  for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
      arr[i][j] = max([
          arr[i-1][j] + gapScore,
          arr[i][j-1] + gapScore,
          arr[i-1][j-1] + (matchScore if seq1[i-1] == seq2[j-1] else misMatch)
        ])

  print('Matrix: \n', np.matrix(arr))

  # Traceback
  path, trace = [], []
  modSeq1, modSeq2 = '', ''
  i, j = l1, l2

  while i>0 and j>0:
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

  while i>0:
    i -= 1
    trace.append('^')
    modSeq1.append(seq1[i])
    path.append(arr[i][0])

  while j>0:
    j -= 1
    trace.append('<')
    modSeq2.append(seq2[j])
    path.append(arr[0][j])

  print(f'Retrace scores: {path[::-1]}')
  print(f'Retrace chages: {trace[::-1]}\n')

  return modSeq1[::-1], modSeq2[::-1]

if __name__ == '__main__':
  str1 = 'AGCT'
  str2 = 'ATGCT'

  matchScore = 1
  misMatchScore = -1
  gapPenalty = -2

  s1, s2 = needlemanWunsch(str1, str2, matchScore, misMatchScore, gapPenalty)
  print(f'Needleman Wunsch: {s1} & {s2}')
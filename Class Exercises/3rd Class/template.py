'''
  Functions
'''

def mean(l):
  total=0
  for i in l:
    total += i
  return (float(total) / len(l))


def median(l):
    new = sorted(l)
    if (len(l)%2 != 0):
        return float(new[(int(len(new)/2))])
    else:
        return float(new[int(len(new)/2)]+new[int(len(new)/2)+1])


def mode(l):
    counts = dict()
    for value in l:
        counts[value]= counts.get(value, 0) + 1
    bigger = 0
    for i in sorted(counts, key=counts.get):
        if (counts[i]>bigger):
                bigger = counts[i]                
    new = ''
    for i in sorted(counts, key=counts.get):
        if (counts[i]==bigger):
            new += str(i)
    return(''.join(sorted(new)))


def range_(l):
    l.sort()
    dif = l[-1]-l[0]
    return dif


def mat_show(m):
    for list_ in m:
        for elem in list_:
            print(elem, end = " ")
        print()


def mat_sum(m1, m2):
    result = [[int(m1[i][j]) + int(m2[i][j])  for j in range(len(m1[0]))] for i in range(len(m1))] 
    return (result)
            

def mat_sub(m1, m2):
    result = [[int(m1[i][j]) - int(m2[i][j])  for j in range(len(m1[0]))] for i in range(len(m1))] 
    return (result)


def mat_mul(m1, m2):
  result = [[0 for row in range(len(m1))] for col in range(len(m1[0]))]

  for lin in range(len(m1)):
      for c in range(len(m1[0])):
          for ln in range(len(m2)):
              result[lin][c] += int(m1[lin][ln])*int(m2[ln][c])
  return (result)


def determinant(m1):
  ''' https://www.youtube.com/watch?v=3ROzG6n4yMc '''
  if (len(m1) == 1):
    return m1[0][0]
  
  if (len(m1) == 2):
    return (float(m1[0][0])*float(m1[1][1])-(float(m1[0][1])*float(m1[1][0])))
  
  return float(sum([float(m1[0][col]) * float(cofactor(m1, 0, col)) for col in range(len(m1))]))
  

def mat_trans(m1):
  result = [[float(m1[i][j])  for i in range(len(m1[0]))] for j in range(len(m1))] 
  return (result)


def sub_matrix(m1, i, j):
  mat_aux = []
  for lin in range(len(m1)):
    if i == lin:
      continue
    line = []
    for col in range(len(m1[0])):
      if j == col:
        continue
      line.append(m1[lin][col])
    mat_aux.append(line)
  return(mat_aux)


def minor(m1, i, j):
  mat_aux = sub_matrix(m1,i,j)
  return float(determinant(mat_aux))


def cofac_matrix(m1):
  ''' https://www.youtube.com/watch?v=EcI4E15ElK0 '''
  mat_aux = []
  for i in range(len(m1)):
    line = []
    for j in range(len(m1[0])):
      line.append((-1) ** (i + j) * minor(m1,i,j))
    mat_aux.append(line)
  return(mat_aux)


def cofactor(m1, lin, col):
  return ((-1) ** (lin + col) * minor(m1, lin, col))


def adjoint(m1):
  ''' https://www.youtube.com/watch?v=Yi5qzNee7dc '''
  mat_aux = []
  for i in range(len(m1)):
    line = []
    for j in range(len(m1[0])):
      cof = cofactor(m1,i,j)
      if(abs(cof) == 0.0):
        cof = 0.0
      line.append(cof)
    mat_aux.append(line)
  return (mat_trans(mat_aux))


def inverse(m1):
  ''' https://www.youtube.com/watch?v=xfhzwNkMNg4 '''
  
  det = determinant(m1)
  if(det != 0.0):
    mat_aux = []
    adjoint_matrix = adjoint(m1)
    for i in range(len(m1)):
      line = []
      for j in range(len(m1[0])):
        line.append((1/det) * adjoint_matrix[i][j])
      mat_aux.append(line)
    return (mat_aux)
  else:
    print("Inverse does not exist.")
    return None
  

def gaussian(m1):
  mat = [[int(m1[i][j])  for j in range(len(m1[0]))] for i in range(len(m1))] 
  n = len(mat[0])
  res = []

  # Get the upper triangular matrix
  for i in range(min(len(mat), len(mat[0]))):
    # go one column and one row
    for r in range(i, len(mat)):
      # find the row with first number != 0
      zero_row = mat[r][i]
      if (zero_row == 0):
        continue
      # Swap rows: first with the not zero
      mat[i], mat[r] = mat[r], mat[i]
      first_row_first_col = mat[i][i]
      # Zero the first elements
      for rr in range(i + 1, len(mat)):
        row_first = mat[rr][i]
        for cc in range(i, len(mat[0])):
          mat[rr][cc] += mat[i][cc] * (-1 * row_first / first_row_first_col)
      break
  smaller = min(len(mat), len(mat[0]))

  for i in range(smaller-1, -1, -1):
    first_elem_col = -1
    first_elem = -1
    for c in range(len(mat[0])):
      if (mat[i][c] == 0):
        continue
      if (first_elem_col == -1):
        first_elem_col = c
        first_elem = mat[i][c]
      mat[i][c] /= first_elem
    for r in range(i):
      this_row_above = mat[r][first_elem_col]
      scalarMultiple = -1 * this_row_above
      for cc in range(len(mat[0])):
        mat[r][cc] += mat[i][cc] * scalarMultiple
  
  for i in range(len(mat)):
    res.append(float(mat[i][n-1]))
  return (res)


'''
  Main code
'''

# Fist problem: function mean
List=input().split(" ")
Numbers=list()

for elem in List:
  Numbers.append(int(elem))

print("%.1f\n" % (mean(Numbers)))

# Second problem: function median
List=input().split(" ")
Numbers=list()

for elem in List:
  Numbers.append(int(elem))

print("%.1f\n" % (median(Numbers)))

# Third problem: function mode
List=input().split(" ")
Numbers=list()

for elem in List:
  Numbers.append(int(elem))

print("{}\n ".format(mode(Numbers)))

# Fourth problem: function range
List=input().split(" ")
Numbers=list()

for elem in List:
  Numbers.append(int(elem))
print("{}\n".format(range_(Numbers)))


# Fifth problem: function sum of matrices
n = int(input())
m1 = [input().split() for i in range(n)]
m2 = [input().split() for i in range(n)]

mat_show(mat_sum(m1,m2))
print()  

# Sixth problem: function subtraction of matrices
n = int(input())
m1 = [input().split() for i in range(n)]
m2 = [input().split() for i in range(n)]

mat_show(mat_sub(m1,m2))   
print()

# Seventh problem: function multiplication of matrices
n = int(input())
m1 = [input().split() for i in range(n)]
m2 = [input().split() for i in range(n)]

mat_show(mat_mul(m1,m2))   
print()

# Eighth problem: function determinant order 2
m1 = [input().split() for i in range(2)]
print("%.1f\n" % (determinant(m1)))


# Ninth problem: function determinant order 3
m1 = [input().split() for i in range(3)]
print("%.1f\n" % (determinant(m1)))

# Tenth problem: function determinant order 4
m1 = [input().split() for i in range(4)]
print("%.1f\n" % (determinant(m1)))

# Eleventh problem: function transpose of matrix
n = int(input())
m1 = [input().split() for i in range(n)]
mat_show(mat_trans(m1))
print()

# Twelfth problem: function cofactor matrix
n = int(input())
m1 = [input().split() for i in range(n)]
mat_show(cofac_matrix(m1))
print()

# Thirteenth problem: function adjoint matrix
n = int(input())
m1 = [input().split() for i in range(n)]
mat_show(adjoint(m1))
print()

# Fourteenth problem: function inverse matrix
n = int(input())
m1 = [input().split() for i in range(n)]
mat_show(inverse(m1))
print()

# Fifteenth problem: function Linear System
n = int(input())
m1 = [input().split() for i in range(n)]
res = gaussian(m1)
for i in range(n):
  print(round(res[i]), end=' ')
print()


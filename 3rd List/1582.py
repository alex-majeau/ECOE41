from fractions import gcd
from functools import reduce

while True:
  try:
    values = [int(A) for A in (input().split(" "))]
    values.sort()
    summ = values[0]*values[0] + values[1]*values[1]
    if values[2]*values[2] == summ:
      if reduce(gcd, values) == 1:
        print('tripla pitagorica primitiva')
      else:
        print('tripla pitagorica')
    else:
        print('tripla')
  except EOFError:
    break
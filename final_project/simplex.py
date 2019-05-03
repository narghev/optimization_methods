from heapq import nsmallest
import numpy

def column(matrix, i):
   return [row[i] for row in matrix]

def transpose(matrix):
   return numpy.array(matrix).transpose()

def isPivotCol(col):
   return (len([c for c in col if c == 0]) == len(col) - 1) and sum(col) == 1

def variableValueForPivotColumn(tableau, column):
   pivotRow = [i for (i, x) in enumerate(column) if x == 1][0]
   return tableau[pivotRow][-1]

def initialTableau(c, A, b):
   tableau = [row[:] + [x] for row, x in zip(A, b)]
   tableau.append([ci for ci in c] + [0])
   return tableau

def primalSolution(tableau):
   columns = transpose(tableau)
   indices = [j for j, col in enumerate(columns[:-1]) if isPivotCol(col)]
   return [(colIndex, variableValueForPivotColumn(tableau, columns[colIndex]))
            for colIndex in indices]


def objectiveValue(tableau):
   return -(tableau[-1][-1])

def canImprove(tableau):
   lastRow = tableau[-1]
   return any(x > 0 for x in lastRow[:-1])

def moreThanOneMin(L):
   if len(L) <= 1:
      return False

   x,y = nsmallest(2, L, key = lambda x: x[1])
   return x == y


def findPivotIndex(tableau):
   column_choices = [(i,x) for (i,x) in enumerate(tableau[-1][:-1]) if x > 0]
   column = min(column_choices, key = lambda x: x[1])[0]

   # check if unbounded
   if all(row[column] <= 0 for row in tableau):
      raise Exception('Linear problem is unbounded.')

   # check for degeneracy
   quotients = [(i, r[-1] / r[column])
      for i,r in enumerate(tableau[:-1]) if r[column] > 0]

   if moreThanOneMin(quotients):
      raise Exception('Linear problem is degenerate.')

   # pick row index minimizing the quotient
   row = min(quotients, key = lambda x: x[1])[0]

   return row, column

def printTableau(tableau):
   for row in tableau:
      print(row)
   print()

def pivotAbout(tableau, pivot):
   i,j = pivot

   pivotDenom = tableau[i][j]
   tableau[i] = [x / pivotDenom for x in tableau[i]]

   for k, _ in enumerate(tableau):
      if k != i:
         pivotRowMultiple = [y * tableau[k][j] for y in tableau[i]]
         tableau[k] = [x - y for x,y in zip(tableau[k], pivotRowMultiple)]


'''
   simplex: [float], [[float]], [float] -> [float], float
   Solve the given linear program:
      max <c,x>
      s.t. Ax = b
           x >= 0
'''

def simplex(c, A, b):
   tableau = initialTableau(c, A, b)
   print("Initial tableau:")
   printTableau(tableau)

   while canImprove(tableau):
      pivot = findPivotIndex(tableau)
      print("Next pivot index is=%d,%d \n" % pivot)
      pivotAbout(tableau, pivot)
      print("Tableau after pivot:")
      printTableau(tableau)

   return tableau, primalSolution(tableau), objectiveValue(tableau)

def addSlackVariables(A, c):
   constraint_n = len(A)

   # Add slack vars
   for i in range(constraint_n):
      empty_array = [0 for j in range(constraint_n)]
      empty_array[i] = 1
      A[i] += empty_array

   # Add zeros to c
   c += [0 for j in range(constraint_n)]

   return A, c

def solveSimplex(c, A, b):
   slacked_A, slacked_c = addSlackVariables(A, c)
   return simplex(slacked_c, slacked_A, b)


if __name__ == "__main__":
   c = [8, 10, 7]
   A = [[1, 3, 2], [1, 5, 1]]
   b = [10, 8]

   t, s, v = solveSimplex(c, A, b)
   print(s)
   print(v)
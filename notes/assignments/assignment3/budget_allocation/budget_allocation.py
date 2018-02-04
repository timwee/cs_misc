# python3


"""
ILP to SAT
----------------

Inputs
-----------
n - number of inequalities, m - number of variables.

Limits
-----------
−100 ≤ 𝐴𝑖𝑗 ≤100; −1000000 ≤ 𝑏𝑖 ≤ 1000000.

constraints
--------------
1. For each inequality, find all the combinations of non-zero coefficients that will satisfy that inequality, 
	we call that set of combinations C_i (for inequality i), 
	and the set of all combinations of non-zero coefficients as A_i.
	We can encode the ineligible combinations D_i = A_i - C_i similar to the edge constraints in cleaning apartment/hamiltonian path.
	
"""

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print("3 2")
    print("1 2 0")
    print("-1 -2 0")
    print("1 -2 0")

printEquisatisfiableSatFormula()

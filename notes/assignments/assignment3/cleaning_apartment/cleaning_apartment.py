#! /usr/bin/env python

"""
Hamiltonian path to SAT.

We have n vertices, and n positions, we create nxn variables to represent the possibility that vertex i can be in position j.

Possible Constraints to express:
--------------------------
1. Total -	 Every vertex in V maps to at least one position in H.
and_clauses = []
for i in V:
	or_clauses = []
	for j in V:
		or_clauses.append(m_ij)
	and_clauses.append(or_all_clauses(or_clauses))
return and_all_clauses(and_clauses)
--------------------------
2. Onto -	 Every position in H has at least one vertex mapped to it.

Same as total, except i and j are flipped in terms of what to iterate on first.
--------------------------
3. Edge -	 Edge constraints - For each vertex i, the only neighbors that it can have are the vertices that share an edge with vertex i.

for j in xrange(lennodes):
    print j
    for i in gnodes:
        for k in gnodes:
            if i != k and k not in g.neighbors(i):
                exp &= -varz[i][j] | -varz[k][(j+1) % lennodes]


--------------------------
4. Fn -	 	 Every vertex maps to at most one position.

and_over_i(
	and_over_j(
		and_over_k_ne_j(
			(!m_ij | !mik))))

--------------------------
5. 1-1 -	 At most one vertex maps to each position. (apparently expensive)

Same as Fn, except the indexing over the clause is flipped.

and_over_i(
	and_over_j(
		and_over_k_ne_j(
			(!m_ji | !m_ki))))

--------------------------
According to "Formalizing Dangerous SAT Encodings", Total, Onto, and Function clauses together are easy to solve, 
whereas Total, 1-1, and Function clauses together are very hard for solvers to solve efficiently.

All of them together seems to be ok.
"""

import sys

# n, m, edges = get_input()
# n, m = map(int, raw_input().split())
# edges = [ list(map(int, raw_input().split())) for i in range(m) ]





def printEquisatisfiableSatFormula(n, m, edges):





def main():
	with open(sys.argv[1], 'r') as f:
		n, m = map(int, next(f).strip().split())
		edges = [ list(map(int, next(f).split())) for i in range(m) ]

		printEquisatisfiableSatFormula(n, m, edges)

if __name__ == "__main__":
	main()
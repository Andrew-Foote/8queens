import functools as ft
import operator

def solutions(partial_solution=()):
	"""Solves the '8 queens problem', which is to find all the ways in which 8 queens can be
	placed on a chessboard so that none of them threatens another.

	A solution is encoded as an 8-tuple j of integers between 0 and 7, such that for every integer
	i between 0 and 7, the unique queen on row i is at column j[i]. The function is a generator
	which yields all the solutions.

	The partial_solution argument may be any possible prefix of such a tuple; it restricts the
	solutions yielded to those that have that prefix."""

	i = len(partial_solution)

	# If the partial solution is actually a total solution, then that solution is the only one we
	# can return.

	if i == 8:
		yield partial_solution
		return

	# Otherwise, we find all the integers j between 0 and 7 such that the partial solution remains
	# a prefix of a solution after appending j. This gives us all the partial solutions of length
	# i + 1, and we can recurse from there.

	for j in range(8):
		if j in partial_solution:
			# No two queens can be in the same column.
			continue

		threatened_along_left_diagonal = False

		for i_, j_ in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
			if partial_solution[i_] == j_:
				threatened_along_left_diagonal = True
				break

		if threatened_along_left_diagonal:
			continue

		threatened_along_right_diagonal = False

		for i_, j_ in zip(range(i - 1, -1, -1), range(j + 1, 8)):
			if partial_solution[i_] == j_:
				threatened_along_right_diagonal = True
				break
		
		if threatened_along_right_diagonal:
			continue

		yield from solutions(partial_solution + (j,))


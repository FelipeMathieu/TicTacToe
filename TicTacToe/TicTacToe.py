#Tic Tac Toe 
#Name: Felipe Vignoli Mathieu

#Board exemple:
# 0 1 2
# 3 4 5
# 6 7 8

class TicTacToe(object):
							#Horizontal
	winningPossibilities = ([0, 1, 2], [3, 4, 5], [6, 7, 8], 
			'''Vertical'''	[0, 3, 6], [1, 4, 7], [2, 5, 8],
			'''Diagonal'''  [0, 4, 8], [2, 4, 6])
	winner = ('X_venceu', 'Velha', 'O_venceu')

	def __init__(auto, circulos = []):
		
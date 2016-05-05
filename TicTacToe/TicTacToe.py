#Tic Tac Toe 
#Name: Felipe Vignoli Mathieu

#Board exemple:
# 0 1 2
# 3 4 5
# 6 7 8

from random import *

class TicTacToe(object):
							#Horizontal, vertical e diagonal
	winningPossibilities = ([0, 1, 2], [3, 4, 5], [6, 7, 8], 
			                [0, 3, 6], [1, 4, 7], [2, 5, 8],
			                [0, 4, 8], [2, 4, 6])
	winners = ('X_vence', 'Empata', 'O_vence')

	def __init__(auto, squares = []):
		if len(squares) == 0:
			auto.squares = [None for i in range(9)]
		else:
			auto.squares = squares

	def showBoard(auto):
		for e in [auto.squares[i: i + 3] for i in range(0, len(auto.squares), 3)]:
			print(e)

	def availableMovements(auto):
		'''Que parte do tabuleiro está vazia'''
		return [k for k, v in enumerate(auto.squares) if v is None]

	def availablePossibilities(auto):
		'''Quais possibilidades são avaliadas'''
		return auto.availableMovements() + auto.getSquares()

	def complete(auto):
		'''Fim de jogo?'''
		if None not in [v for v in auto.squares]:
			return True
		if auto.winner() != None:
			return True
		
		return False
	
	def X(auto):
		return auto.winner() == 'X'
	
	def O(auto):
		return auto.winner() == 'O'

	def tied(auto):
		return auto.complete() == True and auto.winner() is None

	def winner(auto):
		for player in ('X', 'O'):
			pos = auto.getSquares(player)
			
			for possibilities in auto.winningPossibilities:
				win = True

				for p in possibilities:
					if p not in pos:
						win = False

				if win:
					return player
		return None

	def getSquares(auto, player):
		'''Espaços já do jogador'''
		return [k for k, v in enumerate(auto.squares) if v == player]

	def makeMove(auto, pos, player):
		'''Efetua a jogada'''
		auto.squares[pos] = player

	def alphaBeta(auto, node, player, alpha, beta):
		if node.complete():
			if node.X():
				return -1
			elif node.tied():
				return 0
			elif node.O():
				return 1

		for move in node.availableMovements():
			node.makeMove(move, player)
			val = auto.alphaBeta(node, getEnemy(player), alpha, beta)
			node.makeMove(move, None)
			if player == 'O':
				if val > alpha:
					alpha = val
				if alpha >= beta:
					return beta

			else:
				if val < beta:
					beta = val
				if beta <= alpha:
					return alpha
		
		if player == 'O':
			return alpha
		else:
			return beta
	
def determine(board, player):		
	a = -2
	choices = []
	
	if len(board.availableMovements()) == 9:
		return 4

	for move in board.availableMovements():
		board.makeMove(move, player)
		val = board.alphaBeta(board, getEnemy(player), -2, 2)
		board.makeMove(move, None)

		print("Movimento: " + str(move + 1) + " pois: " + board.winners[val + 1])

		if val > a:
			a = val
			choices = [move]
		elif val == 2:
			choices.append(move)

	return choice(choices)

def getEnemy(player):
	if player == 'X':
		return 'O'
	return 'X'

if __name__  ==  "__main__":
	board = TicTacToe()
	board.showBoard()

	while not board.complete():
		player = 'X'
		playerMove = int(input("Proximo movimento: ")) - 1

		if not playerMove in board.availableMovements():
			continue

		board.makeMove(playerMove, player)
		board.showBoard()

		if board.complete():
			break
		
		player = getEnemy(player)
		pcMove = determine(board, player)
		board.makeMove(pcMove, player)
		board.showBoard()

	print("O vencedor e: ", board.winner())

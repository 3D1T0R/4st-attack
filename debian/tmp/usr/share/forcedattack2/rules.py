from board import *

# Checks if the move is legal
def isMoveLegal(board, selector_pos):
	return len(board.state[selector_pos]) < 6 and selector_pos >= 0

def isBoardFull(board):
	for pos in range(7):
		if len(board.state[pos]) < 6:
			return 0 
	return 1

# Checks if theres a winner
def isWinner(board, player):
	
	# Check vertical wins
	for x in range(7):
		sequence = 0
		for y in range(len(board.state[x])):
			if board.state[x][y] == player:
				sequence += 1
				if sequence == 4:
					# Whe've got a winner!!
					return sequence
			else: sequence = 0
	# Check horizontal wins
	for y in range(6):
		sequence = 0
		for x in range(7):
			# Make sure we wont go out of bounds
			if len(board.state[x]) > y:
				if board.state[x][y] == player:
					sequence += 1
                	                if sequence == 4:
                        	               # Whe've got a winner!!
                                	       return sequence
				else: sequence = 0
			else: sequence = 0

	# Check diagonally - bottom to top
	for height in range(6+1-4):
		for start in range(7+1-4):
			sequence = 0
			for pos in range(7 - start):
				# Make sure we wont go out of bounds
	                        if len(board.state[pos+start]) > (pos + height):
				 	if board.state[pos+start][pos+ height] == player:
						sequence += 1
						if sequence == 4:
							# Whe've got a winner!!
							return sequence
					else: sequence = 0
				else: sequence = 0

	# Check diagonally - top to bottom
	for height in range(6+2-4):
		for start in range(7+1-4):
			sequence = 0
			for pos in range(7-start):
				# Make sure we wont go out of bounds
	                        if (len(board.state[pos+start]) > (6 - pos - height) )  and (6 - pos - height) >=0 :
				 	if board.state[pos+start][6 - pos - height] == player:
						sequence += 1
						if sequence == 4:
							# Whe've got a winner!!
							return sequence
					else: sequence = 0
				else: sequence = 0
	# No win for player
	return 0
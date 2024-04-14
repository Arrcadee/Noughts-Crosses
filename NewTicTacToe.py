import random

board = [[1,2,3],
			[4,5,6],
			[7,8,9]
			]
			
def display_board():
			print()
			for sublist in board:
			 print("+-------+-------+-------+")
			 print("|       |       |       |")
			 print("|",end="   ")
			 for item in sublist:
			 	print(item, "  |",end="   ")
			 print()
			 print("|       |       |       |")
			print("+-------+-------+-------+")			
			

			
available = [1,2,3,4,5,6,7,8,9]

def win_checker():
	if (board[0][0] == board[0][1] and board[0][2] == board[0][1]) == True:
		return True
	elif (board[1][0] == board[1][1] and board[1][2] == board[1][1]) == True:
		return True
	elif (board[2][0] == board[2][1] and board[2][2] == board[2][1]) == True:
		return True
	elif (board[0][0] == board[1][0] and board[2][0] == board[1][0]) == True:
		return True
	elif (board[0][1] == board[1][1] and board[2][1] == board[0][1]) == True:
		return True
	elif (board[0][2] == board[1][2] and board[0][2] == board[2][2]) == True:
		return True
	elif (board[1][1] == board[0][2] and board[2][0] == board[1][1]) == True:
		return True
	elif (board[1][1] == board[0][0] and board[2][2] == board[1][1]) == True:
		return True


def comp_choice():
	print()
	print()
	c_choice = random.choice(available)
	while (c_choice>0 and c_choice<10) and (c_choice in available):
		for i in range(len(board)):
		      		for j in range(len(board[i])):
		      			if board[i][j] == c_choice:
		      				board[i][j] = "X"
		      				available.remove(c_choice)
		      				break
		

def player_choice():
	print()
	p_choice = int(input("Enter your move: "))
	while not ((p_choice >0 and p_choice <10) and (p_choice in available)):
		print("Invalid move try again")
		p_choice = int(input("Enter your move: "))
	else:
			for i in range(len(board)):
				for j in range(len(board[i])):
					if board[i][j] == p_choice:
						board[i][j] = "O"
						available.remove(p_choice)
						break

												
board[1][1] = "X"
available.remove(5)
display_board()
turns = 0
while turns < 4:
	player_choice()
	display_board()
	if win_checker() == True:
		print("Player Wins 👍🏼🔥")
		break
	comp_choice()
	display_board()
	if win_checker() == True:
		print("Player Losses 👎🏿😭")
		break
	turns += 1
else:
	print("It's a Tie 😔😔")
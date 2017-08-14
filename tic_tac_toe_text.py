#A text based game of tic-tac-toe:

import os	#Package required for clearing the output screen

#Initialize the required variables
initialboard = [1,2,3,4,5,6,7,8,9]	#To show the structure of the actual board
actualboard = ['-','-','-','-','-','-','-','-','-']  #An empty board
players = [1,2]	 #To decide the turn of the player
characters = []  #To save corresponding markers
position = []    #To keep track of filled positions	
moves = 0		 #Total number of moves posiible is 9
index = 0		 #To toggle between the players


#A function to display the board:
def displayBoard(board):
	clear = lambda : os.system('cls') 
	clear()	 #Clear the output everytime the board is displayed with new markers
	'''
	Create a pattern like this for the board
			1| 2| 3
		   ---------
		    4| 5| 6
		   ---------
		    7| 8| 9
	'''
	for i in range(9):
		if i%3 == 0 and i!=0:
			print "\n" + "-----------" #Add a new line after every 3rd element
		if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
			print "|" + " " + str(board[i]), #Add a straight line after every 2nd element
		else:
			print " " + str(board[i]),
	print "\n" #Add a new line at the end


#A function to ask the players for their characters/markers:
def askCharacter():
	global characters #Make changes to the global characters list
	char = raw_input("Player 1, please choose your marker from 'X' or 'O': ").upper()
	if char == 'X':
		characters = ['X','O'] #If player 1 chooses an 'X', then player 2 gets an 'O'
	elif char == 'O':
		characters = ['O','X'] #If player 1 chooses an 'O', then player 2 gets an 'X'
	else:
		askCharacter()	#If player 1 enters an invalid marker, ask again


#A function to check for filled positions:
def checkPosition(pos):
	if pos not in position:
		position.append(pos) #If position not already filled, add it to the list of filled position
	else:
		pos = raw_input("The position entered is already filled. Please enter another position: ")
		checkPosition(int(pos)) #Check for filled position after asking again


#A function to set the marker on the board:
def setPosition(position, char):
	actualboard[position-1] = char


#A function to check if a player has won:
def checkWin(board, char):
	#Row checks
	if board[0] == board[1] == board[2] == char:
		return True
	elif board[3] == board[4] == board[5] == char:
		return True
	elif board[6] == board[7] == board[8] == char:
		return True
	#Column checks
	elif board[0] == board[3] == board[6] == char:
		return True
	elif board[1] == board[4] == board[7] == char:
		return True
	elif board[2] == board[5] == board[8] == char:
		return True
	#Diagonal checks
	elif board[0] == board[4] == board[8] == char:
		return True
	elif board[2] == board[4] == board[6] == char:
		return True


#A function to replay the game:
def replay():
	temp = raw_input("Do you want to play again. Type 'yes' or 'no' \n")
	if temp.lower().startswith('y'):
		beginPlay()
	elif temp.lower().startswith('n'):
		print "Thank you for playing!"
	else:
		print "You entered an invalid answer!" #Check until user enters a valid answer
		replay()


#A function to begin the play:
def beginPlay():
	global actualboard
	global position
	global moves
	global index
	#Game begins here:
	displayBoard(initialboard)
	print "Let the game of Tic-Tac-Toe begin."
	askCharacter()
	print "You may choose an integer from 1-9."

	while moves < 9: #The game continues for a maximum of 9 moves or less depending on various conditions
		pos = ' '
		while pos not in '1 2 3 4 5 6 7 8 9'.split(): #To check for valid NUMBER input
			print "Player",players[index], #Print the player number depending on the turn
			pos = raw_input(": ")
		pos = int(pos)
		checkPosition(pos) #Check if the entered position is available or not
		setPosition(position[moves],characters[index]) #Set the marker at the respective position
		displayBoard(actualboard) #Display the current board
		if moves >= 4: #Start checking for wins once the 1st player has entered his/her marker at 3 positions
			if checkWin(actualboard, characters[index]):
				print "Player " + str(players[index]) + " wins!!"
				#Reset the variables for a new game
				actualboard = ['-','-','-','-','-','-','-','-','-']
				position = []
				moves = 0
				index = 0
				break #Break the loop as soon as a player wins
			if moves == 8: #On the last move if no one has won, then the game is a draw
				print "The game is a draw. No player wins."
		index = not index #Toggle the player after each iteration
		moves += 1
	replay() #Ask the player for a re-match

beginPlay() #Begin the play or the program starts execution from here
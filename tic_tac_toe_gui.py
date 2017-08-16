#A GUI based game of tic-tac-toe:

from Tkinter import* #The library required for all the user interfaces

#Initialize the required variables
characters = []		#To save corresponding markers
players = [1,2]		#To decide the turn of the player
index = 0
moves = 1

#A function to set the respective characters/markers of the players:
def getMarker(event):
	global characters
	string = str(event.char)
	if string.upper() == 'X':
		characters = ['X', 'O']
	elif string.upper() == 'O':
		characters = ['O', 'X']

#A function to display the board:
def displayBoard(event):
	label1.destroy()
	ok.destroy()
	player.grid(row=0)
	cell1.grid(row=2, column=2)
	cell2.grid(row=2, column=3)
	cell3.grid(row=2, column=4)
	cell4.grid(row=3, column=2)
	cell5.grid(row=3, column=3)
	cell6.grid(row=3, column=4)
	cell7.grid(row=4, column=2)
	cell8.grid(row=4, column=3)
	cell9.grid(row=4, column=4)

#A function to set the marker on the board:
def setMarker(event):
	global moves
	global index
	event.widget.config(text=characters[index])
	if checkWinner():
		player.destroy()
		announce.config(text="Congratulations, Player "+str(players[index])+" wins the game!")
		announce.pack()			
		root.after(3000,replay)
	else:
		if moves == 9:
			player.destroy()
			announce.config(text="The game is a draw!")
			announce.pack()
			root.after(3000,replay)
		else:
			moves += 1
			index = not index
			player.config(text="Player "+str(players[index]))

#A function to check if a player has won:
def checkWinner():
	#Row checks
	if cell1.cget("text") == cell2.cget("text") == cell3.cget("text") == characters[index]:		
		return True
	elif cell4.cget("text") == cell5.cget("text") == cell6.cget("text") == characters[index]:
		return True
	elif cell7.cget("text") == cell8.cget("text") == cell9.cget("text") == characters[index]:
		return True
	#Column checks
	elif cell1.cget("text") == cell4.cget("text") == cell7.cget("text") == characters[index]:
		return True
	elif cell2.cget("text") == cell5.cget("text") == cell8.cget("text") == characters[index]:
		return True 
	elif cell3.cget("text") == cell6.cget("text") == cell9.cget("text") == characters[index]:
		return True
	#Diagonal checks
	elif cell1.cget("text") == cell5.cget("text") == cell9.cget("text") == characters[index]:
		return True 
	elif cell3.cget("text") == cell5.cget("text") == cell7.cget("text") == characters[index]:
		return True

#A function to replay the game:
def replay():
	cell1.destroy()
	cell2.destroy()
	cell3.destroy()
	cell4.destroy()
	cell5.destroy()
	cell6.destroy()
	cell7.destroy()
	cell8.destroy()
	cell9.destroy()	
	announce.destroy()	
	announce2.pack(side=TOP)	
	yes.bind("<Button-1>", askMarker)
	yes.pack(side=LEFT)	
	no.bind("<Button-1>",endGame)
	no.pack(side=LEFT)

#A function to start the game:
def startGame(event):
	ques1.destroy()
	ans1.destroy()
	submit.destroy()
	label1.grid(row=0, columnspan=15)	
	ok.bind("<Button-1>", displayBoard)
	ok.grid(row=5, column=3)

#A function to end the game:
def endGame(event):
	announce2.destroy()
	yes.destroy()
	no.destroy()
	announce3 = Label(frame,text="Thanks for playing!")
	announce3.pack(side=LEFT)

#A function to ask the players for their characters/markers:
def askMarker(event):
	announce2.destroy()
	yes.destroy()
	no.destroy()
	ques1.grid(row=0, column=0)
	ans1.grid(row=0, column=1)
	submit.grid(row=0, column=2)

#Define a root variable to be the entire window
root = Tk()

#Define a frame which is a small part at the TOP of the entire window
frame = Frame(root)
frame.pack(side=TOP)

#Define the required labels, input fields and buttons to begin the play
ques1 = Label(frame, text="Player 1, please select your marker from 'X' or 'O'", height=2)
ans1 = Entry(frame)
submit = Button(frame, text="Submit", height=2)

ans1.bind("<Key>", getMarker)
submit.bind("<Button-1>", startGame)

#Define the actual board as a 3x3 matrix of buttons
cell1 = Button(frame, text='', height=3, width=5, fg='red')
cell2 = Button(frame, text='', height=3, width=5, fg='red')
cell3 = Button(frame, text='', height=3, width=5, fg='red')
cell4 = Button(frame, text='', height=3, width=5, fg='red')
cell5 = Button(frame, text='', height=3, width=5, fg='red')
cell6 = Button(frame, text='', height=3, width=5, fg='red')
cell7 = Button(frame, text='', height=3, width=5, fg='red')
cell8 = Button(frame, text='', height=3, width=5, fg='red')
cell9 = Button(frame, text='', height=3, width=5, fg='red')

#Clicking on the button results in the desired marker to appear at the clicked position
cell1.bind("<Button-1>", setMarker)
cell2.bind("<Button-1>", setMarker)
cell3.bind("<Button-1>", setMarker)
cell4.bind("<Button-1>", setMarker)
cell5.bind("<Button-1>", setMarker)
cell6.bind("<Button-1>", setMarker)
cell7.bind("<Button-1>", setMarker)
cell8.bind("<Button-1>", setMarker)
cell9.bind("<Button-1>", setMarker)

label1 = Label(frame, text="Let's begin the TIC-TAC-TOE game", height=2)
ok = Button(frame, text="OK", width=3)

#Display the current player
player = Label(frame, text="Player "+str(players[index]))

#Define a blank label to fill in afterwards depending on the result of the game
announce = Label(root, text="")
ok2 = Button(frame, text="OK", width=3)

#Ask the player for a re-match
announce2 = Label(frame, text="Do you want to play again?")
yes = Button(frame, text="Yes")
no = Button(frame, text="No")

#Begin the play or the program starts execution from here
ques1.grid(row=0, column=0)
ans1.grid(row=0, column=1)
submit.grid(row=0, column=2)

root.mainloop() #The program runs or the window displays continuously until it is externally closed
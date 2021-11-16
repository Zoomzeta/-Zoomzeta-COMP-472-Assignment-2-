# -Zoomzeta-COMP-472-Assignment-2-

//PARAMETERS

n-Size of board

b-Number of blocks

s-Winning line-up size

t-Maximum time (If playing with an AI, if it fails to perform an action before the time limit, the AI loses by default)

AI/Human (Program will prompt you to choose whether player 1 and/or player 2 should be a human or an AI

d1 and d2-Depth limit (Not properly built into this program)

a-(Write False for Minimax or True for Alpha-Delta)

//INSTRUCTIONS

The program will start by prompting the user(s) to enter the parameter values requested. 
Once entered, the game initializes and the board is drawn to see. 

Everytime a player's turn starts, Minimax or Alpha-Delta are called to go through the board and 
predict a recommended move to make. Everytime it recursively calls itself, the heuristics values (e1 and e2)
will add +1 to each one, indicating that space was temporarily changed to indicate either a possible space for X or O.
Once either function determines a possible winning line-up, it will return 1 (X wins), -1 (X loses), or 0 (A tie), and 
the recommended move. 

If there are human players, they are prompted to pick coordinates x (Rows 0 to n-1) and y (Columns A to ...). Once picked
the board will be redrawn to indicate the change. AIs automatically make a move based on recommendations.

Evaluation time and Heuristics will be printed for each match, and the average of the former and total of the latter will be displayed
once all games are over, in additions to how many times each player won.

A match ends once no more spaces are available, and the game as a whole ends with match 10.

//Note: Due to unforseen technical circumstances, the game draws any boards of sizes bigger than 3, but is not able to display a predicted move when Minimax
or Alpha-Delta are called (They recursively loop infinitely). Apologies for the inconvenience.


showboard = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]]

#comment.
turn = 'player1'
print "welcome to tictactoe PvP"
print " type what is in these boxes to mark"
print showboard[0]
print showboard[1]
print showboard[2]
p1 =raw_input("who is player 1? you are  x: ")
p2 =raw_input("who is player2 you are o: ")
if p1 == p2:
    print("they cant be the same")
    quit(1)
print("this is your board")
board = [['_','_','_'],['_','_','_'],['_','_','_']]
def drawboard():
    print(board[0])
    print(board[1])
    print(board[2])
drawboard()

def isWon():
    return isrowwin()
    return iscolwin()

#this method will check if there are three same values in a single col
#that will mean the player has won if it is true.
def iscolwin():
    #TODO bigelow matbihjdbdjdbneubdegdhdbqsdgxdcgdgcdcggc c

    for c in range(4):
        for r in range(4):
            success= True
            back = None
            board[r][c]
            if back == None:
                back = r
                break
            elif back != r or back == '_':
                success = False
                break
        if success == True:
            return True
        return success



#this method will check if there are three same values in a single row
#that will mean the player has won if it is true.
def isrowwin():
    #there are two bugs right now:
    # return true is not at the right place. Debug the code and figure out why.
    #. second bug is that it will think that you have won even though you have not played that row.
    success = True
    for r in board:
        prev = None
        for c in r:
            if prev == None:
                prev = c
            elif prev != c or prev == '_':
                success = False
                break
        if success == True:
           return True

    return success



def makeMoveP1():
    print("******************")
    print(p1+"'s turn")
    row = raw_input("Give me row#; it can not be more than 2: ")
    col = raw_input("Give me col#; it can not be more than 2: ")
    if board[int(row)][int(col)] != '_':
        print("dont put your piece on someone elses")
    else:
        board[int(row)][int(col)] = 'x'
        print 'here is your board now'
        drawboard()
def makeMoveP2():
    print("******************")
    print(p2+ "'s turn")
    row = raw_input("Give me row#; it can not be more than 2: ")
    col = raw_input("Give me col#; it can not be more than 2: ")
    if board[int(row)][int(col)] != '_':
        print("dont put your piece on someone elses")
    else:
        board[int(row)][int(col)] = 'o'
        print 'here is your board now'
        drawboard()

def isboardfull():
    if '_' not in board[0] and '_' not in board[1] and '_' not in board[2] :
        return True
    else:
        return False

shouldExitApplication = False
while shouldExitApplication == False:
    makeMoveP1()
    shouldExitApplication = isboardfull() or isWon()
    if shouldExitApplication:
        break
    makeMoveP2()
    shouldExitApplication = isboardfull()  or isWon()


#TODO fix up code to check if someone has won

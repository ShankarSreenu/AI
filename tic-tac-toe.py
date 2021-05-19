##minmax tic-tac-toe
#GAME-PLAY
#X-AI agent
#O-player
#input
# 0<=i,j<=2 enter cell where you want to place your coin

def prettyprint(board):
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],end="  ")
        print("\n")
def winorloose(board):
    flag=1
    for i in range(0,3):
        if '-'  in board[i]:
            flag=0
            
    for a in range(0,3):
        win1=0
        win2=0
        win3=0
        win4=0
        for b in range(0,3):
            if board[a][b]=='O':
                win1=win1+1
            if board[a][b]=='X':
                win2=win2+1
            if board[b][a]=='O':
                win3=win3+1
            if board[b][a]=='X':
                win4=win4+1
        if win2==3 or win4==3:
            ##print('Player X has won\n')
            return 1
        
        if win1==3 or win3==3:
            ##print('Player O has won\n')
            return -1
        
    win5=0
    win6=0
    win7=0
    win8=0
    for i in range(0,3):
        if board[i][i]=='X':
            win5=win5+1
        if board[i][2-i]=='X':
            win6=win6+1
        if board[i][i]=='O':
            win7=win7+1
        if board[i][2-i]=='O':
            win8=win8+1
            
    if win5==3 or win6==3:
        ##print('Player X has won\n')
        return 1
    
    if win7==3 or win8==3:
        ##print('Player O has won\n')
        return -1
            
    if flag==1:
          return 0
        
    
def minmax(board,turn):
    val =winorloose(board)
    if val==1:
        return 10
    if val==-1:
        return -10
    if val==0:
        return 0
    if turn == 1:
        best=-1000
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='-':
                    board[i][j]='X'
                    best=max(best,minmax(board,0))
                    board[i][j]='-'
        return best
        
                    
    if turn == 0:
        best=1000
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='-':
                    board[i][j]='O'
                    best=min(best,minmax(board,1))
                    board[i][j]='-'
                    
        return best
    
    




def nextmove(board):
    bestscore=-1000
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=='-':
                board[i][j]='X'
                score =minmax(board,0)
                board[i][j]='-'
                if bestscore<score:
                    bestscore=score
                    a,b=i,j
    board[a][b]='X'
    

board=[['-','-','-'],['-','X','-'],['-','-','-']]
c=0
print("please enter the corresponding x ,y positions")
print("game has begun")
prettyprint(board)
print("its your turn")
i,j =[int(c) for c in input().split()]
board[i][j]='O'
while True:
        nextmove(board)
        if winorloose(board)==1:
            prettyprint(board)
            print("Agent X has won the game")
            break
        if winorloose(board)==-1:
            prettyprint(board)
            print("O has won the game")
            break
        if winorloose(board)==0:
            prettyprint(board)
            print("Draw game")
            break
        prettyprint(board)
        print("its your turn")
        i,j =[int(c) for c in input().split()]
        print("\n")
        board[i][j]='O'

#3 men morris game
#GAME-PLAY
#X-AI agent
#O-player
#L-LEFT,R-RIGHT,U-UP,D-Down,RD=R+D,LD=L+D,LU=L+U,RU=R+U
#FIRST YOU HAVE TO PLACE ALL PIECES LIKE TIC -TAC-TOE
#NEXT YOU HAVE CAN MOVE BOARD STATES
#INPUT contraints
# 1<=i,j<=3you have to say to computer from which position you are moving your coin(after entering i,j values)
#you have to press in which direction you have to move
def prettyprint(board):
    for j in range(1,4):
        print(board[1][j],end="")
        if j<3:
            print(" __ ",end="")
    print("\n")
    print("| \  |  / |")
    for j in range(1,4):
        print(board[2][j],end="")
        if j<3:
            print(" __ ",end="")
    print("\n")
    print("| /  |  \ |")
    for j in range(1,4):
        print(board[3][j],end="")
        if j<3:
            print(" __ ",end="")
    print("\n")
        
def winorloose(board):      
    for a in range(1,5):
        win1=0
        win2=0
        win3=0
        win4=0
        for b in range(1,5):
            if board[a][b]=='O':
                win1=win1+1
            if board[a][b]=='X':
                win2=win2+1
            if board[b][a]=='O':
                win3=win3+1
            if board[b][a]=='X':
                win4=win4+1
        if win2==3 or win4==3:
            #print('Player X has won\n')
            return 1
        
        if win1==3 or win3==3:
            #print('Player O has won\n')
            return -1
        
    win5=0
    win6=0
    win7=0
    win8=0
    for i in range(1,5):
        if board[i][i]=='X':
            win5=win5+1
        if board[i][4-i]=='X':
            win6=win6+1
        if board[i][i]=='O':
            win7=win7+1
        if board[i][4-i]=='O':
            win8=win8+1
            
    if win5==3 or win6==3:
        #print('Player X has won diagonaly\n')
        return 1
    
    if win7==3 or win8==3:
        #print('Player O has won diagonaly\n')
        return -1
    
def minmax(board,depth,turn):
    if depth==2:
        return 0
    val= winorloose(board)
    
    if val==1:
        return 10
    
    if val==-1:
        return -10
    
    if turn==1:
        best=-1000
        for i in range(1,4):
            for j in range(1,4):
                if board[i][j]=='X':
                    if board[i][j+1]!="#" and board[i][j+1]=='-':
                        board[i][j+1]='X'
                        board[i][j]='-'
                        score=minmax(board,depth+1,0)
                        best=max(best,score)
                        board[i][j]='X'
                        board[i][j+1]='-'

                    if board[i][j-1]!="#" and board[i][j-1]=='-':
                        board[i][j-1]='X'
                        board[i][j]='-'
                        score=minmax(board,depth+1,0)
                        best=max(best,score)
                        board[i][j]='X'
                        board[i][j-1]='-'

                    if board[i+1][j]!="#" and board[i+1][j]=='-':
                        board[i+1][j]='X'
                        board[i][j]='-'
                        score=minmax(board,depth+1,0)
                        best=max(best,score)
                        board[i][j]='X'
                        board[i+1][j]='-'

                    if board[i-1][j]!="#" and board[i-1][j]=='-':
                        board[i-1][j]='X'
                        board[i][j]='-'
                        score=minmax(board,depth+1,0)
                        best=max(best,score)
                        board[i][j]='X'
                        board[i-1][j]='-'
                        
                    if (i!=1 or j!=2) and (i!=2 or j!=1 ) and (i!=2 or j!=3) and (i!=3 or j!=2):
                        if board[i-1][j-1]!="#" and board[i-1][j-1]=='-':
                            board[i-1][j-1]='X'
                            board[i][j]='-'
                            score=minmax(board,depth+1,0)
                            best=max(best,score)
                            board[i][j]='X'
                            board[i-1][j-1]='-'

                        if board[i+1][j+1]!="#" and board[i+1][j+1]=='-':
                            board[i+1][j+1]='X'
                            board[i][j]='-'
                            score=minmax(board,depth+1,0)
                            best=max(best,score)
                            board[i][j]='X'
                            board[i+1][j+1]='-'

                        if board[i-1][j+1]!="#" and board[i-1][j+1]=='-':
                            board[i-1][j+1]='X'
                            board[i][j]='-'
                            score=minmax(board,depth+1,0)
                            best=max(best,score)
                            board[i][j]='X'
                            board[i-1][j+1]='-'

                        if board[i+1][j-1]!="#" and board[i+1][j-1]=='-':
                            board[i+1][j-1]='X'
                            board[i][j]='-'
                            score=minmax(board,depth+1,0)
                            best=max(best,score)
                            board[i][j]='X'
                            board[i+1][j-1]='-'
        return best
                    
    if turn == 0:
        best=1000
        for i in range(1,4):
                for j in range(1,4):
                    if board[i][j]=='O':
                        if board[i][j+1]!="#" and board[i][j+1]=='-':
                            board[i][j+1]='O'
                            board[i][j]='-'
                            score=minmax(board,depth+1,1)
                            best=min(best,score)
                            board[i][j]='O'
                            board[i][j+1]='-'

                        if board[i][j-1]!="#" and board[i][j-1]=='-':
                            board[i][j-1]='O'
                            board[i][j]='-'
                            score=minmax(board,depth+1,1)
                            best=min(best,score)
                            board[i][j]='O'
                            board[i][j-1]='-'

                        if board[i+1][j]!="#" and board[i+1][j]=='-':
                            board[i+1][j]='O'
                            board[i][j]='-'
                            score=minmax(board,depth+1,1)
                            best=min(best,score)
                            board[i][j]='O'
                            board[i+1][j]='-'

                        if board[i-1][j]!="#" and board[i-1][j]=='-':
                            board[i-1][j]='O'
                            board[i][j]='-'
                            score=minmax(board,depth+1,1)
                            best=min(best,score)
                            board[i][j]='O'
                            board[i-1][j]='-'
                            
                        if (i!=1 or j!=2) and (i!=2 or j!=1 ) and (i!=2 or j!=3) and (i!=3 or j!=2):
                            if board[i-1][j-1]!="#" and board[i-1][j-1]=='-':
                                board[i-1][j-1]='O'
                                board[i][j]='-'
                                score=minmax(board,depth+1,1)
                                best=min(best,score)
                                board[i][j]='O'
                                board[i-1][j-1]='-'

                            if board[i+1][j+1]!="#" and board[i+1][j+1]=='-':
                                board[i+1][j+1]='O'
                                board[i][j]='-'
                                score=minmax(board,depth+1,1)
                                best=min(best,score)
                                board[i][j]='O'
                                board[i+1][j+1]='-'

                            if board[i-1][j+1]!="#" and board[i-1][j+1]=='-':
                                board[i-1][j+1]='O'
                                board[i][j]='-'
                                score=minmax(board,depth+1,1)
                                best=min(best,score)
                                board[i][j]='O'
                                board[i-1][j+1]='-'

                            if board[i+1][j-1]!="#" and board[i+1][j-1]=='-':
                                board[i+1][j-1]='O'
                                board[i][j]='-'
                                score=minmax(board,depth+1,1)
                                best=min(best,score)
                                board[i][j]='O'
                                board[i+1][j-1]='-'
        return best
    
def nextmove(board):
    bestscore=-100000
    score=-100000
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j]=='X':
                    if board[i][j+1]!="#" and board[i][j+1]=='-':
                        board[i][j+1]='X'
                        board[i][j]='-'
                        score=minmax(board,0,0)
                        board[i][j]='X'
                        board[i][j+1]='-'
                        t=i
                        s=j+1
                        


                    if board[i][j-1]!="#" and board[i][j-1]=='-':
                        board[i][j-1]='X'
                        board[i][j]='-'
                        score=minmax(board,0,0)
                        board[i][j]='X'
                        board[i][j-1]='-'
                        t=i
                        s=j-1
                        

                    if board[i+1][j]!="#" and board[i+1][j]=='-':
                        board[i+1][j]='X'
                        board[i][j]='-'
                        score=minmax(board,0,0)
                        board[i][j]='X'
                        board[i+1][j]='-'
                        t=i+1
                        s=j
                        
            
                        

                    if board[i-1][j]!="#" and board[i-1][j]=='-':
                        board[i-1][j]='X'
                        board[i][j]='-'
                        score=minmax(board,0,0)
                        board[i][j]='X'
                        board[i-1][j]='-'
                        t=i-1
                        s=j
                        
                    if (i!=1 or j!=2) and (i!=2 or j!=1 ) and (i!=2 or j!=3) and (i!=3 or j!=2):
                        if board[i-1][j-1]!="#" and board[i-1][j-1]=='-':
                            board[i-1][j-1]='X'
                            board[i][j]='-'
                            score=minmax(board,0,0)
                            board[i][j]='X'
                            board[i-1][j-1]='-'
                            t=i-1
                            s=j-1
                            

                        if board[i+1][j+1]!="#" and board[i+1][j+1]=='-':
                            board[i+1][j+1]='X'
                            board[i][j]='-'
                            score=minmax(board,0,0)
                            board[i][j]='X'
                            board[i+1][j+1]='-'
                            t=i+1
                            s=j+1
                            
                            

                        if board[i-1][j+1]!="#" and board[i-1][j+1]=='-':
                            board[i-1][j+1]='X'
                            board[i][j]='-'
                            score=minmax(board,0,0)
                            board[i][j]='X'
                            board[i-1][j+1]='-'
                            t=i-1
                            s=j+1
                            
                           
                            

                        if board[i+1][j-1]!="#" and board[i+1][j-1]=='-':
                            board[i+1][j-1]='X'
                            board[i][j]='-'
                            score=minmax(board,0,0)
                            board[i][j]='X'
                            board[i+1][j-1]='-'
                            t=i+1
                            s=j-1
                            
                            
                    if bestscore<score:
                        bestscore=score
                        x,y=i,j
                        a,b=t,s
                        
    board[x][y]='-'
    board[a][b]='X'
    
def minmax1(board,turn):
    val =winorloose(board)
    if val==1:
        return 10
    if val==-1:
        return -10
    if val==0:
        return 0
    if turn == 1:
        best=-1000
        for i in range(1,4):
            for j in range(1,4):
                if board[i][j]=='-':
                    board[i][j]='X'
                    best=max(best,minmax1(board,0))
                    board[i][j]='-'
        return best
        
                    
    if turn == 0:
        best=1000
        for i in range(1,4):
            for j in range(1,4):
                if board[i][j]=='-':
                    board[i][j]='O'
                    best=min(best,minmax1(board,1))
                    board[i][j]='-'
                    
        return best

def nextmove1(board):
    bestscore=-1000
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j]=='-':
                board[i][j]='X'
                score =minmax1(board,0)
                board[i][j]='-'
                if bestscore<score:
                    bestscore=score
                    a,b=i,j
    board[a][b]='X'
    
                
board=[['#','#','#','#','#'],
       ['#','-','-','-','#'],
       ['#','-','-','-','#'],
       ['#','-','-','-','#'],
       ['#','#','#','#','#']]
c=0
nextmove1(board)
prettyprint(board)
i,j =[int(c) for c in input().split()]
board[i][j]='O'
while c<=1:
        nextmove1(board)
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
        i,j =[int(c) for c in input().split()]
        board[i][j]='O'
        c=c+1

prettyprint(board)
print("now you can move")

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
    print("AI player has moved now your turn")
    print("enter postion of which coin to move")
    i,j=[int(c) for c in input().split()]
    print("choose your valid direction")
    S=input()
    if S=='U':
        board[i-1][j]='O'
        board[i][j]='-'
        prettyprint(board)

    if S=='D':
        board[i+1][j]='O'
        board[i][j]='-'
        prettyprint(board)
    
    if S=='L':
        board[i][j-1]='O'
        board[i][j]='-'
        prettyprint(board)

    if S=='R':
        board[i][j+1]='O'
        board[i][j]='-'
        prettyprint(board)
    
    if S=='RD':
        board[i+1][j+1]='O'
        board[i][j]='-'
        prettyprint(board)

    if S=='LD':
        board[i+1][j-1]='O'
        board[i][j]='-'
        prettyprint(board)

    if S=='LU':
        board[i-1][j-1]='O'
        board[i][j]='-'
        prettyprint(board)
    
    if S=='RU':
        board[i-1][j+1]='O'
        board[i][j]='-'
        prettyprint(board)
    

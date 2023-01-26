import random
def check(board,sign):
    if((board[0][0]==sign and board[0][1]==sign and board[0][2]==sign)or(board[0][0]==sign and board[1][0]==sign and board[2][0]==sign) or (board[0][0]==sign and board[1][1]==sign and board[2][2]==sign)or(board[1][0]==sign and board[1][1]==sign and board[1][2]==sign)or(board[2][0]==sign and board[2][1]==sign and board[2][2]==sign)or(board[2][0]==sign and board[1][1]==sign and board[0][2]==sign)or(board[2][1]==sign and board[1][1]==sign and board[0][1]==sign)or(board[2][2]==sign and board[1][2]==sign and board[0][2]==sign)):
        return 1
    else:
        return 0

def moveComp(board,csign,usign):
    #computer's advantage
    for i in range(3):
        if((board[i][0]==csign and board[i][1]==csign and board[i][2]==0)or(board[i][0]==csign and board[i][1]==0 and board[i][2]==csign)or(board[i][0]==0 and board[i][1]==csign and board[i][2]==csign)):
            if(board[i][2]==0):
                board[i][2]=csign
            elif(board[i][1]==0):
                board[i][1]=csign
            else:
                board[i][0]=csign
            return board
        if((board[0][i]==csign and board[1][i]==csign and board[2][i]==0)or(board[0][i]==csign and board[1][i]==0 and board[2][i]==csign)or(board[0][i]==0 and board[1][i]==csign and board[2][i]==csign)):
            if(board[2][i]==0):
                board[2][i]=csign
            elif(board[1][i]==0):
                board[1][i]=csign
            else:
                board[0][i]=csign
            return board
    if(board[0][0]==csign and board[1][1]==csign and board[2][2]==0):
        board[2][2]=csign
        return board
    if(board[1][1]==csign and board[2][2]==csign and board[0][0]==0):
        board[0][0]=csign
        return board
    if(board[0][2]==csign and board[1][1]==csign and board[2][0]==0):
        board[2][0]=csign
        return board
    if(board[0][2]==0 and board[1][1]==csign and board[2][0]==csign):
        board[0][2]=csign
        return board
    #user's advantage
    for i in range(3):
        if((board[i][0]==usign and board[i][1]==usign and board[i][2]==0)or(board[i][0]==usign and board[i][1]==0 and board[i][2]==usign)or(board[i][0]==0 and board[i][1]==usign and board[i][2]==usign)):
            if(board[i][2]==0):
                board[i][2]=csign
            elif(board[i][1]==0):
                board[i][1]=csign
            else:
                board[i][0]=csign
            return board
        if((board[0][i]==usign and board[1][i]==usign and board[2][i]==0)or(board[0][i]==usign and board[1][i]==0 and board[2][i]==usign)or(board[0][i]==0 and board[1][i]==usign and board[2][i]==usign)):
            if(board[2][i]==0):
                board[2][i]=csign
            elif(board[1][i]==0):
                board[1][i]=csign
            else:
                board[0][i]=csign
            return board
    if(board[0][0]==usign and board[1][1]==usign and board[2][2]==0):
        board[2][2]=csign
        return board
    if(board[1][1]==usign and board[2][2]==usign and board[0][0]==0):
        board[0][0]=csign
        return board
    if(board[0][2]==usign and board[1][1]==usign and board[2][0]==0):
        board[2][0]=csign
        return board
    if(board[0][2]==0 and board[1][1]==usign and board[2][0]==usign):
        board[0][2]=csign
        return board
    
    while(True):
        n=random.randint(0,2)
        m=random.randint(0,2)
        if(board[n][m]==0):
            board[n][m]=csign
            return board


def displayBoard(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==0):
                print(" ",end="")
            else:
                print(board[i][j],end="")
            if(j != 2):
                print("|",end="")
        if(i != 2):
            print("\n_ _ _")

board=[[0,0,0],[0,0,0],[0,0,0]]
usign=input("Enter what sign you would like to pick: X(go 1st) or O(go 2nd): ")
csign=""
wcounter=0
c=0
match usign:
    case "X": csign="O"
    case "O": csign="X"
displayBoard(board)
if(usign=="X"):
    while(c<=9):
        print("\nUser's move:")
        n=int(input("Enter the cell index : "))
        m=int(input("Enter the cell index : "))
        if(board[n][m]=="X" or board[n][m]=="O"):
            print("Cell not empty re-enter")
            continue
        board[n][m]=usign
        c+=1
        wcounter=check(board,usign)
        displayBoard(board)
        if(wcounter!=0):
            print("User wins")
            break
        if(c==9):
            break
        print("\nCPU's move:")
        board=moveComp(board,csign,usign)
        c+=1
        wcounter=check(board,csign)
        displayBoard(board)
        if(wcounter!=0):
            print("CPU wins")
            break
else:
    while(c<=9):
        print("\nCPU's move:")
        board=moveComp(board,csign,usign)
        c+=1
        wcounter=check(board,csign)
        displayBoard(board)
        if(wcounter!=0):
            print("CPU wins")
            break
        if(c==9):
            break
        print("\nUser's move:")
        n=int(input("Enter the cell index : "))
        m=int(input("Enter the cell index : "))
        if(board[n][m]=="X" or board[n][m]=="O"):
            print("Cell not empty re-enter")
            continue
        board[n][m]=usign
        c+=1
        wcounter=check(board,usign)
        displayBoard(board)
        if(wcounter!=0):
            print("User wins")
            break
if(wcounter==0):
    print("\nMatch Draw")
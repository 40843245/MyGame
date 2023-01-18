"""
Chomp Variant 
Nickname:
JSDChomp
Rule:
With 2 players.
Given n1*n2 board.
Given m poisoned blocks p={(x1,y1),...,(xm,ym)}
You must eat blocks consecutively with your given direction 
until there are NO blocks to eat in each your turn.
To compensate for player 2,
player 2 can determine to eat extra block or not after one eats the blocks at first round.
"""

def PrintPlayer(currPlayer):
    print(str(currPlayer)+"'s turn.")

def Inputs(upBound,lowerBound,name):
    needRestart=True
    while needRestart==True:
        num=int(input("number of "+str(name)+":"))
        needRestart=False
        
        if num<lowerBound:
            needRestart=True
            print("The number of "+str(name)+" must be >= lowerBound.")
        
        if num>=upBound:
            needRestart=True
            print("Too many "+str(name)+" you entered.")
    return num 

def CheckOutOfRange(starter,ender,lowerBound,upperBound):
    if not(lowerBound<starter and ender<=upperBound):
        return True
    return False

def IsRepeatXY(src,tarList):
    (srcX,srcY)=src
    for idx in range(0,len(tarList),1):
        tar=tarList[idx]
        (tarX,tarY)=tar
        if srcX==tarX and srcY==tarY:
            return True

    return False

def InputNoRepeatXY(poisonBlock,boardRow,boardCol,currIdx):
    needRestart=True
    while needRestart==True:
        x=Inputs(boardRow,0,str(currIdx)+"'s poison point x")
        y=Inputs(boardCol,0,str(currIdx)+"'s poison point y")
        poisonPoint=(x,y)
        isRepeat=IsRepeatXY(poisonPoint,poisonBlock)
        if isRepeat==True:
            needRestart=True
            print("The point (x,y) you just entered repeats to the given points.Try again.")
        else:
            needRestart=False
            poisonBlock.append(poisonPoint)
            
    return poisonBlock

def InputPoisonBlock(upBound,boardRow,boardCol):
    numOfPoisonBlock=Inputs(upBound,1,"poison block")
    poisonBlock=[]
    for idx in range(0,numOfPoisonBlock,1):
        poisonBlock=InputNoRepeatXY(poisonBlock,boardRow,boardCol,idx)
    return poisonBlock

def InputBoardSize(rowUpBound,colUpBound):
    rowSize=Inputs(rowUpBound,8,"board row")
    colSize=Inputs(colUpBound,8,"board col")
    return (rowSize,colSize)

def InputDirection():
    print("Enter a direction to determine the direction to eat blocks./n enter 1:left 2:right 3:up 4:down")
    while True:
        direction=int(input("dir:"))
        if 1<=direction and direction<=4:
            return direction
        print("Error!!! Invalid input for direction.Please try again.")
    
def Input():
    numOfPlayer=2
    boardSize=InputBoardSize(30+1,30+1)
    (boardRow,boardCol)=boardSize
    poisonBlock=InputPoisonBlock(min(4,boardRow*boardCol),boardRow,boardCol)
    return (numOfPlayer,boardSize,poisonBlock)


def EatPosition(boardSize):
    (boardRow,boardCol)=boardSize
    needRestart=True
    while needRestart==True:
        eatX=int(input(""))
        eatY=int(input(""))
        needRestart=False
        if CheckOutOfRange(eatX,eatX,-1,boardRow):
            print("Error Out of range in x!!! Try again")
            needRestart=True
        if CheckOutOfRange(eatY,eatY,-1,boardCol):
            print("Error Out of range in y!!! Try again")
            needRestart=True
    return (eatX,eatY)

def CheckEaten(eatStartPos,availableMatrix):
    (eatStartPosX,eatStartPosY)=eatStartPos
    return (availableMatrix[eatStartPosX][eatStartPosY]==False) ## ensure to return a bool type.

def CheckEatPoison(currPosX,currPosY,poisonBlock):
    for elem in poisonBlock:
        (x,y)=elem
        if currPosX==x and currPosY==y:
            return True
    return False

def EatByDirection(eatStartPos,direction,boardSize,poisonBlock,availableMatrix):
    
    ## Calculate the offset with specified direction.
    offsetX=0
    offsetY=0
    if direction==1:
        offsetX=0
        offsetY=-1
    elif direction==2:
        offsetX=0
        offsetY=1
    elif direction==3:
        offsetX=-1
        offsetY=0
    elif direction==4:
        offsetX=1
        offsetY=0
    
    (boardRow,boardCol)=boardSize
    (eatStartPosX,eatStartPosY)=eatStartPos  
    availableMatrix[eatStartPosX][eatStartPosY]=False
    
    currPosX=eatStartPosX
    currPosY=eatStartPosY
    while True:
        nextPosX=currPosX+offsetX
        nextPosY=currPosY+offsetY
        
        ## Check out of bound while eating.
        if nextPosX<0 or nextPosX>=boardRow:
            return (1,availableMatrix)
        if nextPosY<0 or nextPosY>=boardCol:
            return (2,availableMatrix)
        
        ## Check the block has already been eaten.
        if CheckEaten((nextPosX,nextPosY),availableMatrix):
            return (3,availableMatrix)
        
        availableMatrix[nextPosX][nextPosY]=False
        
        ## Check one eat a poisoned block.
        eatPoisoned=CheckEatPoison(nextPosX, nextPosY, poisonBlock)
        if eatPoisoned==True:
            return (-1,availableMatrix) ## loses the game
        
        ## Update current position
        currPosX=nextPosX
        currPosY=nextPosY

def StartEat(gameInfo):
    (numOfPlayer,boardSize,poisonBlock)=gameInfo
    (boardRow,boardCol)=boardSize
    availableMatrix=[ [True for _ in range(0,boardRow,1)] for _ in range(0,boardCol,1)]
    
    print("availableMatrix=")
    for row in availableMatrix:
        print(row)
    
    isFirstRound=True
    currPlayer=1
    while True:
        print("Eat blocks.Please enter the position(x,y) and direction dir to eat:")
        PrintPlayer(currPlayer)
        needToContinue=True
        while True:
            eatStartPos=EatPosition(boardSize)
            needToContinue=CheckEaten(eatStartPos,availableMatrix)    
            if needToContinue==False:
                break
            print("Error!!! The block has already been eaten.Please try again.")
        direction=InputDirection()
        (gameStatus,availableMatrix)=EatByDirection(eatStartPos,direction,boardSize,poisonBlock,availableMatrix)
        
        print("availableMatrix=")
        for row in availableMatrix:
            print(row)
            
        if gameStatus==-1:
            return (-1,currPlayer) ## currPlayer loses this game.
        
        #Rule:extra eat rule
        if isFirstRound==True and currPlayer==numOfPlayer:
            isFirstRound=False
            c=""
            while True:
                print("Want to eat extra one block? y for yes n for no.")
                c=input("")
                if c=="y":
                    print(str(currPlayer)+"'s player DOES execute the extra eat rule.")
                    print("Which block do you want to eat?")
                    while True:
                        eatStartPos=EatPosition(boardSize)
                        needToContinue=CheckEaten(eatStartPos,availableMatrix)    
                        if needToContinue==False:
                            break
                        print("Error!!! The block has already been eaten.Please try again.")
                    (eatStartPosX,eatStartPosY)=eatStartPos
                    availableMatrix[eatStartPosX][eatStartPosY]=False
                    print(str(currPlayer)+"'s player eat the block at position("+str(eatStartPosX)+","+str(eatStartPosY)+")")
                    
                    eatPoisoned=CheckEatPoison(eatStartPosX, eatStartPosY, poisonBlock)
                    if eatPoisoned==True:
                        return (-1,currPlayer) ## currPlayer loses this game.
                    break
                if c=="n":
                    print(str(currPlayer)+"'s player DON'T execute the extra eat rule.")
                    break
                print("Error!!! Invalid input. The input must be either y or n.Please try again.")
        
        currPlayer=(currPlayer%numOfPlayer)+1 ## change turn.
        
def Play():
    gameInfo=Input()
    (gameStatus,losePlayer)=StartEat(gameInfo)
    if gameStatus==-1:
        print(str(losePlayer)+"'s player loses this game.")
    else: #impossible to happen.
        print("Tie.")

if __name__=='__main__':
    Play()

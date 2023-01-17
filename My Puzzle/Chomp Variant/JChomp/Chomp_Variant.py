"""
Chomp Variant 
Nickname:
JChomp
Rule:
Given n1*n2 board.
Given m poisoned blocks p={(x1,y1),...,(xm,ym)}
You must eat e1*e2 continuous blocks (e1 columns * e2 rows block)once in each your turn.
Assume there are player players.
"""

def PrintPlayer(numOfPlayer,turnedPlayer):
    print(str(turnedPlayer)+"'s player turns.")
    return None

def Inputs(upBound,lowerBound,name):
    needRestart=True
    while needRestart==True:
        numOfPlayer=int(input("number of "+str(name)+":"))
        needRestart=False
        
        if numOfPlayer<lowerBound:
            needRestart=True
            print("The number of "+str(name)+" must be >= lowerBound.")
        
        if numOfPlayer>=upBound:
            needRestart=True
            print("Too many "+str(name)+" you entered.")
    return numOfPlayer 

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

def InputPlayer(upBound,name):
   numOfPlayer=Inputs(upBound,2,name)
   return numOfPlayer

def InputBoardSize(rowUpBound,colUpBound):
    rowSize=Inputs(rowUpBound,4,"board row")
    colSize=Inputs(colUpBound,4,"board col")
    return (rowSize,colSize)

def InputEatSize(rowUpBound,colUpBound):
    rowSize=Inputs(rowUpBound,1,"eat row")
    colSize=Inputs(colUpBound,1,"eat col")
    return (rowSize,colSize)

def InputPoisonBlock(upBound,boardRow,boardCol):
    numOfPoisonBlock=Inputs(upBound,1,"poison block")
    poisonBlock=[]
    for idx in range(0,numOfPoisonBlock,1):
        poisonBlock=InputNoRepeatXY(poisonBlock,boardRow,boardCol,idx)
    return poisonBlock
    
def Input():
    numOfPlayer=InputPlayer(5,"player")
    boardSize=InputBoardSize(15+1,15+1)
    (boardRow,boardCol)=boardSize
    poisonBlock=InputPoisonBlock(min(4,boardRow*boardCol),boardRow,boardCol)
    eatSize=InputEatSize(4,4)
    return (numOfPlayer,boardSize,poisonBlock,eatSize)

def CheckOutOfRange(starter,ender,lowerBound,upperBound):
    if not(lowerBound<starter and ender<=upperBound):
        return True
    return False

def EatPosition(boardSize,eatSize):
    (boardRow,boardCol)=boardSize
    (eatRow,eatCol)=eatSize
    needRestart=True
    while needRestart==True:
        eatX=int(input(""))
        eatY=int(input(""))
        needRestart=False
        if CheckOutOfRange(eatX,eatX+eatRow,-1,boardRow):
            print("Error Out of range in x!!!")
            needRestart=True
        else:
            print("YA!!! NOT out of range in x.")
        if CheckOutOfRange(eatY,eatY+eatCol,-1,boardCol):
            print("Error Out of range in y!!!")
            needRestart=True
        else:
            print("YA!!! NOT out of range in y.")
    return (eatX,eatY)

def CheckEaten(eatStartPos,eatSize,eatenMatrix):
    (eatRow,eatCol)=eatSize
    (eatStartPosX,eatStartPosY)=eatStartPos
    eatEndPosX=eatStartPosX+eatRow-1
    eatEndPosY=eatStartPosY+eatCol-1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("In the func CheckEaten,")
    print("eatStartPosX="+str(eatStartPosX)+",eatEndPosX="+str(eatEndPosX))
    print("eatStartPosY="+str(eatStartPosY)+",eatEndPosY="+str(eatEndPosY))
    
    for currIdx in range(0,len(eatenMatrix),1):
        eatArr=eatenMatrix[currIdx]
        for j in range(0,len(eatArr),1):
            eatenStartPos=eatArr[j]
            (eatenStartPosX,eatenStartPosY)=eatenStartPos
            eatenEndPosX=eatenStartPosX+eatRow-1
            eatenEndPosY=eatenStartPosY+eatCol-1
            print("eatenStartPosX="+str(eatenStartPosX)+",eatenEndPosX="+str(eatenEndPosX))
            print("eatenStartPosY="+str(eatenStartPosY)+",eatenEndPosY="+str(eatenEndPosY))
            OverLapX=(eatenStartPosX<=eatStartPosX and eatStartPosX<=eatenEndPosX ) or ( eatenStartPosX<=eatEndPosX and eatEndPosX<=eatenEndPosX)
            OverLapY=(eatenStartPosY<=eatStartPosY and eatStartPosY<=eatenEndPosY ) or ( eatenStartPosY<=eatEndPosY and eatEndPosY<=eatenEndPosY)
            if OverLapX and OverLapY:
                return True
    return False

def CheckEatPoison(eatPos,eatSize,poisonBlock):
    (eatRow,eatCol)=eatSize
    (eatStartPosX,eatStartPosY)=eatPos
    eatEndPosX=eatStartPosX+eatRow-1
    eatEndPosY=eatStartPosY+eatCol-1
    numOfPoisonBlock=len(poisonBlock)
    
    print("----------------------------------------------------")
    print("In the func CheckEatPoison,")
    print("eatStartPosX="+str(eatStartPosX)+",eatEndPosX="+str(eatEndPosX))
    print("eatStartPosY="+str(eatStartPosY)+",eatEndPosY="+str(eatEndPosY))
    for m in range(0,numOfPoisonBlock,1):
        posionPoint=poisonBlock[m]
        (posionStartPosX,posionStartPosY)=posionPoint
        posionEndPosX=posionStartPosX
        posionEndPosY=posionStartPosY
        
        print("posionStartPosX="+str(posionStartPosX)+",posionEndPosX="+str(posionEndPosX))
        print("posionStartPosY="+str(posionStartPosY)+",posionEndPosY="+str(posionEndPosY))
        
        OverLapX=(posionStartPosX<=eatStartPosX and eatStartPosX<=posionEndPosX) or ( posionStartPosX<=eatEndPosX and eatEndPosX<=posionEndPosX)
        OverLapY=(posionStartPosY<=eatStartPosY and eatStartPosY<=posionEndPosY) or ( posionStartPosY<=eatEndPosY and eatEndPosY<=posionEndPosY)
        
        if OverLapX and OverLapY:
            return True
    
    return False

def CheckTie(availableMatrix,availableCount,eatSize,boardSize):    
    print("________________________________!__________________")
    print("In the func CheckTie,")
    print("availableMatrix")
    for row in availableMatrix:
        print(row)
    print("availableCount="+str(availableCount))
    print("eatSize="+str(eatSize))
    print("boardSize="+str(boardSize))
    
    if availableCount<=0:
        return True
    
    (eatRow,eatCol)=eatSize
    
    if eatRow==1 and eatCol==1:
        return False
    
    #Check Tie by fecth value of availableMatrix
    for row in range(0,len(availableMatrix)-(eatRow-1),1):
        for col in range(0,len(availableMatrix[row])-(eatCol-1),1):
            
            if availableMatrix[row][col]==True:
                #availableMatrix[row][col] is available.
                #Check the next blocks are also available.
                tempStatus=True
                for rowIdx in range(row,row+eatRow-1+1,1):
                    for colIdx in range(col,col+eatCol-1+1,1):
                        tempStatus=availableMatrix[rowIdx][colIdx]
                        if tempStatus==False:
                            break
                    if tempStatus==False:
                        break
                if tempStatus==True:
                    return False
                    
    return True
    
def StartEat(gameInfo):
    (numOfPlayer,boardSize,poisonBlock,eatSize)=gameInfo
    (boardRow,boardCol)=boardSize
    eatenMatrix=[ [] for _ in range(0,numOfPlayer,1)]
    availableMatrix=[ [True for _ in range(0,boardRow,1)] for _ in range(0,boardCol,1)]
    availableCount=boardRow*boardCol
    
    print("eatenMatrix=")
    print(eatenMatrix)
    print("availableMatrix=")
    for row in availableMatrix:
        print(row)
    
    currPlayer=1
    needToContinue=True
    while True:
        
        print("Eat blocks.Please enter the position(x,y) to eat:")
        PrintPlayer(numOfPlayer,currPlayer)
            
        needToContinue=True
        while needToContinue==True:
            eatPos=EatPosition(boardSize,eatSize)
            OverLap=CheckEaten(eatPos,eatSize,eatenMatrix)
            if OverLap:
                needToContinue=True
                print("Error!!! Try to eat blocks which have been already eaten.Try again.")
            else:
                needToContinue=False
                

        eatPoison=CheckEatPoison(eatPos,eatSize,poisonBlock)
        if eatPoison==True:
            print(str(currPlayer)+"'s eats the poison block.")
            needToContinue=False
            return (-1,currPlayer)
        
        currPlayer+=1
        if currPlayer==numOfPlayer+1:
            currPlayer=1
        
        eatenMatrix[currPlayer-1].append(eatPos)
        
        (tempCount,availableMatrix)=UpdateAvailableMatrix(availableMatrix,eatPos,eatSize,boardSize)
        if tempCount>0:
            availableCount-=tempCount
            
        print("eatenMatrix=")
        print(eatenMatrix)
        print("availableMatrix=")
        for row in availableMatrix:
            print(row)
        
        
        if CheckTie(availableMatrix,availableCount,eatSize,boardSize)==True:
            print("CheckTie returns True.")
            needToContinue=False
            return (0,0)
    return (0,0)

def UpdateAvailableMatrix(availableMatrix,eatCenterPos,eatSize,boardSize):
    (eatCenterPosX,eatCenterPosY)=eatCenterPos
    (eatRow,eatCol)=eatSize
    (boardRow,boardCol)=boardSize
    
    eatEndPosX=min(eatCenterPosX+eatRow-1,boardRow-1)
    eatEndPosY=min(eatCenterPosY+eatCol-1,boardCol-1)
    
    eatStartPosX=max(0,eatCenterPosX-eatRow+1)
    eatStartPosY=max(0,eatCenterPosY-eatCol+1)
    
    unavailableCount=0
    for row in range(eatStartPosX,eatEndPosX+1,1):
        for col in range(eatStartPosY,eatEndPosY+1,1):
            if availableMatrix[row][col]==True:
                unavailableCount+=1
                availableMatrix[row][col]=False
    return (unavailableCount,availableMatrix)
    
def Play():
    gameInfo=Input()
    (gameStatus,LosePlayer)=StartEat(gameInfo)
    if gameStatus==0:
        print("Tie.")
    else:
        print(str(LosePlayer)+"'s lose the game.")
    
if __name__=='__main__':
    Play()
   
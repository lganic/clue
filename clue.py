class boardData:
    def __init__(self):
        self.pathBoard=[[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,2,-1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,3,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,-1,4,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,0,1,1,3,3,1,1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,5,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,6,1,1,1,1,1,1],[1,1,5,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1],[1,7,1,1,1,1,0,0,0,1,1,1,1,1,0,0,6,1,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1],[1,1,1,1,1,7,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1,9,1,1,1,1,9,1,0,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,10,1,1,1,1],[1,1,1,1,8,0,0,0,9,1,1,1,1,1,1,9,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1]]
        self.doors=[[(6,3)],[(9,4),(11,6),(12,6)],[(17,5)],[(6,8),(2,10)],[(17,9),(16,12)],[(1,12),(5,15)],[(4,19)],[(8,19),(9,17),(14,17),(15,19)],[(19,18)]]
        self.exits=[[(6,3),(19,18)],[(9,4),(11,6),(12,6)],[(17,5),(4,19)],[(6,8),(2,10)],[(17,9),(16,12)],[(1,12),(5,15)],[(4,19),(17,5)],[(8,19),(9,17),(14,17),(15,19)],[(6,3),(19,18)]]
        self.playerStarts=[(16,0),(23,7),(0,5),(0,18),(9,24),(14,24)]
        self.roomCorners=[(0,0),(9,0),(17,0),(0,6),(16,9),(0,12),(0,19),(8,17),(18,18),(9,8)]
        self.roomNames=["study","hall","lounge","library","dining","billiard","conservatory","ballroom","kitchen","main"]

class cardData:
    def __init__(self):
        self.cardTypes=["player","weapon","room"]
        self.nCards=[6,6,9]
        self.cardNames=[["mrs scarlet","colonel mustard","professor plum","mrs peacock","mr green","mrs white"],["candlestick","revolver","rope","wrench","lead pipe","knife"],["study","hall","lounge","library","dining room","billiard room","conservatory","ballroom","kitchen"]]
    def getNameIndex(self,name):
        #these functions are just to make my life easier
        return self.cardNames[0].index(name)
    def getWeaponIndex(self,weapon):
        return self.cardNames[1].index(weapon)
    def getRoomIndex(self,room):
        return self.cardNames[2].index(room)
    def getCardType(self,str):
        for a in range(3):
            if str in self.cardNames[a]:
                return self.cardTypes[a]
    def genCard(self,str):
        type=self.getCardType(str)
        if type=="player":
            return card(0,self.getNameIndex(str))
        if type=="weapon":
            return card(1,self.getWeaponIndex(str))
        if type=="room":
            return card(2,self.getRoomIndex(str))

class card:
    def __init__(self,cardType,cardIndex):
        c=cardData()
        self.cardType=c.cardTypes[cardType]
        self.cardName=c.cardNames[cardType][cardIndex]
        self.iVals=(cardType,cardIndex)
    def equals(self,cardType,cardIndex):
        c=cardData()
        ct=c.cardTypes[cardType]
        cn=c.cardNames[cardType][cardIndex]
        if ct==self.cardType and cn==self.cardName:
            return True
        return False
    def print(self):
        print(self.cardName)

class game:
    def __init__(self,scarlet=-1,mustard=-1,plum=-1,peacock=-1,green=-1,white=-1):
        global rando
        print("clue game starting...")
        self.nPlayers=(scarlet!=-1)+(mustard!=-1)+(plum!=-1)+(peacock!=-1)+(green!=-1)+(white!=-1)
        print(self.nPlayers,"players")
        c=cardData()
        b=boardData()
        temp=c.cardNames[0]
        nameList=[]
        for a in range(6):
            nameList.append(temp[rando[a]])
        sts=[scarlet!=-1,mustard!=-1,plum!=-1,peacock!=-1,green!=-1,white!=-1]
        self.names=[]
        for a in range(6):
            if sts[a]:
                self.names.append(nameList[a])
        print("list of players:")
        for a in self.names:
            print(a)
        self.playerCords=[]
        for a in self.names:
            self.playerCords.append(b.playerStarts[c.getNameIndex(a)])
        pc=[]
        for player in range(c.nCards[0]):
            pc.append(card(0,player))
        wc=[]
        for weapon in range(c.nCards[1]):
            wc.append(card(1,weapon))
        rc=[]
        for room in range(c.nCards[2]):
            rc.append(card(2,room))
        from random import randint as rand
        self.solution=[]
        self.solution.append(pc.pop(rand(0,c.nCards[0]-1)))
        self.solution.append(wc.pop(rand(0,c.nCards[1]-1)))
        self.solution.append(rc.pop(rand(0,c.nCards[2]-1)))
        deck=[]
        for a in range(len(pc)):
            deck.append(pc[a])
        for a in range(len(wc)):
            deck.append(wc[a])
        for a in range(len(rc)):
            deck.append(rc[a])
        for a in range(len(deck)):
            i=rand(0,len(deck)-1)
            temp=deck[i]
            deck[i]=deck[a]
            deck[a]=temp
        self.hands=[]
        for a in range(self.nPlayers):
            self.hands.append([])
        p=0
        for a in deck:
            self.hands[p].append(a)
            p+=1
            if p==self.nPlayers:
                p=0
        import tileGraphics
        global tileGraphics,graphics,roomsprites,characterSprites,diceSprites
        graphics=tileGraphics.graphics(44,25,fullScreen=True)
        roomsprites=tileGraphics.complexSpriteManager(graphics,"rooms")
        characterSprites=tileGraphics.spriteManager(graphics,"characters",backgroundColor=(0,0,0))
        diceSprites=tileGraphics.complexSpriteManager(graphics,"dice")
        self.solved=False
    def render(self):
        data=boardData()
        graphics.put(0,0,0,width=24,height=25)
        for y in range(25):
            for x in range(24):
                if mapdata.pathBoard[y][x]==1:
                    graphics.put(x,y,7)
        graphics.outline((255,255,255),width=24,height=25)
        for a in range(10):
            graphics.putComplexSprite(data.roomCorners[a][0],data.roomCorners[a][1],roomsprites.get(data.roomNames[a]))
        for a in range(self.nPlayers):
            x, y=self.playerCords[a]
            if mapdata.pathBoard[y][x]<1:
                graphics.putSprite(x,y,characterSprites.get(self.names[a]))
            else:
                ox, oy=mapdata.roomCorners[mapdata.pathBoard[y][x]-2]
                graphics.putSprite(ox+a,oy+1,characterSprites.get(self.names[a]))
    def update(self):
        graphics.update()
    def checkSolution(self,solution):
        if self.solution[0].cardName==solution[0] and self.solution[1].cardName==solution[1] and self.solution[2].cardName==solution[2]:
            print("correct solution!!!")
            self.solved=True
            return True
        return False
    def applyMove(self,move,playerIndex):
        for c in range(len(move[1])):
            cord=move[1][c]
            self.playerCords[playerIndex]=cord
            self.render()
            for d in range(c,len(move[1])-1):
                graphics.line(move[1][d],move[1][d+1],1,width=3)
            self.update()
            checkExit(graphics)
            import time
            #time.sleep(.1)
        if move[0]=="guess":
            if move[2][0] in self.names:
                self.playerCords[self.names.index(move[2][0])]=self.playerCords[playerIndex]
        self.render()
        self.update()
    def getRoom(self,playerIndex):
        m=boardData()
        x, y=self.playerCords[playerIndex]
        b=m.pathBoard[y][x]
        if b>1:
            return b-2
        return -1

def matrix(width,height):
    import copy
    temp=[]
    out=[]
    for a in range(width):
        temp.append(0)
    for a in range(height):
        out.append(copy.copy(temp))
    return copy.deepcopy(out)

def value(lst):
    if 2 in lst:
        return 0
    return sum(lst)

def complexScore(mat,val):
    for a in range(len(mat)):
        if val in mat[a]:
            return a
    return -1

def scramble(lst):
    from random import randint as rand
    for a in range(len(lst)):
        temp=lst[a]
        ind=rand(0,len(lst)-1)
        lst[a]=lst[ind]
        lst[ind]=temp
    return lst

def checkExit(gi):
    if gi.checkKey(27):
        exit()

#holy fuck theres alot of code in this class

class dataBase:
    def __init__(self,nPlayers,myHand,myIndex):
        c=cardData()
        ns=c.nCards
        self.tripleStat=[]
        self.players=matrix(nPlayers,ns[0])
        self.weapons=matrix(nPlayers,ns[1])
        self.rooms=matrix(nPlayers,ns[2])
        for a in range(ns[0]):
            self.players[a][myIndex]=1
        for a in range(ns[1]):
            self.weapons[a][myIndex]=1
        for a in range(ns[2]):
            self.rooms[a][myIndex]=1
        for card in myHand:
            if card.cardType=="player":
                player=c.getNameIndex(card.cardName)
                for a in range(nPlayers):
                    self.players[player][a]=1
                self.players[player][myIndex]=2
            if card.cardType=="weapon":
                weapon=c.getWeaponIndex(card.cardName)
                for a in range(nPlayers):
                    self.weapons[weapon][a]=1
                self.weapons[weapon][myIndex]=2
            if card.cardType=="room":
                room=c.getRoomIndex(card.cardName)
                for a in range(nPlayers):
                    self.rooms[room][a]=1
                self.rooms[room][myIndex]=2
    def addNull(self,playerIndex,guess):
        c=cardData()
        player=c.getNameIndex(guess[0])
        weapon=c.getWeaponIndex(guess[1])
        room=c.getRoomIndex(guess[2])
        self.players[player][playerIndex]=1
        self.weapons[weapon][playerIndex]=1
        self.rooms[room][playerIndex]=1
        self.upkeep()
    def addPos(self,playerIndex,card):
        c=cardData()
        if card.cardType=="player":
            player=c.getNameIndex(card.cardName)
            for a in range(len(self.players[0])):
                self.players[player][a]=1
            self.players[player][playerIndex]=2
        if card.cardType=="weapon":
            weapon=c.getWeaponIndex(card.cardName)
            for a in range(len(self.weapons[0])):
                self.weapons[weapon][a]=1
            self.weapons[weapon][playerIndex]=2
        if card.cardType=="room":
            room=c.getRoomIndex(card.cardName)
            for a in range(len(self.rooms[0])):
                self.rooms[room][a]=1
            self.rooms[room][playerIndex]=2
        self.upkeep()
    def addStr(self,playerIndex,guess):
        self.tripleStat.append((playerIndex,guess))
        self.upkeep()
    def upkeep(self):
        c=cardData()
        changed=False
        for a in self.tripleStat:
            guess=a[1]
            player=c.getNameIndex(guess[0])
            weapon=c.getWeaponIndex(guess[1])
            room=c.getRoomIndex(guess[2])
            p=self.players[player][a[0]]==1
            w=self.weapons[weapon][a[0]]==1
            r=self.rooms[room][a[0]]==1
            if p and w and r:
                print("somethings off... ",p,w,r)
            if w and r:
                cd=card(0,player)
                if self.players[player][a[0]]!=2:
                    changed=True
                    self.addPos(a[0],cd)
            if p and r:
                cd=card(1,weapon)
                if self.weapons[weapon][a[0]]!=2:
                    changed=True
                    self.addPos(a[0],cd)
            if p and w:
                cd=card(2,room)
                if self.rooms[room][a[0]]!=2:
                    changed=True
                    self.addPos(a[0],cd)
        if changed:
            self.upkeep()
    def calcGuess(self):
        c=cardData()
        import random
        max=0
        for player in self.players:
            if value(player)>max:
                max=value(player)
        plst=[]
        for a in range(len(self.players)):
            if value(self.players[a])==max:
                plst.append(c.cardNames[0][a])
        player=random.choice(plst)
        max=0
        for weapon in self.weapons:
            if value(weapon)>max:
                max=value(weapon)
        wlst=[]
        for a in range(len(self.weapons)):
            if value(self.weapons[a])==max:
                wlst.append(c.cardNames[1][a])
        weapon=random.choice(wlst)
        max=0
        for room in self.rooms:
            if value(room)>max:
                max=value(room)
        import copy
        rlst=[]
        for a in range(max+1):
            temp=[]
            for b in range(len(self.rooms)):
                if value(self.rooms[b])==a:
                    temp.append(b)
            rlst.append(copy.copy(temp))
        return (player,weapon,rlst)
    def print(self):
        c=cardData()
        size=17
        print("players"+" "*(size-7),end="")
        for a in g.names:
            print(a[0].upper(),end="")
        print("")
        for a in range(c.nCards[0]):
            text=c.cardNames[0][a]
            print(text+" "*(size-len(text)),end="")
            for a in self.players[a]:
                print(a,end="")
            print("")
        print("")
        print("weapons"+" "*(size-7),end="")
        for a in g.names:
            print(a[0].upper(),end="")
        print("")
        for a in range(c.nCards[1]):
            text=c.cardNames[1][a]
            print(text+" "*(size-len(text)),end="")
            for a in self.weapons[a]:
                print(a,end="")
            print("")
        print("")
        print("rooms"+" "*(size-5),end="")
        for a in g.names:
            print(a[0].upper(),end="")
        print("")
        for a in range(c.nCards[2]):
            text=c.cardNames[2][a]
            print(text+" "*(size-len(text)),end="")
            for a in self.rooms[a]:
                print(a,end="")
            print("")
        input()

class ai:
    def __init__(self,playerIndex,cards,nPlayers):
        self.hand=cards
        self.data=dataBase(nPlayers,cards,playerIndex)
        self.debugEvents=[]
    def event(self,event):
        if event[0]=="show":
            self.data.addStr(event[1],event[2])
            self.debugEvents.append("somebody showed a card to someone else")
        if event[0]=="pass":
            self.data.addNull(event[1],event[2])
            self.debugEvents.append("somebody didnt show a card")
        if event[0]=="has":
            self.data.addPos(event[1],event[2])
            self.debugEvents.append("somebody showed a card to me")
    def move(self,cords,rv1,rv2):
        roll=rv1+rv2
        import copy
        guess=self.data.calcGuess()
        player=guess[0]
        weapon=guess[1]
        paths=self.recurs([cords],roll)
        max=-1
        follow=[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
        for path in paths:
            room=path[0]-2
            if complexScore(guess[2],room)==max:
                if len(path[1])<len(follow):
                    follow=copy.copy(path[1])
            if complexScore(guess[2],room)>max:
                follow=copy.copy(path[1])
                max=complexScore(guess[2],room)
        if follow.count(9)==20:
            paths=self.recurs([cords],12)
            max=-2
            for path in paths:
                room=path[0]-2
                if complexScore(guess[2],room)==max:
                    if len(path[1])<len(follow):
                        follow=copy.copy(path[1])
                if complexScore(guess[2],room)>=max:
                    follow=copy.copy(path[1])
                    max=complexScore(guess[2],room)
            follow=follow[:roll+1]
            return ("move",follow)
        return ("guess",follow,(player,weapon))
    def recurs(self,path,length):
        import copy
        x=path[len(path)-1][0]
        y=path[len(path)-1][1]
        inRoom=False
        if mapdata.pathBoard[y][x]>1:
            inRoom=True
            yield (mapdata.pathBoard[y][x],copy.copy(path))
        if length!=0:
            cords=[(x,y)]
            if inRoom:
                cords=copy.copy(mapdata.doors[mapdata.pathBoard[y][x]-2])
                exits=[]
                for a in mapdata.exits[mapdata.pathBoard[y][x]-2]:
                    if not a in mapdata.doors[mapdata.pathBoard[y][x]-2]:
                        path.append((a[0],a[1]))
                        yield from self.recurs(path,length-1)
                        path.pop()
            for x, y in cords:
                for d in range(4):
                    nx=x+globaldx[d]
                    ny=y+globaldy[d]
                    if nx>=0 and ny>=0 and nx<24 and ny<25:
                        if not (nx,ny) in path:
                            path.append((nx,ny))
                            if mapdata.pathBoard[ny][nx]<1:
                                yield from self.recurs(path,length-1)
                            if mapdata.pathBoard[ny][nx]>1 and mapdata.pathBoard[y][x]!=-1:
                                yield from self.recurs(path,length-1)
                            path.pop()
    def respond(self,guess):
        c=cardData()
        temp=[]
        for card in self.hand:
            temp.append(card.cardName)
        choices=[]
        for a in temp:
            if a in guess:
                choices.append(a)
        types=[]
        for a in range(len(choices)):
            types.append(c.getCardType(choices[a]))
        if "player" in types:
            return choices[types.index("player")]
        if "room" in types:
            return choices[types.index("room")]
        if "weapon" in types:
            return choices[types.index("weapon")]
        return None
    def debug(self):
        print("")
        print("my cards ")
        print("")
        print("these things happened to me")
        for a in self.debugEvents:
            print(a)
        self.debugEvents=[]
        print("")
        for a in self.hand:
            a.print()
        print("")
        self.data.print()
        print("")

class player:
    def __init__(self,playerIndex,cards):
        self.playerIndex=playerIndex
        self.hand=[]
        for a in cards:
            self.hand.append(a.cardName)
        self.textBoxes=[tileGraphics.textBox(graphics,24,0,12,25,nRows=50,rowBoxes=True),tileGraphics.textBox(graphics,36,0,8,len(self.hand),nRows=len(self.hand),rowBoxes=True),tileGraphics.textBox(graphics,36,len(self.hand)+1,8,25-len(self.hand),nRows=25-len(self.hand),rowBoxes=True)]
        self.events=[]
        self.renderActions=False
    def render(self):
        graphics.put(24,0,0,width=20,height=25)
        graphics.putTextArray(self.textBoxes[0],self.events)
        graphics.putTextArray(self.textBoxes[1],self.hand)
        if self.renderActions:
            if g.getRoom(self.playerIndex)!=-1:
                graphics.putTextArray(self.textBoxes[2],["moves remaining:"+str(self.remaining),"end turn","make guess"])
            else:
                graphics.putTextArray(self.textBoxes[2],["moves remaining:"+str(self.remaining),"end turn"])


        global showy,turn
        for y in range(showy,25):
            graphics.put(24,y,0,width=2)
            if y-showy==turn:
                graphics.putSprite(25,y,characterSprites.get(g.names[turn]))
            else:
                graphics.putSprite(24,y,characterSprites.get(g.names[y-showy]))



    def event(self,event):
        global globalEvent
        if globalEvent!="":
            self.events.append(globalEvent)
            globalEvent=""
        if event[0]=="show":
            text=g.names[event[1]]+" showed a card"
            self.events.append(text)
        if event[0]=="pass":
            text=g.names[event[1]]+" did not show a card"
            self.events.append(text)
        if event[0]=="has":
            text=g.names[event[1]]+" showed you "+event[2].cardName
            self.events.append(text)
        self.render()
        graphics.update()
    def move(self,cords,rv1,rv2):
        self.remaining=rv1+rv2
        self.renderActions=True
        cont=True
        x, y=cords
        while cont:
            checkExit(graphics)
            tile=mapdata.pathBoard[y][x]
            posis=[]
            if self.remaining>0:
                if tile<1:
                    for d in range(4):
                        nx=x+globaldx[d]
                        ny=y+globaldy[d]
                        if nx>=0 and nx<24 and ny>=0 and ny<25:
                            newtile=mapdata.pathBoard[ny][nx]
                            if newtile>1:
                                if tile!=-1:
                                    posis.append((nx,ny))
                            if newtile<1:
                                posis.append((nx,ny))
                else:
                    for x, y in mapdata.doors[tile-2]:
                        for d in range(4):
                            nx=x+globaldx[d]
                            ny=y+globaldy[d]
                            if mapdata.pathBoard[ny][nx]==0:
                                posis.append((nx,ny))
                    for cord in mapdata.exits[tile-2]:
                        if not cord in mapdata.doors[tile-2]:
                            posis.append((cord[0],cord[1]))
            g.playerCords[self.playerIndex]=(x,y)
            for tx, ty in posis:
                graphics.highlight(tx,ty,(0,255,0))
            self.render()
            while not graphics.checkClick():
                checkExit(graphics)
                graphics.update()
            while graphics.checkClick():
                checkExit(graphics)
                graphics.update()
            for tx, ty in posis:
                graphics.highlight(tx,ty,(0,0,0))
                graphics.highlight(tx,ty,(255,255,255),lineWidth=1)
            graphics.put(x,y,0)
            nx, ny=graphics.mouseTile()
            if (nx,ny) in posis:
                x=nx
                y=ny
                self.remaining-=1
            graphics.putSprite(x,y,characterSprites.get(g.names[self.playerIndex]))
            if nx>35:
                ny=ny-len(self.hand)-1
                if ny==1:
                    self.renderActions=False
                    self.events=[]
                    graphics.put(36,0,0,width=8,height=25)
                    return ("move",[(x,y)])
                if ny==2 and tile>1:
                    c=cardData()
                    nx=0
                    ny=0
                    self.renderActions=False
                    while nx<36 or ny==0 or ny>c.nCards[0]:
                        checkExit(graphics)
                        while graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        graphics.put(36,0,0,width=8,height=25)
                        self.render()
                        graphics.putTextArray(self.textBoxes[2],["pick player"]+c.cardNames[0])
                        while not graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        while graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        nx, ny=graphics.mouseTile()
                        ny=ny-len(self.hand)-1
                    player=c.cardNames[0][ny-1]
                    nx=0
                    ny=0
                    while nx<36 or ny==0 or ny>c.nCards[1]:
                        checkExit(graphics)
                        while graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        graphics.put(36,0,0,width=8,height=25)
                        self.render()
                        graphics.putTextArray(self.textBoxes[2],["pick weapon"]+c.cardNames[1])
                        while not graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        while graphics.checkClick():
                            checkExit(graphics)
                            graphics.update()
                        nx, ny=graphics.mouseTile()
                        ny=ny-len(self.hand)-1
                    weapon=c.cardNames[1][ny-1]
                    room=c.cardNames[2][tile-2]
                    self.events=[]
                    graphics.put(36,0,0,width=8,height=25)
                    self.renderActions=False
                    return ("guess",[(x,y)],(player,weapon))
    def respond(self,guess):
        global globalEvent
        if globalEvent!="":
            self.events.append(globalEvent)
            globalEvent=""
        selections=[]
        for a in self.hand:
            if a in guess:
                selections.append(1)
            else:
                selections.append(0)
        if selections.count(1)==0:
            self.events.append("you did not have a card to show")
            self.render()
            graphics.update()
            return None
        self.events.append("choose a card to show")
        self.render()
        for a in range(len(selections)):
            if selections[a]==1:
                graphics.highlight(36,a,(0,255,0),width=8,height=1)
        graphics.update()
        cont=True
        while cont:
            checkExit(graphics)
            x=0
            y=0
            while x<36 or y>=len(self.hand):
                checkExit(graphics)
                while not graphics.checkClick():
                    checkExit(graphics)
                    graphics.update()
                while graphics.checkClick():
                    checkExit(graphics)
                    graphics.update()
                x, y=graphics.mouseTile()
            if selections[y]==1:
                cont=False
        self.events.append("you showed "+self.hand[y])
        self.render()
        return self.hand[y]



#simple startup menu
import tileGraphics
g=tileGraphics.graphics(12,7,fullScreen=True)
button=tileGraphics.textBox(g,8,0,4,1,nRows=1,rowBoxes=True)
idk=[tileGraphics.textBox(g,8,1,1,1,nRows=1,rowBoxes=True),tileGraphics.textBox(g,9,1,2,1,nRows=1,rowBoxes=True),tileGraphics.textBox(g,11,1,1,1,nRows=1,rowBoxes=True)]
button2=tileGraphics.textBox(g,8,2,4,1,nRows=1,rowBoxes=True)
title=tileGraphics.textBox(g,0,0,7,1,font="terminal",nRows=1)
characters=tileGraphics.textBox(g,0,1,4,6,font="terminal",rowBoxes=True,nRows=6)
info=tileGraphics.textBox(g,8,3,4,4,nRows=8)
g.putTextArray(idk[0],["<"])
g.putTextArray(idk[2],[">"])
g.putTextArray(info,["","d = disabled","a = ai","p = player","press s to start","hold esc at any time","to exit"])
g.putTextArray(title,["clue               D  A  P"])
g.putTextArray(characters,["scarlet","mustard","plum","peacock","green","white"])
g.putTextArray(button,["shuffle"])
rando=[0,1,2,3,4,5]
data=[0,0,0,0,0,0]
ss1=False
ss2=False
num=1
import time
for y in range(1,7):
    g.put(4,y,4)


while not g.checkKey(115) and not ss1:
    checkExit(g)
    g.putTextArray(idk[1],[str(num)])
    if num==1:
        g.putTextArray(button2,["all random"])
    else:
        g.putTextArray(button2,["random"])
    g.update()
    if g.checkClick() or ss2:
        x, y=g.mouseTile()
        if (x==8 and y==1) and not ss2:
            while g.checkClick():
                g.update()
            if num!=1:
                num-=1
        if (x==11 and y==1) and not ss2:
            while g.checkClick():
                g.update()
            if num!=6:
                num+=1
        if (x>7 and x<12 and y==2) and not ss2:
            while g.checkClick():
                g.update()
            from random import randint as rand
            if num==1:
                for a in range(300):
                    num=rand(2,6)
                    g.putTextArray(idk[1],[str(num)])
                    g.update()
                    checkExit(g)
            data=[0,0,0,0,0,0]
            while sum(data)<num:
                data[rand(0,5)]=1
            while sum(data)<num+1:
                h=rand(0,5)
                if data[h]==1:
                    data[h]=2
            tim=time.time()
            ss2=True
        if ss2:
            dif=time.time()-tim
            if dif>3:
                g.putTextArray(characters,temp)
                for b in range(1,7):
                    for a in range(4,7):
                        g.put(a,b,0)
                    g.put(data[rando[b-1]]+4,b,4)
                g.update()
                ss2=False
                g.update()
                tim=time.time()
                while time.time()-tim<1:
                    g.update()
                    checkExit(g)
                ss1=True
        if (x>7 and x<12 and y==0) or ss2:
            rando=scramble(rando)
            temp=[]
            for a in rando:
                temp.append(["scarlet","mustard","plum","peacock","green","white"][a])
                g.putTextArray(characters,temp)
            for b in range(1,7):
                for a in range(4,7):
                    g.put(a,b,0)
                g.put(data[rando[b-1]]+4,b,4)
            g.update()
        if (x>3 and y>0 and x<7 and y<7) and not ss2:
            c=y-1
            s=x-4
            if s==2:
                if 2 in data:
                    ty=data.index(2)
                    data[ty]=1
            data[rando[c]]=s
            for b in range(1,7):
                for a in range(4,7):
                    g.put(a,b,0)
                g.put(data[rando[b-1]]+4,b,4)
            g.update()
#some data post processing

for a in range(6):
    if data[a]==0:
        data[a]=-1

#main game
globalEvent=""
g=game(scarlet=data[rando[0]],mustard=data[rando[1]],plum=data[rando[2]],peacock=data[rando[3]],green=data[rando[4]],white=data[rando[5]])
mapdata=boardData()
globaldx=[0,-1,0,1]
globaldy=[-1,0,1,0]
hands=g.hands
hi=0
players=[]
from random import randint as rand
for a in range(6):
    if data[rando[a]]>0:
        if data[rando[a]]==1:
            players.append(ai(hi,hands[hi],g.nPlayers))
        else:
            players.append(player(hi,hands[hi]))
        hi+=1

g.render()
g.update()
import time
time.sleep(1)
turn=0
cdat=cardData()
showy=25-len(g.names)
while not g.solved:
    print(g.names[turn]+"s turn")
    for y in range(showy,25):
        graphics.put(24,y,0,width=2)
        if y-showy==turn:
            graphics.putSprite(25,y,characterSprites.get(g.names[turn]))
        else:
            graphics.putSprite(24,y,characterSprites.get(g.names[y-showy]))
#    if turn==0:
#        players[0].debug()
    rv1=rand(1,6)
    rv2=rand(1,6)
    print("rolled",rv1+rv2)
    graphics.putComplexSprite(6,10,diceSprites.get(str(rv1)))
    graphics.putComplexSprite(13,10,diceSprites.get(str(rv2)))
    graphics.update()
    time.sleep(.5)
    checkExit(graphics)
    g.render()
    action=players[turn].move(g.playerCords[turn],rv1,rv2)
    g.applyMove(action,turn)
    if action[0]=="guess":
        room=g.getRoom(turn)
        if room!=-1:
            room=cdat.cardNames[2][room]
            player=action[2][0]
            weapon=action[2][1]
            guess=(player,weapon,room)
            print(g.names[turn],"guessed",guess[0],"in the",guess[2],"with the",guess[1])
            globalEvent=g.names[turn]+" guessed "+guess[0]+" in the "+guess[2]+" with the "+guess[1]
            tempturn=turn+1
            if tempturn==g.nPlayers:
                tempturn=0
            answer=None
            while tempturn!=turn and answer==None:
                answer=players[tempturn].respond(guess)
                if answer==None:
                    print(g.names[tempturn],"did not show a card")
                    for a in range(g.nPlayers):
                        if a!=tempturn:
                            players[a].event(("pass",tempturn,guess))
                else:
                    print(g.names[tempturn],"showed a card")
                    for a in range(g.nPlayers):
                        if a!=tempturn and a!=turn:
                            players[a].event(("show",tempturn,guess))
                    players[turn].event(("has",tempturn,cdat.genCard(answer)))
                tempturn+=1
                if tempturn==g.nPlayers:
                    tempturn=0
            if answer==None:
                bool=g.checkSolution(guess)
                if bool:
                    print(g.names[turn],"won the game!!!")
                    end={'mrs scarlet':(255,0,0),'colonel mustard':(255,255,0),'professor plum':(128,0,128),'mrs peacock':(0,255,255),'mr green':(0,255,0),'mrs white':(255,255,255)}
                    color=end[g.names[turn]]
                    cords=[]
                    for y in range(25):
                        for x in range(44):
                            cords.append((x,y))
                    cords=scramble(cords)
                    graphics.palette.add(color)
                    title=tileGraphics.textBox(graphics,9,7,26,5,nRows=2,rowBoxes=True)
                    rows=tileGraphics.textBox(graphics,9,12,26,6,nRows=2,rowBoxes=True)
                    sol=tileGraphics.textBox(graphics,0,0,9,4,nRows=4,rowBoxes=True)
                    p=0
                    for a in range(275):
                        for b in range(4):
                            x, y=cords[p]
                            graphics.put(x,y,8)
                            p+=1
                        graphics.update()
                    graphics.putTextArray(title,[g.names[turn],"won the game!!!"])
                    graphics.update()
                    import time
                    time.sleep(1)
                    graphics.putTextArray(sol,["solution"]+[a.cardName for a in g.solution])
                    graphics.putTextArray(rows,["new game","exit"])
                    graphics.update()
                    x=0
                    y=0
                    while x<9 or x>34 or y<7 or y>17:
                        while not graphics.checkClick():
                            graphics.update()
                        while graphics.checkClick():
                            graphics.update()
                        x, y=graphics.mouseTile()
                    if y>11 and y<15:
                        import os
                        os.system("start python clue.py")
                    exit()
    turn+=1
    if turn==g.nPlayers:
        turn=0
    g.render()
    g.update()
    import time
    time.sleep(1)
    checkExit(graphics)

file1 = open("input.txt","r")
contents = file1.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].strip("\n")

hX = 0
hY = 0
tX = 0
tY = 0
xPos = 0
yPos = 0
places = [(0,0)]
test= []
xCoor = [0,0,0,0,0,0,0,0,0,0]
yCoor = [0,0,0,0,0,0,0,0,0,0]

""" for x in contents:
    xMove = 0
    yMove = 0
    if(x[0] == "R"):
        xMove = 0 + int(x[2:])
    elif(x[0] == "L"):
        xMove = 0 - int(x[2:])
    elif(x[0] == "U"):
        yMove = 0 + int(x[2:])
    elif(x[0] == "D"):
        yMove = 0 - int(x[2:])

    if(abs(xMove) > abs(yMove)):
        counter = xMove
        yPos = 0
        if(xMove > 0):
            xPos = 1
        else:
            xPos = -1
    else:
        counter = yMove
        xPos = 0
        if(yMove > 0):
            yPos = 1
        else:
            yPos = -1
    for y in range(abs(counter)):
        hX += xPos
        hY += yPos
        if((abs(hX - tX) > 1 and hY != tY) or (abs(hY - tY) > 1 and hX != tX)):
            if(hX - tX > 0):
                xAdj = 1
            else:
                xAdj = -1
            if(hY - tY > 0):
                yAdj = 1
            else:
                yAdj = -1
                
            tX += xAdj
            tY += yAdj
        elif(abs(hX - tX) > 1):
            if(hX - tX > 0):
                xAdj = 1
            else:
                xAdj = -1

            tX += xAdj
        elif(abs(hY - tY) > 1):
            if(hY - tY > 0):
                yAdj = 1
            else:
                yAdj = -1
                    
            tY += yAdj
        
        places.append((tX, tY))

places = set(places)
print(len(places)) """

for x in contents:
    xMove = 0
    yMove = 0
    if(x[0] == "R"):
        xMove = 0 + int(x[2:])
    elif(x[0] == "L"):
        xMove = 0 - int(x[2:])
    elif(x[0] == "U"):
        yMove = 0 + int(x[2:])
    elif(x[0] == "D"):
        yMove = 0 - int(x[2:])

    if(abs(xMove) > abs(yMove)):
        counter = xMove
        yPos = 0
        if(xMove > 0):
            xPos = 1
        else:
            xPos = -1
    else:
        counter = yMove
        xPos = 0
        if(yMove > 0):
            yPos = 1
        else:
            yPos = -1
    for y in range(abs(counter)):
        xCoor[0] += xPos
        yCoor[0] += yPos
        for z in range(1,10):
            try:
                if((abs(xCoor[z-1] - xCoor[z]) > 1 and yCoor[z-1] != yCoor[z]) or (abs(yCoor[z-1] - yCoor[z]) > 1 and xCoor[z-1] != xCoor[z])):
                    if(xCoor[z-1] - xCoor[z] > 0):
                        xAdj = 1
                    else:
                        xAdj = -1
                    if(yCoor[z-1] - yCoor[z] > 0):
                        yAdj = 1
                    else:
                        yAdj = -1
                        
                    xCoor[z] += xAdj
                    yCoor[z] += yAdj
                elif(abs(xCoor[z-1] - xCoor[z]) > 1):
                    if(xCoor[z-1] - xCoor[z] > 0):
                        xAdj = 1
                    else:
                        xAdj = -1
                    xCoor[z] += xAdj
                elif(abs(yCoor[z-1] - yCoor[z]) > 1):
                    if(yCoor[z-1] - yCoor[z] > 0):
                        yAdj = 1
                    else:
                        yAdj = -1
                    yCoor[z] += yAdj
            except:
                pass
            places.append((xCoor[9], yCoor[9]))

places = set(places)
print(len(places))
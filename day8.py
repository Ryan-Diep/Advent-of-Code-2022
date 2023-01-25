file1 = open("input.txt","r")
contents = file1.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].strip("\n")

formated = []
counter = 0

for x in range(len(contents)):
    contents[x] = [*contents[x]]

for x in range(len(contents)):
    for y in range(len(contents[x])):
        contents[x][y] = int(contents[x][y])

for x in range(len(contents)):
    for y in range(len(contents[x])):
        left = True 
        right = True 
        up = True
        down = True
        for a in range(1,len(contents)+1):
            if(x-a >= 0):
                if(contents[x][y] <= contents[x-a][y]):
                    up = False
            if(x+a < len(contents[x])):
                if(contents[x][y] <= contents[x+a][y]):
                    down = False

        for b in range(1,len(contents[x])+1):
            if(y-b >= 0):
                if(contents[x][y] <= contents[x][y-b]):
                    left = False
            if(y+b < len(contents)):
                if(contents[x][y] <= contents[x][y+b]):
                    right = False
            
        if(left == True or right == True or up == True or down == True):
            counter += 1

print(counter)
""" for x in range(len(contents)):
    contents[x] = [*contents[x]]

for x in range(len(contents)):
    for y in range(len(contents[x])):
        contents[x][y] = int(contents[x][y])

for x in range(len(contents)):
    for y in range(len(contents[x])):
        left = True 
        right = True 
        up = True
        down = True
        counter2 = 1
        for a in range(1,len(contents)+1):
            if(x-a >= 0):
                if(contents[x][y] <= contents[x-a][y] and up == True):
                    counter2 = counter2*a
                    up = False
                elif(x-a == 0 and up == True):
                    counter2 = counter2*a
            if(x+a < len(contents[x])):
                if(contents[x][y] <= contents[x+a][y] and down == True):
                    counter2 = counter2*a
                    down = False
                elif(x+a == len(contents[x])-1 and down == True):
                    counter2 = counter2*a

        for b in range(1,len(contents[x])+1):
            if(y-b >= 0):
                if(contents[x][y] <= contents[x][y-b] and left == True):
                    counter2 = counter2*b
                    left = False
                elif(y-b == 0 and left == True):
                    counter2 = counter2*b
            if(y+b < len(contents)):
                if(contents[x][y] <= contents[x][y+b] and right == True):
                    counter2 = counter2*b
                    right = False
                elif(y+b == len(contents)-1 and right == True):
                    counter2 = counter2*b
        if(counter < counter2):
            counter = counter2
print(counter) """
file1 = open("input.txt","r")
contents = file1.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].strip("\n")

items = []
inspect = [] 
test = []
monkey = 0

""" for x in range(8):
    items.append([])
    inspect.append([0])

for a in range(20):
    counter = 0
    for x in contents:
        if(counter == 0):
            monkey = int(x[-2])
        elif(counter == 1):
            if(a == 0):
                for y in range(len(x)):
                    try:
                        items[monkey].append(int(x[17+4*y:20+4*y]))
                        
                    except:
                        pass
        elif(counter == 2):
            change = ""
            if(x[23] == "*"):
                for y in range(len(items[monkey])):
                    inspect[monkey][0] += 1
                    try:
                        change = int(x[-2:])
                    except:
                        try:
                            change = int(x[-1])
                        except:
                            change = items[monkey][y]
                    items[monkey][y] = (items[monkey][y] * change)//3
            else:
                for y in range(len(items[monkey])):
                    inspect[monkey][0] += 1
                    try:
                        change = int(x[-1])
                    except:
                        change = items[monkey][y]
                    items[monkey][y] = (items[monkey][y] + change)//3
        elif(counter == 3):
            test = []
            divisor = 0
            try:
                divisor = int(x[-2:])
            except:
                divisor = int(x[-1])
            for y in items[monkey]:
                if(y%divisor == 0):
                    test.append(True)
                else:
                    test.append(False)
        elif(counter == 4):
            for y in range(len(test)):
                if(test[y]):
                    items[int(x[-1])].append(items[monkey][y])
        elif(counter == 5):
            for y in range(len(test)):
                if(test[y] == False):
                    items[int(x[-1])].append(items[monkey][y])
            items[monkey] = []
        counter += 1
        if(counter == 7):
            counter = 0

print(items)
print(inspect) """

items = [[54, 98, 50, 94, 69, 62, 53, 85], [71, 55, 82], [77, 73, 86, 72, 87], [97, 91], [78, 97, 51, 85, 66, 63, 62], [88], [87, 57, 63, 86, 87, 53], [73, 59, 82, 65]]
inspect = [0, 0, 0, 0, 0, 0, 0, 0] 
divisors = [3, 13, 19, 17, 5, 7, 11, 2]
operations = ["y * 13", "y + 2", "y + 8", "y + 1", "y * 17", "y + 3", "y * y", "y+6"]
loc = [[2,1],[7,2],[4,7],[6,5],[6,3],[1,0],[5,0],[4,3]]
supermod = 1
for x in divisors:
    supermod *= x

for a in range(10000):
    for x in range(8):
        for y in items[x]:
            inspect[x] += 1
            y = eval(operations[x])%supermod
            if(y%divisors[x] == 0):
                items[loc[x][0]].append(y)
            else:
                items[loc[x][1]].append(y)
        items[x] = []
        

inspect.sort()
print(sorted(inspect))
print(inspect[-1]*inspect[-2])
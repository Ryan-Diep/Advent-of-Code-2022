file1 = open("input.txt","r")
contents = file1.readlines()
path = []
system = []
possibilties = []
sum1 = 0
total = 0
space = []
ans = 70000000

for x in contents:
    if(x[0:4] == "$ cd"):
        if(x[5:].strip("\n") == ".."):
            path.pop(-1)
        elif(x[-2:].strip("\n") == " /"):
            try:
                path = ["/"]
            except:
                pass
        else:
            try:
                path.append(x[5:].strip("\n"))
            except:
                pass
    elif(x[0] != "$"):
        if(len(path) == 1):
            current = "//"
        else:
            current = "/".join(path)
        possibilties.append(current)
        system.append(current + "/" + x.strip("\n"))

possibilties = set(possibilties)

for x in possibilties:
    counter = 0
    for y in system:
        start = 100000
        end = 0
        first = True
        if(x == y[0:len(x)]):
            for z in range(len(y)):
                if(start == 100000 and (48 <= ord(y[z]) <= 57)):
                    start = z

                elif(z >= start and (48 > ord(y[z]) or ord(y[z]) > 57) and first):
                    end = z
                    counter = counter + int(y[start:end])
                    first = False
    if(counter < 100000):
        sum1 = sum1+ counter
print(sum1)

""" for x in contents:
    if(x[0:4] == "$ cd"):
        if(x[5:].strip("\n") == ".."):
            path.pop(-1)
        elif(x[-2:].strip("\n") == " /"):
            try:
                path = ["/"]
            except:
                pass
        else:
            try:
                path.append(x[5:].strip("\n"))
            except:
                pass
    elif(x[0] != "$"):
        if(len(path) == 1):
            current = "//"
        else:
            current = "/".join(path)
        possibilties.append(current)
        system.append(current + "/" + x.strip("\n"))

possibilties = set(possibilties)

for x in possibilties:
    counter = 0
    for y in system:
        start = 100000
        end = 0
        first = True
        if(x == y[0:len(x)]):
            for z in range(len(y)):
                if(start == 100000 and (48 <= ord(y[z]) <= 57)):
                    start = z
                
                elif(z >= start and (48 > ord(y[z]) or ord(y[z]) > 57) and first):
                    end = z
                    counter = counter + int(y[start:end])
                    first = False
    if(x=="//"):
        total = counter
    space.append(counter)
for x in space:
    print((70000000-(total-x)))
    print((70000000-(total-ans)))
    
    if((70000000-(total-x)) < (70000000-(total-ans)) and (70000000-(total-x)) >= 30000000):
        ans = x
        print(ans)
    
print(ans)
 """
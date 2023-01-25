file1 = open("input.txt","r")
contents = file1.readlines()
for x in range(len(contents)):
    contents[x] = contents[x].strip("\n")

cycle = 0
val = 1
total = 0
l = []
pos = [0,1,2]
first = True
valid = False
""" for x in contents:
    if(x == "noop"):
        cycle += 1
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            total = total + cycle*val

    else:
        cycle += 1

        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            total = total + cycle*val
        cycle += 1
        val += int(x.split()[1])
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            total = total + cycle*val
        
print(total) """

for x in contents:
    if(x == "noop"):
        valid = False
        cycle += 1
        if(cycle == 40):
            cycle = 0
        print(pos,cycle)
        for y in pos:
            if(cycle == y):
                valid = True
        if(valid):
            l.append("#")
        else:
            l.append(".")

    else:
        valid = False
        cycle += 1
        if(cycle == 40):
            cycle = 0
        print(pos,cycle)
        for y in pos:
            if(cycle == y):
                valid = True
        if(valid):
            l.append("#")
        else:
            l.append(".")
        
        valid = False

        cycle += 1
        if(cycle == 40):
            cycle = 0
        print(pos,cycle)
        for y in pos:
            if(cycle == y):
                valid = True
        if(valid):
            l.append("#")
        else:
            l.append(".")
        if(first):
            val = int(x.split()[1])+1
            first = False
        else:
            val = int(x.split()[1])
        for y in range(len(pos)):
            pos[y] += val

""" print(l)"""
for x in range(6):
    print(" ".join(l[x*40:(x+1)*40])) 
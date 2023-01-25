""" file1 = open("input.txt","r")
contents = file1.readlines()
temp = []
boxes = []
boxes1 = []
ans = []
counter = 0

for x in range(8):
  temp.append(list(contents[x]))
  for y in range(1,len(contents[x]), 4):
    boxes.append(temp[x][y])

for x in range(9):
  boxes1.append([])
  for y in range(8):
    if(boxes[y*9+x]!= " "):
      boxes1[x].append(boxes[y*9+x])

print(boxes1)
for x in range(10, len(contents)):
  string = contents[x].split(" ")
  first=int(string[1])
  second=int(string[3])-1
  third=int(string[5])-1
  print(first,second,third)
  
  for y in range(first):
    try:
      boxes1[third].insert(0,(boxes1[second][0]))
    except:
      pass
    try:
      boxes1[second].pop(0)
    except:
      pass
  print(boxes1)

for x in range(9):
  ans.append(boxes1[x][0])

final = "".join(ans)
print(final) """

file1 = open("input.txt","r")
contents = file1.readlines()
temp = []
boxes = []
boxes1 = []
ans = []
counter = 0

for x in range(8):
  temp.append(list(contents[x]))
  for y in range(1,len(contents[x]), 4):
    boxes.append(temp[x][y])

for x in range(9):
  boxes1.append([])
  for y in range(8):
    if(boxes[y*9+x]!= " "):
      boxes1[x].append(boxes[y*9+x])

print(boxes1)
for x in range(10, len(contents)):
  string = contents[x].split(" ")
  first=int(string[1])
  second=int(string[3])-1
  third=int(string[5])-1
  print(first,second,third)
  
  for y in range(first):
    boxes1[third].insert(0,(boxes1[second][first-y-1]))
    boxes1[second].pop(first-y-1)
  print(boxes1)

for x in range(9):
  ans.append(boxes1[x][0])

final = "".join(ans)
print(final)
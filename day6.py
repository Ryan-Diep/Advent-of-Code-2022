file1 = open("input.txt","r")
contents = file1.readlines()
temp =[]

for letter in contents[0]:
    temp.append(letter)

for x in range(13, len(temp)):
    l = []
    for y in range(14):
        l.append(temp[x-y])

    for y in range(26):
        try:
            l.remove(chr(97+y))
        except:
            pass

    if(not l):
        print(x+1)
        break

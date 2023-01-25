file1 = open("input.txt","r")
contents = file1.readlines()
counter = 0

for x in contents:
  temp = x.split(",")
  first = temp[0]
  first = first.split("-")
  second = temp[1]
  second = second.split("-")
  if((int(first[0]) <= int(second [0])) and (int(first[1]) >= int(second[1]))):
    counter = counter+1
  elif(int(second[0]) <= int(first [0]) and int(second[1]) >= int(first[1])):
    counter = counter+1

print(counter)

for x in contents:
  temp = x.split(",")
  first = temp[0]
  first = first.split("-")
  second = temp[1]
  second = second.split("-")
  if((int(first[0]) <= int(second [1])) and (int(first[1]) >= int(second[1]))):
    counter = counter+1

  elif(int(second[0]) <= int(first [0]) and int(second[1]) >= int(first[1])):
    counter = counter+1

  elif(int(first[0]) <= int(second [1])) and (int(first[1]) <= int(second[1]) and int(first[1]) >= int(second [0])):
    counter = counter+1

  elif(int(second[0]) <= int(first [1]) and int(second[1]) <= int(first[1]) and int(first[0]) <= int(second [1])):
    counter = counter+1

print(counter)

from itertools import combinations
list_f = []

with open("task1.txt", "r") as f:
     for line in f:
         try:
             list_f.append(int(line))
         except:
              print("Ввели что-то плохое")

for triplet in combinations(list_f, 3):
    x,y,z = tuple(triplet)
    if x + y + z == 2020:
       print((x, y, z))
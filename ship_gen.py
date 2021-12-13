import csv
import random

# 1x2, 2x3, 1x4, 1x5

row_num = col_num = 10

map_list = [[0 for i in range(row_num)] for i in range(col_num)]

def aaaaa():
  return map_list

def boat2(map_list):
  a = random.randint(1, 2)
  r1 = random.randint(0, col_num-2)
  r2 = random.randint(0, row_num-2)
  if a == 1:
    if map_list[r1][r2] == "@":
      r1 = random.randint(0, col_num-2)
      r2 = random.randint(0, row_num-2)
      map_list[r1][r2] = "@"
      map_list[r1][r2+1] = "@"
    else:
      map_list[r1][r2] = "@"
      map_list[r1][r2+1] = "@"
  else:
    if map_list[r1][r2] == "@":
      r1 = random.randint(0, col_num-2)
      r2 = random.randint(0, row_num-2)
      map_list[r1][r2] = "@"
      map_list[r1+1][r2] = "@"
    else:
      map_list[r1][r2] = "@"
      map_list[r1+1][r2] = "@"


def boat3(map_list):
  a = random.randint(1, 2)
  while True:
    r1 = random.randint(0, col_num-3)
    r2 = random.randint(0, row_num-3)
    if a == 1:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1][r2+1] == "@":
        pass
      elif map_list[r1][r2+2] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1][r2+1] = "@"
        map_list[r1][r2+2] = "@"
        break
    else:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1+1][r2] == "@":
        pass
      elif map_list[r1+2][r2] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1+1][r2] = "@"
        map_list[r1+2][r2] = "@"
        break

def boat4(map_list):
  a = random.randint(1, 2)
  while True:
    r1 = random.randint(0, col_num-4)
    r2 = random.randint(0, row_num-4)
    if a == 1:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1][r2+1] == "@":
        pass
      elif map_list[r1][r2+2] == "@":
        pass
      elif map_list[r1][r2+3] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1][r2+1] = "@"
        map_list[r1][r2+2] = "@"
        map_list[r1][r2+3] = "@"
        break
    else:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1+1][r2] == "@":
        pass
      elif map_list[r1+2][r2] == "@":
        pass
      elif map_list[r1+3][r2] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1+1][r2] = "@"
        map_list[r1+2][r2] = "@"
        map_list[r1+3][r2] = "@"
        break

def boat5(map_list):
  a = random.randint(1, 2)
  while True:
    r1 = random.randint(0, col_num-5)
    r2 = random.randint(0, row_num-5)
    if a == 1:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1][r2+1] == "@":
        pass
      elif map_list[r1][r2+2] == "@":
        pass
      elif map_list[r1][r2+3] == "@":
        pass
      elif map_list[r1][r2+4] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1][r2+1] = "@"
        map_list[r1][r2+2] = "@"
        map_list[r1][r2+3] = "@"
        map_list[r1][r2+4] = "@"
        break
    else:
      if map_list[r1][r2] == "@":
        pass
      elif map_list[r1+1][r2] == "@":
        pass
      elif map_list[r1+2][r2] == "@":
        pass
      elif map_list[r1+3][r2] == "@":
        pass
      elif map_list[r1+4][r2] == "@":
        pass
      else:
        map_list[r1][r2] = "@"
        map_list[r1+1][r2] = "@"
        map_list[r1+2][r2] = "@"
        map_list[r1+3][r2] = "@"
        map_list[r1+4][r2] = "@"
        break

def ships():
  boat2(map_list)
  boat3(map_list)
  boat3(map_list)
  boat4(map_list)
  boat5(map_list)

  with open(r"table2.csv", "w") as a:
    writer = csv.writer(a)
    for i in map_list:
      writer.writerow(i)

  with open(r"table.csv", "w") as a:
    writer = csv.writer(a)
    for i in map_list:
      if "@" in i:
        k = ""
        for j in i:
          if j == "@":
            k = k + "🚢"
          else:
            k = k + "🌊"
        writer.writerow(k)
      else:
        writer.writerow("🌊" * col_num)
  b = ""
  
  with open('table.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    for row in a:
      b = b + ' '.join(row)
      b = b + "\n"
  return b
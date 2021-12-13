import csv
from time import sleep
from os import system

def clear():
    system("cls")

ships = ["Destroyer(2)", "Submarine(3)", "Cruiser(3)", "Battleship(4)", "Carrier(5)"]

col_num = row_num = 10
p_map = [[0 for i in range(row_num)] for i in range(col_num)]

grid = {
  1: "a",
  2: "b",
  3: "c",
  4: "d",
  5: "e",
  6: "f",
  7: "g",
  8: "h",
  9: "i",
  10: "j"
}

for i in range(col_num):
  for j in range(row_num):
    p_map[i][j] = i, j
  

def god_help_me():
  return p_map

def boat2(g):
  while True:
    try:
      clear()
      with open(r"p_table2.csv", "w") as a:
        writer = csv.writer(a)
        for i in p_map:
          writer.writerow("0" * row_num)
      
      l = 0
      with open("p_table.csv", "w") as t:
        writer = csv.writer(t)
        for i in p_map:
          l = l + 1
          if "@" in i:
            k = ""
            for j in i:
              if j == "@":
                k = k + "🚢"
              else:
                k = k + "🌊"
            writer.writerow(str(grid[l]) + k)
          else:
            writer.writerow(str(grid[l]) +("🌊" * col_num))

      with open('p_table.csv', newline='') as csvfile:
        h = csv.reader(csvfile)
        print("   1  2  3  4  5  6  7  8  9  10")
        for row in h:
          print(' '.join(row))
      
      ask = input("Enter co-ordinates for Destroyer(2) (e.g a,1): ")
      ask = ask.replace(" ", "")
      ask = ask.replace("a", "0")
      ask = ask.replace("b", "1")
      ask = ask.replace("c", "2")
      ask = ask.replace("d", "3")
      ask = ask.replace("e", "4")
      ask = ask.replace("f", "5")
      ask = ask.replace("g", "6")
      ask = ask.replace("h", "7")
      ask = ask.replace("i", "8")
      ask = ask.replace("j", "9")
      ask = ask.split(",")
      r1 = int(ask[0])
      r2 = int(ask[1])-1
      dire = input("(H)orizontal or (V)ertical: ").lower()
      if "h" in dire[0]:
        if g[r1][r2] == "@":
          exit("Something has gone bloody wrong here mate, good luck lol")
        else:
          g[r1][r2] = "@"
          g[r1][r2+1] = "@"
          break
      else:
        if g[r1][r2] == "@":
          exit("Something has gone bloody wrong here mate, good luck lol")
        else:
          g[r1][r2] = "@"
          g[r1+1][r2] = "@"
          break
    except:
      print("Boat placement out of bounds.")
      g[r1][r2] = "0"
      sleep(2)
      pass


def boat3(map_list, _list, ii):
  while True:
    try:
      clear()
      with open(r"p_table2.csv", "w") as a:
        writer = csv.writer(a)
        for i in p_map:
          writer.writerow("0" * row_num)
    
      l = 0
      with open("p_table.csv", "w") as t:
        writer = csv.writer(t)
        for i in p_map:
          l = l + 1
          if "@" in i:
            k = ""
            for j in i:
              if j == "@":
                k = k + "🚢"
              else:
                k = k + "🌊"
            writer.writerow(str(grid[l]) + k)
          else:
            writer.writerow(str(grid[l]) +("🌊" * col_num))

      with open('p_table.csv', newline='') as csvfile:
        h = csv.reader(csvfile)
        print("   1  2  3  4  5  6  7  8  9  10")
        for row in h:
          print(' '.join(row))
    
      ask = input(f"Enter co-ordinates for {_list[ii]} (e.g a1): ")
      ask = ask.replace(",", "")
      ask = ask.replace(" ", "")
      ask = ask.replace("a", "0")
      ask = ask.replace("b", "1")
      ask = ask.replace("c", "2")
      ask = ask.replace("d", "3")
      ask = ask.replace("e", "4")
      ask = ask.replace("f", "5")
      ask = ask.replace("g", "6")
      ask = ask.replace("h", "7")
      ask = ask.replace("i", "8")
      ask = ask.replace("j", "9")
      r1 = int(ask[0])
      r2 = int(ask[1])-1
      dire = input("(H)orizontal or (V)ertical: ").lower()
      if "h" in dire[0]:
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
    except:
      pass

def boat4(map_list):
  while True:
    try:
      clear()
      with open(r"p_table2.csv", "w") as a:
        writer = csv.writer(a)
        for i in p_map:
          writer.writerow("0" * row_num)
    
      l = 0
      with open("p_table.csv", "w") as t:
        writer = csv.writer(t)
        for i in p_map:
          l = l + 1
          if "@" in i:
            k = ""
            for j in i:
              if j == "@":
                k = k + "🚢"
              else:
                k = k + "🌊"
            writer.writerow(str(grid[l]) + k)
          else:
            writer.writerow(str(grid[l]) +("🌊" * col_num))

      with open('p_table.csv', newline='') as csvfile:
        h = csv.reader(csvfile)
        print("   1  2  3  4  5  6  7  8  9  10")
        for row in h:
          print(' '.join(row))
    
      ask = input(f"Enter co-ordinates for Battleship(4) (e.g a1): ")
      ask = ask.replace(",", "")
      ask = ask.replace(" ", "")
      ask = ask.replace("a", "0")
      ask = ask.replace("b", "1")
      ask = ask.replace("c", "2")
      ask = ask.replace("d", "3")
      ask = ask.replace("e", "4")
      ask = ask.replace("f", "5")
      ask = ask.replace("g", "6")
      ask = ask.replace("h", "7")
      ask = ask.replace("i", "8")
      ask = ask.replace("j", "9")
      r1 = int(ask[0])
      r2 = int(ask[1])-1
      dire = input("(H)orizontal or (V)ertical: ").lower()
      if "h" in dire[0]:
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
    except:
      pass


def boat5(map_list):
  while True:
    try:
      clear()
      with open(r"p_table2.csv", "w") as a:
        writer = csv.writer(a)
        for i in p_map:
          writer.writerow("0" * row_num)
    
      l = 0
      with open("p_table.csv", "w") as t:
        writer = csv.writer(t)
        for i in p_map:
          l = l + 1
          if "@" in i:
            k = ""
            for j in i:
              if j == "@":
                k = k + "🚢"
              else:
                k = k + "🌊"
            writer.writerow(str(grid[l]) + k)
          else:
            writer.writerow(str(grid[l]) +("🌊" * col_num))

      with open('p_table.csv', newline='') as csvfile:
        h = csv.reader(csvfile)
        print("   1  2  3  4  5  6  7  8  9  10")
        for row in h:
          print(' '.join(row))
    
      ask = input(f"Enter co-ordinates for Carrier(5) (e.g a1): ")
      ask = ask.replace(",", "")
      ask = ask.replace(" ", "")
      ask = ask.replace("a", "0")
      ask = ask.replace("b", "1")
      ask = ask.replace("c", "2")
      ask = ask.replace("d", "3")
      ask = ask.replace("e", "4")
      ask = ask.replace("f", "5")
      ask = ask.replace("g", "6")
      ask = ask.replace("h", "7")
      ask = ask.replace("i", "8")
      ask = ask.replace("j", "9")
      r1 = int(ask[0])
      r2 = int(ask[1])-1
      dire = input("(H)orizontal or (V)ertical: ").lower()
      if "h" in dire[0]:
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
    except:
      pass

def start():
  boat2(p_map)
  clear()
  k = ["Submarine(3)", "Cruiser(3)"]
  i = 0
  boat3(p_map, k, i)
  clear()
  i =+ 1
  boat3(p_map, k, i)
  clear()
  boat4(p_map)
  clear()
  boat5(p_map)
  clear()

  with open(r"p_table2.csv", "w") as a:
    writer = csv.writer(a)
    for i in p_map:
      if "@" in i:
        k = ""
        for j in i:
          if j == "@":
            k = k + "@"
          else:
            k = k + "0"
        writer.writerow(k)
      else:
        writer.writerow("0" * row_num)
  
  l = 0
  with open("p_table.csv", "w") as t:
    writer = csv.writer(t)
    for i in p_map:
      l = l + 1
      if "@" in i:
        k = ""
        for j in i:
          if j == "@":
            k = k + "🚢"
          else:
            k = k + "🌊"
        writer.writerow(str(grid[l]) + k)
      else:
        writer.writerow(str(grid[l]) +("🌊" * col_num))

  b = ""
  with open('p_table.csv', newline='') as csvfile:
    h = csv.reader(csvfile)
    print("   1  2  3  4  5  6  7  8  9  10")
    for row in h:
      b = b + ' '.join(row)
      b = b + "\n"
  return b
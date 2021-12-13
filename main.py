import ship_gen
import player_gen
import csv
from random import randint as r
from time import sleep as s
from os import system

ai_board = ship_gen.ships()
p_board = player_gen.start()

row_num = col_num = 10

shot_at = []
pwins = 0
aiwins = 0

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

def clear():
    system("cls")

p_map = player_gen.god_help_me()
ai_map = ship_gen.aaaaa()

clear()
while True:
  with open(r"table2.csv", "w") as a:
    writer = csv.writer(a)
    for i in ai_map:
      writer.writerow(i)

  with open(r"p_table2.csv", "w") as a:
    writer = csv.writer(a)
    for i in p_map:
      writer.writerow(i)

  
  with open("table2.csv", newline='') as csvfile:
    print("   1  2  3  4  5  6  7  8  9  10")
    h = csv.reader(csvfile)
    l = 0
    for row in h:
      l = l + 1
      if "@" or "x" or "m" in row:
        k = ""
        for j in row:
          if j == "x":
            k = k + " 🔥"
          elif j == "m":
            k = k + " ⚪"
          else:
            k = k + " 🌊"
        print(str(grid[l]) + k)
      else:
        print(str(grid[l]) + ' '.join(row))
  print("-------------------------------")
  with open("p_table2.csv", newline='') as csvfile:
    print("   1  2  3  4  5  6  7  8  9  10")
    h = csv.reader(csvfile)
    l = 0
    for row in h:
      l = l + 1
      if "@" or "x" or "m" in row:
        k = ""
        for j in row:
          if j == "@":
            k = k + " 🚢"
          elif j == "x":
            k = k + " 🔥"
          elif j == "m":
            k = k + " ⚪"
          else:
            k = k + " 🌊"
        print(str(grid[l]) + k)
      else:
        print(str(grid[l]) + ' '.join(row))
  s(1)
  print()
  ask = input("Enter co-ordinates To Shoot at: ")
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
  while True:
    a1 = r(0, 9)
    a2 = r(0, 9)
    shot = a1, a2
    if shot not in shot_at:
      if p_map[a1][a2] == "@":
        p_map[a1][a2] = "x"
        aiwins += 1
        break
      else:
        p_map[a1][a2] = "m"
        break

  if ai_map[r1][r2] == "@":
    ai_map[r1][r2] = "x"
    pwins += 1
  else:
    ai_map[r1][r2] = "m"

  if pwins == 17:
    print("Player wins.")
    break
  elif aiwins == 17:
    print("Ai wins")
    break
  else:
    clear()
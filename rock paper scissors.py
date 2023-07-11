import os,time
from getpass import getpass as input
p1_counter=0
p2_counter=0
def clean():
  time.sleep(2)
  os.system('cls')
while True:
  print("\033[35m","==EPIC ROCK, PAPER,SCISSORS BATTLE==","\033[0m")
  print("Select your move(R, P or S)")
  player1= input("player 1 >")
  player2=input("Player 2 >")
  u1=player1.upper()
  u2=player2.upper()
  #if you know a faster way of doing this please help me out 
  if u1=="R" and u2=="P":
   print(" you are on fire player 2")
   p2_counter+=1
   clean()
  elif  u1=="P" and u2=="P":
   print("draw") 
   clean()
  elif  u1=="P" and u2=="R":
   print(" you are on fire player 1")
   p1_counter+=1
   clean()
  elif  u1=="P" and u2=="S":
   print(" you are on fire player 2")
   p2_counter+=1
   clean()
  elif  u1=="S" and u2=="S":
   print("DRAW")
   clean()
  elif  u1=="S" and u2=="P": 
   print(" you are on fire player 1")
   p1_counter+=1
   clean()
  elif  u1=="S" and u2=="R": 
   print(" you are on fire player 2")
   p2_counter+=1
   clean()
  elif  u1=="R" and u2=="S": 
   print(" you are on fire player 1")
   p1_counter+=1
   clean()
  elif  u1=="S" and u2=="P":
   print(" you are on fire player 1")
   p1_counter+=1
   clean()
  elif  u1=="R" and u2=="R": 
   print("DRAW")
   clean()
  if p1_counter==3:
    print(f"player 1 wins {p1_counter} : {p2_counter}")
    clean()
    p1_counter-= p1_counter
    p2_counter-=p2_counter
  if p2_counter==3:
    print(f"player 2 wins {p2_counter} : {p1_counter}")
    clean()
    p1_counter-= p1_counter
    p2_counter-=p2_counter
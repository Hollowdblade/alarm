import random,os,time
words=["Elephant" ,"Sunshine", "Enigma","Bicycle","Serendipity","Galaxy","Chocolate","Rainbow","Harmony","Anaconda"]
def clear():
  time.sleep(2)
  os.system("cls")
def gameplay(my_word ,play):
  position=0
  for char in my_word:
    if char!=play:
      position+=1
    if char== play:
      list[position]= char
      position+=1
  word= "".join(list)
  return word.capitalize()
while True:
  score=6
  choice=random.choice(words)
  my_word = choice.lower()
  list=[]
  for i in range(len(my_word)):
    list.append("_ ")
  while score>0:
    play=input("Choose a letter > ").lower()
    clear()
    if play not in my_word:
      print("nope, not in there")
      score-=1
      print(f"you have {score} lives left")
      clear()
      if score==0:
        print("OH NO!! you have died")
        break
    if play in my_word:
      print (gameplay(my_word,play))
      clear()
      if gameplay(my_word,play)== choice.capitalize():
        print(f"You have won with {score} lives")
        break
  
  print("Try again [Yes/No]? :")
  again= input().strip()
  if again.capitalize() == "Yes":
    clear()
    continue
  else:
    clear()
    break
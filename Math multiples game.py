import os,time
counter=0
while True:
    print("MATH GAME")
    print()
    TT=int(input("Name your multiples: "))
    for i in range(1,11,1):
        print(TT,"X",i)
        mp=int(input("> "))
        answer=TT*i
        if mp== answer:
            print("awesone work!!")
            counter+=1
            time.sleep(1)
            os.system('cls')
        else:
            print(f"sorry the answer was{answer}")
            time.sleep(1)
            os.system('cls')
    print(f"You scored {counter} out of 10")
    counter-=counter
    time.sleep(2)
    os.system('cls')
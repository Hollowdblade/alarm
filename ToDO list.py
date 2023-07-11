import os,time
td=[]
def items():
    for i in td:
        print(i)
while True:
    print("""ToDo list manager
          """)
    action=input("""Do you want to view, add, remove or edit the ToDo list:
""")
    lower= action.lower()
    if lower=="view":
        items()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    if lower=="add":
        d=input("""what would you like to add?:
""")
        if d in td:
            print("item already in list")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            td.append(d)
            os.system('cls' if os.name == 'nt' else 'clear')
    if lower=="remove":
        r=input("""what do you want to remove?:
""")
        r2=input(f"""are you sure you want to remove {r} ?:
""")
        r3=r2.lower()
        if r3=="yes":
            td.remove(r)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("okeyyy")
    if lower=="edit":
        items()
        print()
        c= input("""what do you want to change?:
""") 
        td.remove(c)
        cp= input("""what do you want to change it to?:
""")
        td.append(cp)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        continue
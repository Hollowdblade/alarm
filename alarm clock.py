import datetime,time,winsound
ahour=int(input("hour: "))
min=int(input("minute: "))
time=input("am/pm : ")
while True:
    if time=="pm" or time=="Pm" or time=="PM":
        ahour+=12
    if ahour==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        for i in range(1,5):
            winsound.PlaySound("SystemExit",winsound.SND_ALIAS)
            i+=1
        break
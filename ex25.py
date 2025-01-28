totalTail=0
totalHead=0
while True:
    a=str(input("enter th ail or head"))
    if a=="head":
        totalHead=totalHead+1
    elif a=="tail":
        totalTail=totalTail+1
    elif a=="stop":
        break
print(totalHead)
print(totalTail)
per=100*(totalHead/totalHead+totalTail)
print("head= "+str(per)+"%")
print("tail= "+str(100*(totalTail/totalHead+totalTail))+"%")
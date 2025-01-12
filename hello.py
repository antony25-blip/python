geometry =int(input("enter the mark of geometry: "))
algebra =int(input("enter the mark of algebra: "))
physics =int(input("enter the mark of physics: "))

total =physics+geometry+algebra
avg=total/3
if avg>=7:
    print("good job!")
elif 4<=avg<=6:
    print("you need to work hard")
else:
    print("failed,you really need to hard work")
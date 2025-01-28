duration=int(input("enter the duration: "))
if 1<=duration<=500:
    totalCost=25+(duration*0.01)
elif 501<=duration<=800:
    totalCost=25+(500*0.01)+((duration-500)*0.008)
elif duration>=801:
    totalCost=25+(500*0.01)+(300*0.008)+((duration-800)*0.005)
print(totalCost)

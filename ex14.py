costOfproduct=int(input("enter the product cost: "))
location=str(input("enter the location: "))
if location=="us":
    totalCost=costOfproduct+5
elif location=="Europe":
    totalCost=costOfproduct+7
elif location=="canada":
    totalCost=costOfproduct+3
else:
    totalCost=costOfproduct+9
print("total cost: "+str(totalCost))
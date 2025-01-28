totalMoney= float(input("enter the total money you have: "))
Bitcoin= float(input("enter Bitcoin value: "))
Ethereum= float(input("enter Ethereum value: "))
Litecoin= float(input("enter Litecoin value: "))
noOfbitcoin=totalMoney/Bitcoin
noOfethereum=totalMoney/Ethereum
noOflitecoin=totalMoney/Litecoin
print("With"+str(totalMoney)+"you can buy: "+str(noOfbitcoin)+"Bitcoins,"+str(noOfethereum)+"Ethereums, and"+str(noOflitecoin)+"litecoins")
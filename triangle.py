n=int(input("enter the num:"))
a="*"
for i in range(1,n):
    for j in range(1,n,2):
            print(a*j,end=" ")
    print("\n")
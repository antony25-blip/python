r=int(input("enter the row: "))
c=int(input("enter the coloumn: "))
mat=[]
print("enter the elements: ")
for i in range(0,r):
    a=[]
    for j in range(0,c):
        a.append(int(input()))
    mat.append(a)
print("---MATRIX")
for i in range(0,r):
    for j in range(0,c):
        print(mat[i][j],end="\t")
    print()
minrow=0
maxrow=r
mincol=0
maxcol=c
ar=[]
while(len(mat)<r*c):
    if len(mat)<r*c:
        for i in range(mincol,maxcol):
            ar.append(mat[minrow][i])
        minrow+=1
    if len(mat)<r*c:
        for i in range(minrow,maxrow):
            ar.append(mat[i][maxcol-1])
        maxcol-=1
    if len(mat)<r*c:
        for i in range(maxcol-1,mincol-1,-1):
            ar.append(mat[maxrow-1][i])
        maxrow-=1
    if len(mat)<r*c:
        for i in range(maxrow-1,minrow-1,-1):
            ar.append(mat[i][mincol])
        mincol+=1
return(ar)
A=[75689853, -1973594324, -2038664370, -184803526, 142426898]
maxsum=-1            
l=0
m=[]
ar=[]
sums=0 
for i in range(len(A)):
    if A[i]>=0:                
        sums=sums+A[i]
        ar.append(A[i])
    else:
        if sums>maxsum:
            maxsum=sums                        
            m=ar[:]
        elif sums==maxsum and len(ar)>len(m):
            maxsum=sums
            m=ar[:]
        ar.clear()
        sums=0    
if sums>maxsum:
    maxsum=sums                        
    m=ar[:]
elif sums==maxsum and len(ar)>len(m):
    maxsum=sums
    m=ar[:]                
print(m)
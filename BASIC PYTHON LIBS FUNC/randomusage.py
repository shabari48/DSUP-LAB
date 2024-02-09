from numpy import random
import random as rm

#implementation of loops,control flow and function

def setmat(mat):
    for i in range(6):
        for j in range(10):
            if(j%2==0):
                mat[i][j]=rm.randrange(1,49)
            else: 
                mat[i][j]=rm.randrange(50,99)
    return mat

# 10 x 6 matrix 
mat=[[0]*10]*6
mat=setmat(mat)
print(*mat,sep="\n",end="\n")
print()

x=random.randint(100,size=(10,6))
print(x)
print()

y=random.rand(10,6)
print(y)
print()

x=lambda a,b: a**b

print(x(random.randint(3,5),2))


from numpy import random
import numpy as np
import statistics


#REPLACE WITH MEAN VALUES
y=random.randint(7,size=(10,6)) #create a 2d array of size 10 x 6. Range 0 to 7

print("MEAN")
for i in range(10):
 x=statistics.mean(y[i]) #find mean of each row
 print(x,end=" ")
 for j in range(6):
     if y[i][j]==0:  #if array value is 0 . fill with row mean that is x
         y[i][j]=x
print()        
print(y)

#REPLACE WITH MEDIAN VALUES

y=random.randint(7,size=(10,6)) #create a 2d array of size 10 x 6. Range 0 to 7

print("MEDIAN")

for i in range(10):
 x=statistics.median(y[i]) #find median of each row
 print(x,end=" ")
 for j in range(6):
     if y[i][j]==0:  #if array value is 0 . fill with row median that is x
         y[i][j]=x
print() 
print(y)
print() 

#REPLACE WITH MODE VALUES

names = ['Shabari','Shaye','Keer','Sak','Pavi', 'Amir','Gokul',""]

namearray=np.empty((5, 5),dtype='U10')

for i in range(5):
    for j in range(5):
        namearray[i][j]=random.choice(names)
        
print()      
print(namearray)

print("MODE")

for i in range(5):
    x=statistics.mode(namearray[i]) #mode gives the frequently used value in a row
    print(x,end=" ")
    for j in range(5):
     if namearray[i][j]==""  and x!="":
            namearray[i][j]=x
print()    
print(namearray)


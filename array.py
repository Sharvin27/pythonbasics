from array import *

vals=array('i',[0,1,2,3])                             #integer arrays
for i in range(len(vals)):  
    print (vals[i])

char=array('u',['s','h','r','g'])                     #unicode arrays
for e in char:
    print(e)

newArr=array(vals.typecode,(a for a in vals))         #Copying the elements of array
for e in vals:
    print(e)

arr=array('i',[])                                       #user input arrays
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("Enter elements"))
    arr.append(x)

for e in arr:
    print(e)

val=int(input("Enter the number for search: "))         #finding index of no 
k=0
for e in arr:                                           #manually
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val))                                   #function
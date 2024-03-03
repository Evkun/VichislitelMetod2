import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
filename = "C:\\Users\\User\\Downloads\\03_Владивосток.xlsx"
data = pd.read_excel(filename)
array = data.values
global x3, y3

x3=[]
y3=[]
a=10

i=a
while len(x3)<6:
#for i in range(a, b+1):
    if array[i][6]!=999.9:
        x3+=[array[i][0]]
        y3+=[array[i][6]]
    else: print("нет информации в год",array[i][0], "Выберете другой промежуток времени.")
    i+=1
    
print(x3)
print(y3)
def dy0_n(y, n):
    if n==0: return y[0]
    dy=[ [0 for i in range(n)] for j in range(n)]
    dy[0]=[(y[i+1]- y[i]) for i in range(n)]
    for i in range(1, n):
        dy[i]=[dy[i-1][j+1] - dy[i-1][j] for j in range(n-i)]
    #return dy[n-1][0]
    return float(dy[n-1][0])

for i in range(6):
   print(dy0_n(y3, i))
def fact(n):
    l=1
    for i in range(1, n+1):
        l*=i
    return l   
def li3(i, a):
    l=dy0_n(y3, i)/fact(i)
    q=a-x3[0]
    for j in range(i):
        l*=q-j
    return l
def L3(x):
    m=[li3(i, x) for i in range(len(y3))]
    s=0
    for elem in m:
        s+=elem
        #print(elem)
    return s
x1=np.arange(min(x3),max(x3)+0.1, 0.1)
y1=np.array([L3(elem) for elem in x1])
plt.plot(x1, y1)
plt.plot(x3[:len(x3)], y3[:len(x3)], 'ro')


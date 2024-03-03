import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
filename = "C:\\Users\\User\\Downloads\\03_Владивосток.xlsx"
data = pd.read_excel(filename)
array = data.values
global x4, y4

x4=[]
y4=[]
a=16

i=a
while len(x4)<6:
#for i in range(a, b+1):
    if array[i][6]!=999.9:
        x4+=[array[i][0]]
        y4+=[array[i][6]]
    else: print("нет информации в год", array[i][0], "Выберете другой промежуток времени.")
    i+=1
print(x4)
print(y4)
def dyn_n(y, n):
    if n==0: return y[5]
    #dy=[ [0 for i in range(6)] for j in range(6)]
    dy=[[(y[i+1]- y[i]) for i in range(5)]]
    for i in range(1, 6):
        dy+=[[dy[i-1][j+1] - dy[i-1][j] for j in range(5-i)]]
    #return dy[n-1][0]
    return float(dy[n-1][5-n])

for i in range(6):
   print(dyn_n(y4, i))
def fact(n):
    l=1
    for i in range(1, n+1):
        l*=i
    return l 
def li4(i, a):
    l=dyn_n(y4, i)/fact(i)
    q=a-x4[5]
    for j in range(i):
        l*=q+j
    return l
def L4(x):
    m=[li4(i, x) for i in range(len(y4))]
    s=0
    for elem in m:
        s+=elem
    return s
x1=np.arange(min(x4),max(x4)+0.1, 0.1)
y1=L4(x1)
plt.plot(x1, y1)
plt.plot(x4[:len(x4)], y4[:len(x4)], 'ro')
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
filename = "C:\\Users\\User\\Downloads\\03_Владивосток.xlsx"
data = pd.read_excel(filename)
array = data.values
global x5, y5

x5=[]
y5=[]
a=1

i=a
y5=[elem[6] for elem in array if elem[6]!=999.9]
x5=[elem[0] for elem in array if elem[6]!=999.9]

print(x5)
print(y5)
print(len(x5), len(y5))
def sum_pow(x, p):
    s=0
    for elem in x:
        s+=elem**p
    return s
def sum2_pow(x, y, p):
    s=0
    for i in range(len(x)):
        s+=y[i]*x[i]**p
    return s
m=10
A=np.array([[sum_pow(x5, i+j) for i in range(m) ] for j in range(m)])
B=np.array([ sum2_pow(x5, y5, i) for i in range(m) ])
X=np.linalg.solve(A, B)
print(X)

global coef
coef=X
def f(x):
    t=[coef[i]*x**i for i in range(len(coef))]
    s=0
    for elem in t:
        s+=elem
    return s
x1=np.linspace(min(x5),max(x5), 9999)
y1=f(x1)
plt.plot(x1, y1)
plt.plot(x5[:len(x5)], y5[:len(x5)], 'r')

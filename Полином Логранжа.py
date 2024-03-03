import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# Замените 'your_file.xlsm' на путь к вашему файлу Excel
filename = "C:\\Users\\User\\Downloads\\03_Владивосток.xlsx"

# Читаем данные из Excel файла
data = pd.read_excel(filename)

# Преобразуем данные в двумерный массив numpy
array = data.values
global x2, y2

x2=[]
y2=[]
a=1

i=a
while len(x2)<13:
#for i in range(a, b+1):
    if array[i][6]!=999.9:
        x2+=[array[i][0]]
        y2+=[array[i][6]]
    i+=1
print(x2)
print(y2)

def li2(i, a):
    l=1
    for j in range(len(y2)):
        if i!=j:
            l*=(a-x2[j])/(x2[i]-x2[j])
    return l
def L2(x1):
    m=[y2[i]*li2(i, x1) for i in range(len(y2))]
    s=0
    for elem in m:
        s+=elem
    return s

    
x1=np.arange(min(x2),max(x2)-0.9, 0.1)
y1=L2(x1)
plt.plot(x1, y1)
plt.plot(x2[:len(x2)-1], y2[:len(x2)-1], 'ro')
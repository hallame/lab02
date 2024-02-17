#!/usr/bin/env python
# coding: utf-8

# In[5]:


from math import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

n = 3.5
s = 11.5
fi=pi*3/4 #угол движения


# In[6]:


def f(tetha, r): #уравнение катера
    dr=r/sqrt(n**2 - 1)
    return dr

def f2(t): #лодка браконьеров
    xt = tan(fi+pi)*t
    return xt


# In[7]:


r0=s/(n+1) #первый случай

#решение диф уравнения для катера
tetha = np.arange(0, 2*pi, 0.01)
r = odeint(f, r0, tetha)

#вычисление траектории лодки
t=np.arange(0.00000000000001, 20)
r1=np.sqrt(t**2 + f2(t)**2)
tetha1=np.arctan(f2(t)/t)

plot.rcParams["figure.figsize"] = (10, 10)


plot.polar(tetha, r, 'red', label = 'катер')
plot.polar(tetha1, r1, 'green', label = 'лодка')

#вычисление точки пересечения
tmp=0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp=i
print("Тета:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))

plot.legend()
plot.savefig("01.png",dpi=100)


# In[8]:


r0=s/(n-1) #второй случай

#решение диф уравнения для катера
tetha = np.arange(0, 2*pi, 0.01)
r = odeint(f, r0, tetha)

#вычисление траектории лодки
t=np.arange(0.00000000000001, 20)
r1=np.sqrt(t**2 + f2(t)**2)
tetha1=np.arctan(f2(t)/t)

plot.rcParams["figure.figsize"] = (8, 8)


plot.polar(tetha, r, 'red', label = 'катер')
plot.polar(tetha1, r1, 'green', label = 'лодка')

#вычисление точки пересечения
tmp=0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp=i
print("Тета:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))

plot.legend()
plot.savefig("02.png",dpi=100)


# In[ ]:





# In[ ]:





# In[ ]:





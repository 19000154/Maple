import numpy as np
import matplotlib.pyplot as plt
from sympy import *

l=6
h=0.12
E=2.1*(10**5)
q=1.34*(10**(-2))

n=input("Введите n: ")
n=int(n)
arr1 = [None] * (n)
for i in range (n):
    arr1[i]=i

arr2 = [None] * (n)

for i in range (1, n+1):
  #if i%2 == 0:  
    N=int(i)
    print(' ')
    p=symbols('p')
    x=symbols('x')
    W0=symbols('W0')
    summ=W0*sin(p*x/l)
    W = [None] * (N)
    Args = [None] * (N)
    W[0] = W0
    Args[0] = sin(p*x/l)

    for i in range (2, N+1):
        index=str(i-1)
        Wi=symbols('W'+index)
        W[i-1]=Wi
        Args[i-1]=sin(i*p*x/(l))
        summ=summ+W[i-1]*(i)*sin(i*p*x/(l))
        #sum=sum+Wi*(i)
        type(summ)
    print("W =",summ,'\n')
    d1=diff(summ,x)
    d2=diff(d1,x)
 
    dd=d2*d2
    I1 = integrate(dd,(x,0,l))
    
    #Подстановка пи в p
    I1=I1.subs(p,pi)
   
    E1=I1*E*h**3/24

    E2 = integrate(summ,(x,0,l))
    E2 = E2.subs(p,pi)
    E2 = E2*q
    Es = E1 - E2
    
    print('Функционал энергии деформации: \n Es = ', Es , '\n Поиск минимума Es:')
    res = [None] * N
    for i in range(N):
        res[i] = diff(Es,W[i])
        print('по W',i ,'   ', diff(Es,W[i]))

        
    print('\n Поиск минимума Es:')
    Wres = [None] * N
    for i in range(N):
        Wres[i] = solve(res[i],W[i])
        print('W',i ,'=', Wres[i])
    
    Wr=list(np.array(Wres, dtype = 'float'))
    Wx = Wr[0]
    for i in range (N):
        Wx = Wx+Wr[i]*sin(i*pi/l)

        
    print('\n Wx:')
    print('Wx=', Wx)
    arr2[i]=Wx
  #else:i=i+1
    
plt.plot(arr1,arr2)
plt.show()

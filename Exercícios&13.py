from math import sin
from math import log as ln

h= 0.25
def func9(x, fx): return fx * x**2 - fx
def funcy13(z, fz): return fz ** 2 - 2*fz*z
def funcz13(x, fz, fx): return x * fz + fz ** 2 * sin(fx)
def interpol(x, fx):
    print('        ', end='')
    d=[i for i in range(len(fx))]
    d[0]=[i for i in fx]
    for i in range(len(d)-1):
        d[i+1]=[(d[i][j+1]-d[i][j])/(x[j+i+1]-x[j]) for j in range(len(d[i])-1)]
    print("P(x)=", end='')
    for i in range(len(x)-1):
        print(d[i][0], "+ (", end='')
        print(chr(92), end='')
        print("x -", x[i], ")*(", end='')
    print(d[len(d)-1][0], end='')
    for i in range(len(x)): print(')', end='')
    print('')
    print('')

print("Atividade 9")
for p in range(2):
    if(p): print("(d) Euler:")
    else: print("(b) Euler:")
    y, N, x=[1], int(1/h), [0]
    for i in range(N): 
        y.append(y[i]+h*func9(i/N, y[i]))
        x.append((i/N)+h)
    for i in range(int(N/2)): print('        y', 2*i,"= ", y[2*i], 'y', 2*i+1,"= ", y[2*i+1])
    print('        y',N,"= ", y[N])
    interpol(x, y)

    
    print("    Runge Kutta:")
    y=[1]
    for i in range (N): 
        k,t=[0],0
        for j in range (4):
            k.append(func9(i/N+t*h/2, y[i]+t*h*k[j]/2))
            t=1
        y.append(y[i]+h*(k[1]+2*(k[2]+k[3])+k[4])/6)
    #for i in range(N): y.append(y[i]+h*func9(i/N, y[i]))
    for i in range(int(N/2)): print('        y', 2*i,"= ", y[2*i], 'y', 2*i+1,"= ", y[2*i+1])
    print('        y',N,"= ", y[N])
    h=0.1
    interpol(x, y)

#interpolação


print("")
print("Atividade 13")
print("(a) Método de Euler:")
y, z, h = [1], [-1], .2
N=int(.4/h)
for i in range(N): 
    y.append(y[i]+h*funcy13(.4*i/N, y[i]))
    z.append(z[i]+h*funcz13(.4*i/N, y[i], z[i]))
for i in range(N+1): print('        y', i,"= ", y[i], 'z', i,"= ", z[i])
print("(a) Método de Nystrom:")
y, z= [1], [-1]
for i in range(N):
    k,l, t=[0],[0],0
    for j in range (3):
        k.append(funcy13(i/N+2*t*h/3, y[i]+2*t*h*k[j]/3))
        l.append(funcz13(i/N+2*t*h/3, y[i]+2*t*h*l[j]/3, z[i]+2*t*h*l[j]/3))
        t=1
    y.append(y[i]+h*(k[1]+3*(k[2]+k[3])/2)/4)
    z.append(z[i]+h*(l[1]+3*(l[2]+l[3])/2)/4)
for i in range(N+1): print('        y', i,"= ", y[i], 'z', i,"= ", z[i])

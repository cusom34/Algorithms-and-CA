#средние квадраты 

def f1(x): 
    x = x**2
    x = str(x)
    if (len(x)%2!=0):
        x="0"+x
    y=str(int(x[2:len(x)-2]))
    return int(y)*10**(4-len(y))

#print(f1(7350))
    
def f2(x1,x2):
    x = str(x1*x2)
    if (len(x)%2!=0):
        x="0"+x
    y=str(int(x[2:len(x)-2]))
    return int(y)*10**(4-len(y))

#print(f2(4004, 9494))
def f3(x):
    x=str(x)
    
    t=int(len(x)/4)
    a=x[t:]+x[:t]
    b=x[-t:]+x[:-t]
    c = str(int(a) + int(b))
    if len(c) > 4:
        c = c[0:4]
    y=str(int(c))
    return int(y)*10**(4-len(y))
"""
c = 5379
b = 7931
mass=[]
mass += [b]

for i in range(1,128):
    c=f2(c,mass[i-1])
    mass += [c]
    print(i,c)

print ('######################')
"""

c = 5379
b = 7931
mass=[]

for i in range(128):
    if c%3==0:
        c=f1(c)
        mass += [c]
        print(i,("0."+str(c)))
    elif c%3==1:
        c = f3(c)
        mass += [c]
        print(i,("0."+str(c)))
    else:
        c = f2(c, mass[i - 1])
        mass += [c]
        print(i,("0."+str(c)))

n=len(mass)
m=0
for elem in mass:
    m+=elem*0.0001
m/=n
print("m    =", m)

d=0
for elem in mass:
    d+=(elem*0.0001-m)**2
d/=n
print("D    =", d)
print("sigma=", d**0.5)
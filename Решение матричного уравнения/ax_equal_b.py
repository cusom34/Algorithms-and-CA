import time

def mult(z, b):
    if len(z)!=len(b[0]): 
        print(z)
        print(b)
        print("error")
        return -1
    k=min(len(z), len(b))

    c=[[0 for i in range(len(b[0]))] for i in range(len(z))]
    for i in range(len(c)):
        for j in range(len(c[0])):
            for t in range(k):
                c[i][j]+=z[i][t]*b[t][j]
    return c

def proizv_mass_chislo(a, b):
    c=a[:]
    for i in range(len(c)):
        c[i]*=b
    return c
    
def differ(a, b):
    c=a[:]
    for i in range(len(c)):
        c[i]-=b[i]
    return c

def reverse(pop):
    b=pop[:]

    if (len(b)!=len(b[0])):
        print("матрица прямоугольная, обратной не существует", len(b), len(b[0]))
        for elem in b:
            print(elem)
        return False
    
    l=len(b)

    #расширение единичной матрицей
    a=[[0 for i in range(l)] for i in range(l)]
    for i in range(len(b)):
        a[i][i]=1
    for i in range(len(a)):
        a[i]=b[i]+a[i]

    #ниже главной диагонали
    for i in range(l):
        for j in range(i+1, l):
            a[j]=differ(a[j], proizv_mass_chislo(a[i], a[j][i]/a[i][i]))
            #print("    ", j, a[j])
        #print(i, "a=", a)
    #print(a)
    for i in range(l):
        for j in range(i+1, l+l):
            a[i][j]=a[i][j]/a[i][i]
        a[i][i]=1

    #print("\n", a, "\n")

    #выше главной диагонали
    for i in range(l-1, -1, -1):
        for j in range(i-1, -1, -1):
            a[j]=differ(a[j], proizv_mass_chislo(a[i], a[j][i]/a[i][i]))
    for i in range(l):
        for j in range(i+1, l+l):
            a[i][j]=a[i][j]/a[i][i]
        a[i][i]=1

    c=[[0 for i in range(l)] for i in range(l)]
    for i in range(l):
        for j in range(l):
            c[i][j]=a[i][l+j]
    
    return c

def minor(a, ia, ja):
    n=len(a)
    b=[]
    for i in range(n):
        if i!=ia:
            c=[]
            for j in range(n):
                if j!=ja:
                    c+=[a[i][j]]
            b+=[c]
    return b

def det(b):
    a=b[:]
    n=len(a)

    if (len(a)==2):
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    s=0
    for i in range(n):
        s+=det(minor(a, 0, i))*(-1)**i*b[0][i]
    return s
   
def rev_min(b):
    d = det(b)
    n = len(b)
    a=[[0 for i in range(n)]  for i in range(n)]
    for i in range (n):
        for j in range(n):
             a[i][j]+=b[j][i] 
   
    c =[[0 for i in range(n)]  for i in range(n)]
     
    for i in range (n):
        for j in range(n):
             c[i][j] += det(minor(a,i,j))/d*(-1)**(i+j)
    
    return c


"""
k=[[1, 2, 4], [6, 8, 5], [2, 4, 4]]
A=[[2, 8, 8], [2, 8, 8], [2, 8, 8]]
A=[[1, 2, 3], [4, 5, 6], [7, 89, 9]]
B=[[4, 8, 7], [6, 2, 3], [6, 2, 5]]

"""            
a=[[1, 2, -4],
   [0, 0.5, 3],
   [0, 0, 2]]

b=[[1, 1, -1],
   [2, 1, 0],
   [1, -1, 1]]

    
tic = time.perf_counter()
if (det(a)==0):
    print("детерминант A 0, решений нет")
else:
    print(reverse(a), "\n")
    print(mult(reverse(a),b))
toc = time.perf_counter()

print(f"Вычисление заняло {toc - tic:0.4f} секунд")

tic = time.perf_counter()
if (det(a)==0):
    print("детерминант A 0, решений нет")
else:
    print(rev_min(a), "\n")
    print(mult(rev_min(a),b))
toc = time.perf_counter()

print(f"Вычисление заняло {toc - tic:0.4f} секунд")

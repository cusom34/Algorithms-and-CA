def det(a):
    if (len(a)==len(a[1])==2):
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]

def revers(a):
    d=det(a)
    b=[[0 for i in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[len(a)-j-1][len(a)-i-1]=1/d*(-1)**(i+j)*a[i][j]
    return b


def mult(a, b):
    if len(a)!=len(b[0]): 
        print("errorr")
        return -1
    k=len(a[1])
    c=[[0 for i in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c[0])):
            for z in range(k):
                c[i][j]+=a[i][z]*b[z][j]
    return c
            
a=[[3, 7], 
   [2, 8]]

b=[[4, 8], 
   [6, 2]]

if (det(a)==0):
    print("детерминант 0")
else:
    print(revers(a))
    print(mult(revers(a),b))
    
    
"""
def reverse(a):
    l=len(a)
    b=[[0 for i in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(b)):
        b[i][i]=1
    for i in range(len(a)):
        a[i]+=b[i]
    for i in range(l):
        for j in range(i, len(a[i])):
            deli = a[j][i]
"""         
            
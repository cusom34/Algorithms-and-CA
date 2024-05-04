import time

def summ(m1, m2):
    m1i, m2i=0, 0
    ans=[]
    while len(ans)<len(m1)+len(m2):
        if m1i<len(m1) and m2i<len(m2):
            ans+=[min(m1[m1i], m2[m2i])]
            if m1[m1i] < m2[m2i]:
                m1i+=1
            else: m2i+=1
        elif m1i<len(m1):
            ans+=m1[m1i:]
        else:
            ans+=m2[m2i:]
    return ans

def qsort(mass):
    n=len(mass)
    if n==1:
        return mass
    else:
        return summ(qsort(mass[n//2:]), qsort(mass[:n//2]))
    
    
tic = time.perf_counter()    
print(qsort([2, 4, 6, 1, 1 , 10, 15, 0, -2, -10]))
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.4f} секунд")
import sys
import timeit
sys.setrecursionlimit(1000000000)
a = [0] * 55_000


def rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        if a[n] != 0:
            rekursif(n-1) 
            return a[n]  
        else:
            hasil = rekursif(n-1) + rekursif(n-2) 
            a[n] = hasil
            return rekursif(n-1)+ rekursif(n-2)

for i in range(0,101, 1):
    if i == 0:
        continue
    awal= timeit.default_timer()
    print(rekursif(i))
    akhir= timeit.default_timer()
    print(f" Fibonacci data ke- {i} ", 'adalah : ' , akhir-awal ,  'second' ,  'bilangan Fibonacci ke', rekursif(i))




import numpy as np
import timeit

def fibonaci_iteratif(n):
    let_a =[1,1]
    for i in range(2,n,1):
        let_a.append(let_a[i-2] + let_a[i-1])
    return let_a[len(let_a)-1]



for i in range (1, 101):
    start = timeit.default_timer()
    k = fibonaci_iteratif(i)
    end = timeit.default_timer()
    print(f'Fibonacci data ke-', i, 'adalah : ', start-end,'second' , ' bilangan Fibonacci ke', k)
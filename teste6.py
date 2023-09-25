N1=int(input("digite um numero"))
N2=int(input("digite um numero"))
for N1 in range (N1, N2, 1):
    N1 += 1
    if N1 %2 ==0:
        print(N1,"este numero e par")
    else:
        print(N1,"este numero e impar")
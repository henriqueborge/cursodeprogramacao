N1=int(input("digite primeiro numero"))
N2=int(input("digite segundo numero"))
N3=int(input("digite terceiro numero"))
soma=0
for N1 in range(N1, N2, N3):
    soma += N1
    print(soma)
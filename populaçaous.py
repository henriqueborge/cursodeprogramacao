# Definição de variaveis
paisA=int(input("digite tamanho da população do pais A: "))
paisB=int(input("digite tamanho da população do pais B: "))
porcentagempaisA=float(input("digite taxa de crescimento do primeiro pais: "))
porcentagempaisB=float(input("digite taxa de crescimento do segundo pais: "))
tempo = 0
#laço de repetição e calculo
while paisB > paisA:
    populacaoA = paisA * porcentagempaisA
    populacaoB = paisB * porcentagempaisB
    paisA = populacaoA + paisA
    paisB = populacaoB + paisB
    tempo = tempo + 1
    
print("o pais A vai ultrapassar o pais B em",tempo,"anos")
paisA = 80000
paisB = 200000
tempo = 0
while paisB > paisA:
    populacaoA = paisA * 0.03
    populacaoB = paisB * 0.015
    paisA = populacaoA + paisA
    paisB = populacaoB + paisB
    tempo = tempo + 1

print("o pais A vai ultrapassar o pais B em",tempo,"anos")
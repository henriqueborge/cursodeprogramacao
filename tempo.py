tamanho_do_arquivo=int(input("digite tamanho do arquivo: "))
velocidade_da_internet=int(input("digite velocidade da internet: "))
tempo=(tamanho_do_arquivo * 8) / (velocidade_da_internet * 60)
print(tempo)
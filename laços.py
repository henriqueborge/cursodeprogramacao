while True:
    nota=float(input("digite uma nota: "))
    if nota >=0 and nota<=10:
        print(f"nota valida: {nota}")
        break
    else:
        print("nota não existe.")

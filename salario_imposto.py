N1=int(input("digite ganho por hora"))
N2=int(input("digite horas trabalhadas por mes"))
ir = 0.11
inss = 0.08
sindicato = 0.05
valor=N1*N2
imposto1=valor*ir
imposto2=valor*inss
imposto3=valor*sindicato
valor_liquido=(valor-imposto1-imposto2-imposto3)
print(f"valor: {valor}\n imposto IR: {imposto1}\n imposto INSS: {imposto2}\n imposto do sindicato: {imposto3}\n valor liquido: {valor_liquido}.")
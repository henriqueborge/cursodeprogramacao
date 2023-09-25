metros=int(input("digite metros"))
litros = metros/6
latas = litros/18
print(f"voce precisara de {latas} latas o valor sera de {latas*80} reais")

litros = metros/6
galao = litros/3.6
print(f"voce precisara de {galao} galões o valor sera de {galao*25} reais")

mlata = int(litros / 18.0)
mgalao = int((litros - (mlata * 18)) / 3.6)
if litros - (mlata * 18) % 3.6 != 0:
    mgalao += 1
    gtotal = (mlata * 80) + (mgalao * 25)
    print(f"ou então para mais economia use {mlata} lata e {mgalao} galões e custará R$ {gtotal}")

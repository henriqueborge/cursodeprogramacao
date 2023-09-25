produtos=["arroz","feijão","café","açucar","farinha","sal","oleo","bolacha","leite","sabonte"]
valores=[7,9,6.5,10,4.5,8.5,5,9,6,1.5]
imposto1= 12
imposto2= 6
imposto3= 3
frete= 50
for a in range (len(produtos)):
    produto = produtos[a]
    valor = valores[a]
    lucro = 60
    impostoa=((valor*imposto1)/100)
    impostob=((valor*imposto2)/100)
    impostoc=((valor*imposto3)/100)
    pc = (valor+impostoa+impostob+impostoc)
    ml = ((pc * lucro) /100)
    pv = pc+ml
    print(f"produto: {produto} valor: {valor} preço custo: {pc} preço venda: {pv}")
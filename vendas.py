produtos=["arroz","feijão","café","açucar","farinha","sal","oleo","bolacha","leite","sabonte"]
valores=[10,5.25,3,6,2.5,7,3.5,4.5,6.5,5.5,]
qtd=[10,10,10,10,10,10,10,10,10,10]
imposto1= 12
imposto2= 6
imposto3= 3
frete= 50
for a in range (len(produtos)):
    produto = produtos[a]
    valor = valores[a]
    quantidade = qtd[a]
    lucro = 0.60
    impostoa=((valor*imposto1)/100)
    impostob=((valor*imposto2)/100)
    impostoc=((valor*imposto3)/100)
    valorfrete=frete/quantidade
    pc = (valor+impostoa+impostob+impostoc+valorfrete)
    ml = pc * lucro
    pv = pc+ml
    print(f"produto: {produto}, quantidade {quantidade}, valor: {valor}, preço custo: {pc}, preço venda: {pv}.")
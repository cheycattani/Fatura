# Faça um programa para registrar uma venda. O programa vai receber do usuário o nome do produto e o preço e
# vai adicioná-lo à fatura. Em seguida, pergunte ao usuário se ele quer comprar mais algum produto.
# Se a respostar fo 's', repita a operação. Só pare quando a resposta for 'n' e então imprima a fatura,
# que deve conter os produtos comprados e os preços. Ao final deve apresentar o total da fatura.

# OBS: Para facilitar a resolução do exercício, considere que só é possível comprar uma unidade de cada produto por vez;

repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    fatura.append([produto, preco])
    total += preco
    repetir = input('Deseja comprar mais algum produto? (S ou N) ').lower()

for i in fatura:
    print(i[0], '-', i[1])

print('Total:', total)




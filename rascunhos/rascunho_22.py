#Atividade do Dikastis

produtos_vendidos = ['Kirby', 'Água', 'Pirulito', 'Dinossauro', 'Armário']
produto_estoque = ['Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Pirulito', 'Dinossauro', 'Dinossauro', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário']

entrada_um = input()
total_do_produto = 0

for i in produtos_vendidos:
    if entrada_um == i:
        print("Vendemos sim!")
        for a in produto_estoque:
            if entrada_um == a:
                total_do_produto += 1
    
print(f'Existe(m) {total_do_produto} {entrada_um}(s) em estoque!')


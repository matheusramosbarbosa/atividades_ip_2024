#Atividade do Dikastis

produtos_vendidos = ['Kirby', 'Água', 'Pirulito', 'Dinossauro', 'Armário']
produto_estoque = ['Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Água', 'Pirulito', 'Dinossauro', 'Dinossauro', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário', 'Armário', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby', 'Kirby']

total_do_produto = 0

for i in produtos_vendidos:
        total_do_produto = 0
        for a in produto_estoque:
            if i == a:
                total_do_produto += 1
        print(f'Existe(m) {total_do_produto} {i}(s) em estoque!')        
    
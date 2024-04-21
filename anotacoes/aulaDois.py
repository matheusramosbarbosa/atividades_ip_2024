print("olá, meu mundo <3") #no python não há distinção entre caractere e simbolo
#agora vamos utilizar uma variável para guardar a mensagem
# = é atribuição
mensagem = 'Python é massa!'
print(mensagem) #não vai imprimir o nome mensagem, vai imprimir o valor de dentro
print(mensagem)
print(mensagem)

#como traduzir algoritmo de portugol pra python?
x = input("Digite um número") #input é literalmente um input
y = (x * 2) # * é multiplicação
print(y)

#deu errado ???
#o programa fez a leitura de um texto, não de um número. ou seja, não fez a leitura do valor inteiro 2. ele leu o TEXTO "2". quando ele executou y = (x * 2), duplicou o texto "2", resultando no texto "22"

#para corrigir, vamos indicar que queremos ler um INTEIRO, através do comendo int()


#corrigindo
x = int(input("Digite um número")) #perceba que aqui coloquei o int para forçar que o input faça uma leitura e converta esse valor para um inteiro
y = (x * 2)
print(y)

#dá pra combinar textos usando o comando de concatenação (ligar-se) +

print('Programação' + 'com' + 'python')
print('Programação ' + 'com ' + 'Python') #com espaços agora

#Exercício! Criar um programa para armazenar o STRING 2+3 em uma varíavel / 2 - Armazenar o valor da operação numérica 2+3 em outra variável / 3. Imprimir o valor do string seguido pelo resultado numérico da operação na mesma linha

#vamos ver...

x = "2+3"
y = 2 + 3
print(x + "=" + str(y)) #fiz sozinho porraaaaaaaa
#pra transformar int em string tem que fazer str()

#correção do professor
var_string = '2+3:'
var_num = 2+3
print(var_string + str(var_num))

#Nomes de variáveis e funções
# - podem conter letras, dígitos e underscores(_)
# não pode iniciar com dígitos
#boas práticas: utilize nomes significativos, escreva todas as letras minúsculas, separar palavras com _ (comum em python), evitar preposições para separar palavras, evitar acentos e cedilha, não pode usar palavras reservadas

#palavras reservadas: and, as, assert, break, class, continue, def, del, elif, else, except, false, finally, for, from, global, if, import, in, is, lambda, none, nonlocal, not, or, pass, raise, return, true, try, while, with, yield, async, await

#desafio

nome = "Rui"
print("Olá, " + nome)
taxa_metabolica_rui = int(input('Ponha a taxa metabólica basal de Rui: '))
qtd_media_calorias = int(input('Ponha a quantidade média de calorias que Rui gasta quando faz alguma atividade física: '))
qtd_atividades_semana = int(input('Ponha a quantidade de vezes que Rui faz atividades físicas durante a semana: '))
qtd_meses_descanso = int(input('Ponha a quantidade de meses que Rui descansa durante um ano: '))

#Agora que Rui já sabe quantas calorias gasta e consome por ano, será que ele vai ganhar ou perder peso durante um ano?
#Vamos utilizar o comando if-else para decidir se ele irá ganhar ou perder peso

# if (condição):
#     comando1 IMPORTANTE
#     comando2 IMPORTANTE
# else:
#     comandoA IMPORTANTE
#     comandoB IMPORTANTE

# Esse é o nome de Rui, e a apresentação.
nome = "Rui"
print("Olá, " + nome + '!')

# Cálculos do gasto calórico
taxa_basal = int(input('Qual sua taxa metabólica? '))
qtd_calorias = int(input('Quantas calorias você gasta por atividade? '))
qtd_atividades = int(input('Qual a quantidade de vezes que você faz atividade física durante a semana? '))
qtd_descanso = int(input('Qual a quantidade de meses que você descansou durante um ano? '))
caloria_basal = taxa_basal * 7 * 4 * 12 #só não sabia essa bomba de taxa basal e caloria basal
caloria_atv_fisica = qtd_calorias * qtd_atividades * 4 * (12 - qtd_descanso)
calorias_gastas = caloria_basal + caloria_atv_fisica

# Impressão do relatório de gasto calórico
print(nome + ', realizamos o cálculo!')
print('Você gasta ' + str(calorias_gastas) + ' calorias por ano!')

# Cálculo do consumo calórico
qtd_calorias_ref = int(input("Qual a quantidade média de calorias que você consome por refeição?"))
qtd_ref_dia = int(input("Quantas refeições você faz por dia?"))
qtd_calorias_ano = qtd_ref_dia * qtd_calorias_ref * 7 * 4 * 12 

# Impressão do relatório de gasto calórico
print(nome + " , realizamos o cálculo de quantas calorias você consome em um ano.")
print("Você consome " + str(qtd_calorias_ano) + " calorias por ano!")

if(qtd_calorias_ano > calorias_gastas):
    print("Infelizmente, você não vai atingir seu objetivo.")
else:
    print("Parabéns, você está no caminho certo!")

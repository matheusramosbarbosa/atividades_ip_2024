# Atividade 1 da Lista 6

# Catálogo com as informações fornecidas
catalogo = [("Abbey Road", "The Beatles", 1969, "Rock"), ("The Dark Side of the Moon", "Pink Floyd", 1973, "Rock"), ("Riot!", "Paramore", 2007, "Rock"), ("Fearless", "Taylor Swift", 2008, "Pop"), ("Da Lama ao Caos", "Chico Science e Nação Zumbi", 1994, "Manguebeat"), ("Gal Costa", "Gal Costa", 1969, "MPB"), ("Sim", "Vanessa da Mata", 2007, "MPB"), ("As 20 Melhores", "Luiz Gonzaga", 2004, "Forró"), ("O Melhor de Dominguinhos", "Dominguinhos", 2013, "Forró"), ("Alucinação", "Belchior", 1976, "MPB"), ("Samba Esquema Novo", "Jorge Ben Jor", 1963, "Samba")]

# Função para adicionar álbum
def adicionar_album(catalogo, nome_album, nome_artista, ano_lancamento, genero_musical):
    generos_existentes = {album[3] for album in catalogo}
    novo_album = (nome_album, nome_artista, ano_lancamento, genero_musical)
    catalogo.append(novo_album)
    print(f"Este foi o novo álbum adicionado:\n- {nome_album} do/da artista/banda {nome_artista} lançado em {ano_lancamento}")
    
    # Verificar se o gênero musical é novo após adicionar o álbum
    if genero_musical not in generos_existentes:
        print("Oba, você adicionou um novo estilo musical ao catálogo!")
    return catalogo

# Função para consultar gênero
def consultar_genero(catalogo, genero_musical):
    albuns_encontrados = [album for album in catalogo if album[3] == genero_musical]
    if albuns_encontrados:
        print(f"Nessa galeria há {len(albuns_encontrados)} albuns de {genero_musical}. Os albuns encontrados foram:")
        for album in albuns_encontrados:
            print(f"- {album[0]} do/da artista/banda {album[1]} lançado em {album[2]}")
    else:
        print("Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!")

# Loop principal para receber comandos

consulta = True
while consulta:
    comando = input().strip()
    if comando == "FIM":
        consulta = False
    elif comando == "CONSULTAR":
        genero_musical = input().strip()
        consultar_genero(catalogo, genero_musical)
    else:
        nome_album = comando
        nome_artista = input().strip()
        ano_lancamento = int(input().strip())
        genero_musical = input().strip()
        catalogo = adicionar_album(catalogo, nome_album, nome_artista, ano_lancamento, genero_musical)
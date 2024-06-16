frase = "Olá, meu nome é Thomaz, meu pokémon preferido é Grumpig e tenho 3 pokébolas"

frase = frase.replace("Olá, meu nome é ", "")
print(frase)
frase = frase.replace(", meu pokémon preferido é ", " | ")
print(frase)
frase = frase.replace(" e tenho ", " | ")
print(frase)
frase = frase.replace(" pokébolas", "")
print(frase)
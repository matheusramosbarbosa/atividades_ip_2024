# Atividade 1 da Lista 5

entrada = input()
entrada = entrada.split(":")
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])
usuario = ''
password = ''

def login(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return (n * 2) + login(n-1)
        else:
            return (n * 3) + login(n-1)
        
def senha(n):
    if(n == 0):
        return 1
    else:
        return n * senha(n - 1)

    
for i in entrada:
    x = str(login(i))
    usuario += x

for i in entrada:
    x = str(senha(i))
    password += x

print(f'As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!')
print(f'Login: {usuario}')
print(f'Senha: {password}')
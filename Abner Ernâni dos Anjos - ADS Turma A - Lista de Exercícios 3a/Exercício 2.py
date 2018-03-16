print('Por favor, digite um usuário diferente da senha para ser logado com sucesso')
usuario= input('Usuário: ')
senha= input('Senha: ')
while senha == usuario:
    print('Usuário é igual a senha.')
    usuario= input('Usuário: ')
    senha= input('Senha: ')
if senha != usuario:
    print('Logado com sucesso')

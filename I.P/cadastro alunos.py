lista_alunos = []

def mostrar_nome(nome):
    print('Novo aluno cadastrado: ', nome)
    print(lista_alunos)
while True:
    nome_novo = input('Digite o nome: ')
    lista_alunos.append(nome_novo)
    mostrar_nome(nome_novo)
    cont = input('Quer continuar? (s/n): ')
    if cont.lower() == 'n':
        break
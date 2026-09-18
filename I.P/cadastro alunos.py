lista_alunos = []

def mostrar_nome(nome):
    print("\n--- Lista de Alunos Cadastrados  ---")
    for i, aluno in enumerate(lista_alunos, 1):
        print(f"{i}. {aluno}")
    print("---------------------------------\n")
while True:
    nome_novo = input('Digite o nome: ').strip()
    lista_alunos.append(nome_novo)
    mostrar_nome(nome_novo)
    cont = input('Quer continuar? (s/n): ')
    if cont.lower() == 'n':
        break
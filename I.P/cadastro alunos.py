lista_alunos = []

def mostrar_nome(nome):
    print("\n--- Lista de Alunos Cadastrados  ---")
    for i, aluno in enumerate(lista_alunos, 1):
        print(f"{i}. {aluno}")
    print("---------------------------------\n")
while True:
    print("=== MENU PRINCIPAL ===")
    print("1- Cadastrar aluno")
    print("2- Remover aluno")
    print("3- Sair")
    opcao = input("Escola a opção que você deseja: ").strip()
    if opcao == '1':
        while True:
            nome_novo = input('Digite o nome: ').strip()
            if not nome_novo:
                print('Texto Inválido, tente novamente')
                continue
            lista_alunos.append(nome_novo)
            mostrar_nome(nome_novo)
            cont = input('Quer continuar? (s/n): ')
            if cont.lower() == 'n':
                break
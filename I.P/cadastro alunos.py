lista_alunos = []

def mostrar_nome():
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
    elif opcao == '2':
        if not lista_alunos:
            print('\nA lista está vazia! Não há alunos para remover.\n')
        else:
        mostrar_nome()
        eliminar = input('Digite o aluno a remover: ').strip()
        if eliminar in lista_alunos:
            lista_alunos.remove(eliminar)
            print(f'{eliminar} foi removido com sucesso!')
        else:
            print('Aluno nâo encontrado.')
    elif opcao == '3':
        print('Saindo do Sistema.....')
        break
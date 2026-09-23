def salvar_txt():
    with open('alunos.txt', 'w', encoding='utf-8') as archivo:
        for aluno in lista_alunos:
            archivo.write(f"{aluno}\n")

def carregar_txt():
    lista = []
    try:
        with open('alunos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                lista.append(linea.strip())
    except FileNotFoundError:
        pass
    return lista

# Cargar los datos del archivo al iniciar el programa
lista_alunos = carregar_txt()

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
    print("0- Mostrar Lista")
    opcao = input("Escolha a opção que você deseja: ").strip()
    
    if opcao == '1':
        while True:
            nome_novo = input('Digite o nome: ').strip()
            if not nome_novo:
                print('Texto Inválido, tente novamente')
                continue
            lista_alunos.append(nome_novo)
            salvar_txt()
            mostrar_nome()
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
                salvar_txt()
                print(f'{eliminar} foi removido com sucesso!')
            else:
                print('Aluno não encontrado.')

    elif opcao == '3':
        print('Saindo do Sistema.....')
        break

    elif opcao == '0':
        if not lista_alunos:
            print('\nA lista está vazia!\n')
        else:
            mostrar_nome()

    else:
        print('Opção Inválida!')
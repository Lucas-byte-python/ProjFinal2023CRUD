import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="academia"
    )

# Função para inserir um novos registro pelo usuário
def inserir_valores(cursor, nome, data_nas, sexo):
    cursor.execute("INSERT INTO cadastro_crud (nome, data_nas, sexo) VALUES (%s, %s, %s)", (nome, data_nas,sexo))
    conexao.commit()

# Função para listar todos os usuários
def listar_valores(cursor):
    cursor.execute("SELECT * FROM cadastro_crud")
    return cursor.fetchall()

# Função para buscar um usuário pelo ID
def buscar_valores(cursor, id):
    cursor.execute("SELECT * FROM cadastro_crud WHERE id = %s", (id,))
    return cursor.fetchone()

# Função para atualizar um usuário pelo ID
def atualizar_valores(cursor, id, nome, data_nas, sexo):
    cursor.execute("UPDATE cadastro_crud SET nome = %s, data_nas = %s, sexo = %s WHERE id = %s", (nome, data_nas, sexo, id))
    conexao.commit()

# Função para deletar um usuário pelo ID
def deletar_valores(cursor, id):
    cursor.execute("DELETE FROM cadastro_crud WHERE id = %s", (id,))
    conexao.commit()

# Conectar ao banco de dados
conexao = conectar()
cursor = conexao.cursor()

while True:
    # Menu de opções
    print("Seja Bem-Vindo a Nossa Academia!")
    print("*" * 30)
    print("*" * 30)
    print("Escolha uma opção:")
    print("1 - Adicionar usuário:")
    print("2 - Deletar usuário:")
    print("3 - Ler registros:")
    print("4 - Atualizar registro:")
    print("5 - Finalizar Programa!")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":

        nome = input("Digite o nome do usuário: ")
        data_nasc = input("Digite a data de nascimento do usuário (F-AAAA/MM/DD): ")
        sexo = input("Digite o seu sexo: ")
        inserir_valores(cursor, nome, data_nasc, sexo)
        print("-" * 20)
        print("Registros adicionado com sucesso!")
        print("-" * 20)
        print("\n")


    elif opcao == "2":

        registros = listar_valores(cursor)
        print("\nLista de registros existente:")
        for registros in registros:
            print("-" * 20)
            print(registros)
            print("-" * 20)

        id = int(input("Digite o ID do usuário a ser deletado: "))
        deletar_valores(cursor, id)
        print("-" * 20)
        print("Usuário deletado com sucesso!")
        print("-" * 20)
        print("\n")


    elif opcao == "3":

        registros = listar_valores(cursor)
        print("\nLista de registros existente:")
        for registros in registros:
            print("-" * 20)
            print(registros)
            print("-" * 20)
            print("\n")

    elif opcao == "4":

        registros = listar_valores(cursor)
        print("\nLista de registros existente:")
        for registros in registros:
            print("-" * 20)
            print(registros)
            print("-" * 20)

        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        data_nasc = input("Digite a nova data de nascimento (F-AAAA/DD/MM): ")
        sexo = input("Digite o sexo: ")
        atualizar_valores(cursor, id, nome, data_nasc, sexo)
        print("-" * 20)
        print("Registros atualizado com sucesso!")
        print("-" * 20)
        print("\n")

    elif opcao == "5":
        break

    else:
        print("-" * 60)
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print("-" * 60)
        print("\n")

# Fechar cursor e conexão ao sair do programa
cursor.close()
conexao.close()
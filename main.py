from alunos import *

def main():
    while True:
        print("\n=== Sistema de Gerenciamento de Notas ===")
        print("1. Adicionar novo aluno")
        print("2. Adicionar nota a um aluno")
        print("3. Calcular média de um aluno")
        print("4. Verificar situação de um aluno")
        print("5. Exibir todos os alunos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula do aluno: ")
            adicionar_aluno(nome, matricula)

        elif opcao == '2':
            matricula = input("Matrícula do aluno: ")
            try:
                nota = float(input("Nota a ser adicionada: "))
                adicionar_nota(matricula, nota)
            except ValueError:
                print("Nota inválida. Digite um número.")

        elif opcao == '3':
            matricula = input("Matrícula do aluno: ")
            media = calcular_media(matricula)
            if media is not None:
                print(f"Média do aluno: {media:.2f}")

        elif opcao == '4':
            matricula = input("Matrícula do aluno: ")
            situacao = verificar_situacao(matricula)
            if situacao:
                print(f"Situação do aluno: {situacao}")

        elif opcao == '5':
            exibir_todos_os_alunos()

        elif opcao == '6':
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()

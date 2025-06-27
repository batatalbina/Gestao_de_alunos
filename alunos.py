alunos = []
def adicionar_aluno(nome, matricula):
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'notas': []
    }
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso.")

def encontrar_aluno(matricula):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

def adicionar_nota(matricula, nota):
    aluno = encontrar_aluno(matricula)
    if aluno:
        aluno['notas'].append(nota)
        print(f"Nota {nota} adicionada ao aluno {aluno['nome']}.")
    else:
        print("Aluno não encontrado.")

def calcular_media(matricula):
    aluno = encontrar_aluno(matricula)
    if aluno:
        if aluno['notas']:
            media = sum(aluno['notas']) / len(aluno['notas'])
            return media
        else:
            return 0.0
    else:
        print("Aluno não encontrado.")
        return None

def verificar_situacao(matricula):
    media = calcular_media(matricula)
    if media is None:
        return
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_todos_os_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        media = calcular_media(aluno['matricula'])
        situacao = verificar_situacao(aluno['matricula'])
        print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}")
        print(f"Notas: {aluno['notas']} | Média: {media:.2f} | Situação: {situacao}")
        print("-" * 40)

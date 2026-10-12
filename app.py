
# Simulação

# Entrada dos dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


# Função para calcular a média
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


# Função para verificar a aprovação
def calcular_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# Função para gerar o relatório
def gerar_relatorio(nome, nota1, nota2, media, situacao):
    relatorio = f"""
Relatório de Notas
------------------
Aluno: {nome}
Nota 1: {nota1}
Nota 2: {nota2}
Média: {media:.1f}
Situação: {situacao}
"""
    return relatorio


# Chamada das funções
media = calcular_media(nota1, nota2)
situacao = calcular_aprovacao(media)


# Relatório
resposta = input("Deseja gerar o relatório? (s/n): ").lower()

if resposta == "s":
    relatorio = gerar_relatorio(
        nome, nota1, nota2, media, situacao
    )
    print(relatorio)
elif resposta == "n":
    print("Relatório não gerado.")
else:
    print("Opção inválida.")

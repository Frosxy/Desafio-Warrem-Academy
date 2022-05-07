
while True:
    try:
        qtdAluno = input(
            "Print digite o minimo de alunos necessários para a aula começar: ")
        break
    except ValueError:  # Exibe na tela caso o úsusário digite um valor não esperado
        print("Digite um valor válido")

HAluno = []

while True:
    while True:
        try:    # Exibe na tela caso o úsusário digite um valor não esperado
            HAlunos = int(input("Digite o tempo de chegada do aluno: "))
            break
        except ValueError:
            print("Informe um valor Válido")
            print("\n " * 130)  # Limpa a Tela

    # percorre a lista e armazena os tempos de chegada dos alunos
    HAluno.append(HAlunos)

    try:    # Exibe na tela caso o úsusário digite um valor não esperado
        resposta = input(
            "Deseja digitar mais algum tempo?  ('Y' para continuar e qualquer outra tecla para parar): ")
    except ValueError:
        print("Digite um valor Válido")
        print("\n " * 130)  # Limpa a Tela

    resposta = resposta.upper()  # Garante que o valor digitado seja maiusculo

    if (resposta != "Y"):  # Fecha a repetição caso não tenha sido digitado nada
        break

qtd = 0
for repeticoes in HAluno:

    if repeticoes <= 0:

        qtd = qtd + 1

qtd = 0
qtdAluno = 0

if qtd >= qtdAluno:

    print("Aula normal")

else:

    print("Aula cancelada")

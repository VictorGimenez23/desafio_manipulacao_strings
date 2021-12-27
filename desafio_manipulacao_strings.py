qtdeAlunos = int(input("Digite a quantidade de alunos a ser lido: "))

nomes = []
provas1 = []
provas2 = []
trabalhos1 = []
trabalhos2 = []
mediasFinal = []
status = []

for i in (range(qtdeAlunos)):
    nome = input("Digite o nome do aluno: ")
    prova1 = float(input("Digite a nota da prova 1: "))
    prova2 = float(input("Digite a nota da prova 2: "))
    trabalho1 = float(input("Digite a nota do trabalho 1: "))
    trabalho2 = float(input("Digite a nota da trabalho 2: "))

    nomes.append(nome)
    provas1.append(prova1)
    provas2.append(prova2)
    trabalhos1.append(trabalho1)
    trabalhos2.append(trabalho2)
    print("")

espacos = 16 * " "
print(f"Nome{espacos}",end="")
print("Trab1 ",end="")
print("Prova1   ",end="")
print("Trab2 ",end="")
print("Prova2   ",end="")
espacos = 6 * " "
print(f"Nota Final{espacos}", end="")
print(f"Resultado Final{espacos}")

for i in (range(len(nomes))):
    resultado = ((((trabalhos1[i] + trabalhos2[i])/2)*3) + (((provas1[i] + provas2[i])/2)*7))/10
    mediasFinal.append(round(resultado,1))

    if resultado < 5:
        status.append("Reprovado")
    elif resultado >= 5 and resultado < 6:
        status.append("Recuperacao")
    else:
        status.append("Aprovado")

    if len(nomes[i]) >= 19:
        print(f"{nomes[i][:16]}... ",end="")
    else:
        qtdeEspacos = len(nomes[i])
        espacos = " " * (20 - qtdeEspacos)
        print(f"{nomes[i]}{espacos}", end="")

    qtdeEspacos = len(str(trabalhos1[i]))
    espacos = " " * (5 - qtdeEspacos)
    print(f"{trabalhos1[i]}{espacos} ",end="")
    qtdeEspacos = len(str(provas1[i]))
    espacos = " " * (8 - qtdeEspacos)
    print(f'{provas1[i]}{espacos} ', end="")
    qtdeEspacos = len(str(trabalhos2[i]))
    espacos = " " * (5 - qtdeEspacos)
    print(f'{trabalhos2[i]}{espacos} ', end="")
    qtdeEspacos = len(str(provas2[i]))
    espacos = " " * (8 - qtdeEspacos)
    print(f'{provas2[i]}{espacos} ', end="")
    qtdeEspacos = len(str(mediasFinal[i]))
    espacos = " " * (15 - qtdeEspacos)
    print(f'{mediasFinal[i]}{espacos} ', end="")
    qtdeEspacos = len(str(status[i]))
    espacos = " " * (14 - qtdeEspacos)
    print(str(f'{status[i]} ').center(15))
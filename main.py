# Função open("Localização do Arquvivo", Modo de Abertura do Arquivo)
# Ex de modos de abertura:
# "r" = read (Ler); "w" = whrite (Escrever), "a" = append (Escreve no final do Arquivo), "x" (Cria um novo arquivo e escreve)

"""
arquivo = open("log.txt", "a", encoding="utf-8")

arquivo.write(str(input("Escreva algo: ") + "\n"))

"""

cont = 1

while True:

    arquivo_log = open(
        f"C:\\Users\\João Pedro Sousa\\Desktop\\python\\manipulaçãoDeArquivos\\arquivos_log\\log_cadastro_{cont}.txt",
        "w",
        encoding="utf-8",
    )

    arquivo_log.write(str(input(f"[Arquivo N° {cont}] \nEscreva algo: ")))

    flag_continuar = (
        str(input("Deseja continuar? [S] para SIM, [N] para NÃO: ")).strip().upper()
    )

    cont += 1

    arquivo_log.close()

    if flag_continuar == "N":
        print("Programa encerrado...")
        break

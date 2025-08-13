class GravarArquivo:

    def __init__(self):
        pass

    def gravar_arquivo(self):

        cont = 1

        while True:

            with open(
                f"C:\\Users\\João Pedro Sousa\\Desktop\\python\\manipulaçãoDeArquivos\\arquivos_log\\log_cadastro_{cont}.txt",
                "w",
                encoding="utf-8",
            ) as arquivo_log:

                arquivo_log.write(str(input(f"[Arquivo N° {cont}] \nEscreva algo: ")))

            flag_continuar = (
                str(input("Deseja continuar? [S] para SIM, [N] para NÃO: "))
                .strip()
                .upper()
            )

            cont += 1

            if flag_continuar == "N":
                print("Programa encerrado...")
                break

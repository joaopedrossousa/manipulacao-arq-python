class LerArquivo:

    def __init__(self):
        pass

    def cabecalho_menu_leitura(self):
        print("-" * 40)
        print(f"LEITURA DO ARQUIVO N° {self.id_arquivo}".center(40))
        print("-" * 40)

    def indice_arquivo(self):
        self.id_arquivo = int(input("Informe o N° do arquivo: "))

    def ler_arquivo(self):

        while True:

            self.indice_arquivo()

            print()

            self.cabecalho_menu_leitura()

            print()

            with open(
                f"C:\\Users\\João Pedro Sousa\\Desktop\\python\\manipulaçãoDeArquivos\\arquivos_log\\log_cadastro_{self.id_arquivo}.txt",
                "r",
                encoding="utf-8",
            ) as arquivo_log:

                leitura_arquivo = arquivo_log.read()

                for i in range(0, len(leitura_arquivo), 40):
                    print(f"{leitura_arquivo [i:i+40]:<40}")

            print()

            flag_continuar = int(
                input("[1] Ler outro arquivo \n[0] Sair \nSelecione uma opção: ")
            )

            if flag_continuar == 0:
                break

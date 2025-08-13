from services.gravar_arquivo import GravarArquivo


class Menu:

    def __init__(self):

        self.gravar_arquivo = GravarArquivo()

    def cabecalho(self):

        print("-" * 40)
        print("MENU PRINCIPAL".center(40))
        print("-" * 40)

    def indices_menu(self):
        print("[1] GRAVAR ARQUIVO")
        print("[2] LER ARQUIVO")
        print("[0] SAIR")

    def ler_opcao(self):
        try:
            self.opcao = int(input("Selecione uma opção: "))

        except (ValueError, TypeError):
            print("Opção Invalida! ")

    def menu_principal(self):

        while True:
            self.cabecalho()
            print()
            self.indices_menu()
            print()
            self.ler_opcao()
            if self.opcao == 1:
                self.gravar_arquivo.gravar_arquivo()

            if self.opcao == 0:
                print("Programa encerrado...")
                break

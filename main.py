# Função open("Localização do Arquvivo", Modo de Abertura do Arquivo)
# Ex de modos de abertura:
# "r" = read (Ler); "w" = whrite (Escrever), "a" = append (Escreve no final do Arquivo), "x" (Cria um novo arquivo e escreve)

"""
arquivo = open("log.txt", "a", encoding="utf-8")

arquivo.write(str(input("Escreva algo: ") + "\n"))

"""
from menu.menu_funcoes import Menu

menu = Menu()
menu.menu_principal()

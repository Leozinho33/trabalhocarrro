import os
import json


class Veiculo:
    def __init__(self):
        self.lista_veiculos = []

    def cadastrar(self):
        print("Cadastro de Veículo:")
        placa = input("Informe a placa do veículo: ").strip()
        modelo = input("Informe o modelo do veículo: ").strip()
        ano = input("Informe o ano de fabricação do veículo: ").strip()

        
        veiculo = {
            "placa": placa,
            "modelo": modelo,
            "ano": ano
        }
        
        self.lista_veiculos.append(veiculo)

        print(f"Veículo {modelo} com placa {placa} cadastrado com sucesso!")

    def listar(self):
        if not self.lista_veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("+-------------------------------+")
            print("|        Veículos Cadastrados    |")
            print("+-------------------------------+")
            for veiculo in self.lista_veiculos:
                print(f"Placa: {veiculo['placa']} | Modelo: {veiculo['modelo']} | Ano: {veiculo['ano']}")
            print("+-------------------------------+")


def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    veiculo = Veiculo()  

    TContinue = True
    while TContinue:
        LimpaTela()
        print("+-------------------------------+")
        print("|     1 - Cadastrar Veículo     |")
        print("|     2 - Listar Veículos       |")
        print("|    10 - Sair                  |")
        print("+-------------------------------+")
        Menu = input("      Informe a opção: ")

        if Menu == '1':
            LimpaTela()
            veiculo.cadastrar()  
            input("Pressione Enter para continuar...")

        elif Menu == '2':
            LimpaTela()
            veiculo.listar()  
            input("Pressione Enter para continuar...")

        elif Menu == '10':
            TContinue = False
            print("Saindo do sistema...")
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()  

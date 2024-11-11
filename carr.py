import os
import json

class Veiculo:
    def __init__(self):
        self.listaveiculo = []

    def carregar(self):
        self.arquivo = "veiculos.json"
        if(os.path.exists(self.arquivo)):
            with open(self.arquivo, "r") as f:
                self.listaveiculo = json.load(f)
        else:
            self.listaveiculo = []

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.listaveiculo, f, indent=4)

    def cadastrar(self):
        print("+----------------------------------------+")
        modelo = input("| Modelo: ")
        ano = input("| Ano: ")
        placa = input("| Placa: ")
        cor = input("| Cor: ")
        tipo = input("| Tipo (carro, moto, caminhão): ")
        chassi = input("| Chassi: ")
        renavam = input("| RENAVAM: ")
        print("+----------------------------------------+")

        
        self.listaveiculo.append({
            "modelo": modelo,
            "ano": ano,
            "placa": placa,
            "cor": cor,
            "tipo": tipo,
            "chassi": chassi,
            "renavam": renavam
        })

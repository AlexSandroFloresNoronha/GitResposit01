import json

class Produto:
    def __init__(self, codigo, nome, quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

def detalhar(self):
    return self.__dict__

def inserir(self):

    try:
        with open('db/produtos.json') as file:
            lista = json.load(file)
    except Exception:
        lista = []

lista.append(self.detalhar())

with open('db/produtos.json', 'w') as file:
    json.dump(lista, file, indent=4)

print('Registro cadastrado com sucesso')
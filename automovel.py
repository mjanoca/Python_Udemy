import veiculo
from PySimpleGUI import PySimpleGUI as sg


class Automovel(veiculo.Veiculo):

    def __init__(self, *args, **kwargs):
        veiculo.Veiculo.__init__(self)
        try:
            if len(args) != 0:
                self.tipo = args[0] or None
                self.modelo = args[1] or None
                self.marca = args[2] or None
                self.valor = args[3] or None
                self.ano_fabricacao = args[4] or None
                print(args, kwargs)
            elif len(kwargs) != 0:
                self.tipo = kwargs.get('tipo')
                self.modelo = kwargs.get('modelo')
                self.marca = kwargs.get('marca')
                self.valor = kwargs.get('valor')
                self.ano_fabricacao = kwargs.get('ano_fabricacao')
        except Exception as e:
            sg.popup(f'Atenção! {e}. Foram passados {len(args)} parâmetro(s) para a função, porém é necessário'
                  f' que passe 5 parâmetros Ou passe parâmetros nomeados!')
            exit(1)

    def setTipo(self, tipo):
        self.tipo = tipo

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca

    def setValor(self, valor):
        self.valor = valor

    def setAnoFabricacao(self, ano):
        self.ano_fabricacao = ano

    def getTipo(self):
        return self.tipo

    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def getValor(self):
        return self.valor

    def getAnoDeFabricacao(self):
        return self.ano_fabricacao

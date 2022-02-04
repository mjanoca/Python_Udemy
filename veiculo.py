from abc import ABC, abstractmethod


class Veiculo(ABC):
    tipo            = ""
    modelo          = ""
    marca           = ""
    valor           = 0.0
    ano_fabricacao  = 0

    @abstractmethod
    def setTipo(self, tipo):
        pass

    @abstractmethod
    def setModelo(self, modelo):
        pass

    @abstractmethod
    def setMarca(self, marca):
        pass

    @abstractmethod
    def setValor(self, valor):
        pass

    @abstractmethod
    def setAnoFabricacao(self, ano):
        pass

    @abstractmethod
    def getTipo(self):
        pass

    @abstractmethod
    def getModelo(self):
        pass

    @abstractmethod
    def getMarca(self):
        pass

    @abstractmethod
    def getValor(self):
        pass

    @abstractmethod
    def getAnoDeFabricacao(self):
        pass
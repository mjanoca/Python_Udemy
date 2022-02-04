import automovel
import motocicleta

carro1 = automovel.Automovel(tipo='Carro')
moto1 = motocicleta.Motocicleta(marca="dafra", tipo="moto")
# moto2 = motocicleta.Motocicleta("a")

print(carro1.getTipo())
print(moto1.getTipo())

print(carro1 == moto1)

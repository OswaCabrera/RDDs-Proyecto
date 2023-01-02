class Operacion:
  def __init__(self, operacion_anterior, operador):
    self.operacion_anterior = operacion_anterior
    self.operador = operador

  def resultado(self):
    # IMPLEMENTAR+
    return 1

class OperacionMap(Operacion):
  def resultado(self):
    resultado_previo = operacion_anterior.resultado()
    for elemento in resultado_previo:
      yield self.operador(elemento)

class OperacionReduce(Operacion):
  def resultado(self):
    resultado_previo = operacion_anterior.resultado()
    yield self.operador(resultado_previo)

class OperacionInicial(Operacion):
  def __init__(self, datos):
    self.datos = datos

  def resultado(self):
    return self.datos

#Y con esto podrian hacer:
inicio = OperacionInicial([1, 2, 3, 4, 5])
dobles = OperacionMap(inicio, lambda x: x*2)

dobles.resultado() # -> [2, 4, 6, 8, 10]

suma_dobles = OperacionReduce(dobles, sum)
# suma_doles.resultado() # -> [30]

# -- si se dan cuenta, esto define un grafo aciclico: OperacionInicial() -> OperacionMap(doble) -> OperacionMap(cuadrado) -> OperacionReduce(sum)


# Una idea: 
# Como harian una OperacionUnion que toma dos entradas tal que:
OperacionUnion(
  OperacionInicial([1,2]),
  OperacionInicial([3,4])).resultado() # -> [1, 2, 3, 4]

# Como harian una OperacionReduce que utiliza pares de clave-valor?

OperacionReduce(
  sum,   #<- operador de suma
  OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])).resultado() # -> [('llave1', 3), ('llave2', 3)]   <- las sumas de los elementos de cada llave

# Como harian una OperacionGroup que agrupa pares de clave-valor?
OperacionGroup(
  OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])).resultado() # -> [('llave1', [1, 2]), ('llave2', [3])]   <- las uniones de los pares

# Como harian una OperacionJoin que une dos colecciones segun sus llaves de clave-valor?
OperacionJoin(
  OperacionInicial([('llave1', 1), ('llave2',2)]),
  OperacionInicial([('llave1', 10), ('llave1',9)])).resultado() # -> [('llave1', [1, 10]), ('llave2', [2, 9])]   <- las uniones de los pares


# Esto les permite construir grafos mas complejos:

OperacionInicial---OperacionMap() -v
OperacionInicial ---> OperacionUnion() -> OperacionMap(...) -> OperacionReduce(...)
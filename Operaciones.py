import functools

class Operacion:
  def __init__(self, operacion_anterior, operador):
    self.operacion_anterior = operacion_anterior
    self.operador = operador

  def resultado(self):
    # IMPLEMENTAR+
    return 1

class OperacionMap(Operacion):
  def resultado(self):
    resultado_previo = self.operacion_anterior.resultado()
    # for elemento in resultado_previo:
    #   yield self.operador(elemento)
    self.datos = list(map(self.operador, resultado_previo))
    return self.datos

class OperacionReduce(Operacion):
  def resultado(self):
    resultado_previo = self.operacion_anterior.resultado()
    self.datos = functools.reduce(self.operador, resultado_previo)
    return self.datos

class OperacionInicial(Operacion):
  def __init__(self, datos):
    self.datos = datos

  def resultado(self):
    return self.datos


def main():
  inicio = OperacionInicial([1, 2, 3, 4, 5])
  dobles = OperacionMap(inicio, lambda x: x*2)
  suma_dobles = OperacionReduce(dobles, sum)

  print(suma_dobles.resultado())

if __name__ == "__main__":
    main()
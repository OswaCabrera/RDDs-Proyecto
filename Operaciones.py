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
    if(type(resultado_previo[0])=='int'):
      self.datos = functools.reduce(self.operador, resultado_previo)
    else:
      for item in resultado_previo:
          
          pass
    return self.datos

class OperacionInicial(Operacion):
  def __init__(self, datos):
    self.datos = datos

  def resultado(self):
    return self.datos

# OperacionUnion(
#   OperacionInicial([1,2]),
#   OperacionInicial([3,4])).resultado() # -> [1, 2, 3, 4]
# )

class OperacionUnion(Operacion):
  def __init__(self, operacion_1 , operacion_2):
    self.operacion_1 = operacion_1
    self.operacion_2 = operacion_2

  def resultado(self):
    self.datos = self.operacion_1.datos + self.operacion_2.datos
    self.datos.sort()
    return self.datos

# OperacionGroup(
#   OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])).resultado() # -> [('llave1', [1, 2]), ('llave2', [3])]   <- las uniones de los pares

('llave1', 1)

class OperacionGroup(Operacion):
  def __init__(self, operacion_anterior):
    self.operacion_anterior = operacion_anterior
  
  def buscarKey(val, lista):
    for index, item in enumerate(lista):
      if val == item[0]:
        return index

  def resultado(self):
    self.datos = self.operacion_anterior.resultado()
    #array de tuplas
    arrayResultado = []
    array_aux = []
    keys = []
    for item in self.datos:
      if item[0] in keys:
        indice = self.buscarKey(item[0])
        array_aux = arrayResultado[indice]
        array_aux.append(item[1])
        array_aux.sort()
        # arrayResultado.append((item[0], array_aux))
        arrayResultado[item[0]] = array_aux
        array_aux = []
      else:
        keys.append(item[0])
        array_aux.append(item[1])
        arrayResultado.append((item[0], array_aux))
        array_aux = []
    self.datos = arrayResultado
    return self.datos
    


# Como harian una OperacionReduce que utiliza pares de clave-valor?

# OperacionReduce(
#   sum,   #<- operador de suma
#   OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])).resultado(
#    # -> [('llave1', 3), ('llave2', 3)]   <- las sumas de los elementos de cada llave

def main():
  inicio = OperacionInicial([1, 2, 3, 4, 5])
  dobles = OperacionMap(inicio, lambda x: x*2)
  print(dobles.resultado())
  suma_dobles = OperacionReduce(dobles,lambda a,b: a+b)

  union = OperacionUnion(dobles, inicio)
  print(union.resultado())

  # lista_1 = [1,2,3]
  # print(lista_1.type)
  lista_2 = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
  lista_group = OperacionGroup(lista_2)
  print(lista_group.resultado())


if __name__ == "__main__":
    main()
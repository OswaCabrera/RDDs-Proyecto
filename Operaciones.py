import functools
from Graph import Graph

lineage_graph = Graph(0)
paralelo = [[]]

class Operacion:
  def __init__(self, operacion_anterior, operador):
    self.operacion_anterior = operacion_anterior
    self.operador = operador
    self.nivel = operacion_anterior.nivel + 1
    self.id = lineage_graph.V
    lineage_graph.V = lineage_graph.V + 1
    lineage_graph.addEdge(operacion_anterior.id,self.id)
    if len(paralelo) == self.nivel:
      array_aux_paral = [self.id]
      paralelo.append(array_aux_paral)
    else:
      paralelo[self.nivel].append(self.id)

class OperacionInicial(Operacion):
  def __init__(self, datos):
    self.datos = datos
    self.nivel = 0
    self.id = lineage_graph.V
    lineage_graph.V = lineage_graph.V + 1
    paralelo[self.nivel].append(self.id)

  def resultado(self):
    return self.datos

class OperacionMap(Operacion):
  def resultado(self):
    resultado_previo = self.operacion_anterior.resultado()
    self.datos = list(map(self.operador, resultado_previo))
    return self.datos

class OperacionReduce(Operacion):
  def resultado(self):
    resultado_previo = self.operacion_anterior.resultado()
    if(type(resultado_previo[0])=='int'):
      self.datos = functools.reduce(self.operador, resultado_previo)
    else:
      self.datos = group(resultado_previo)
      for index, item in enumerate(self.datos):
        self.datos[index] = (item[0], functools.reduce(self.operador, item[1]))
    return self.datos

class OperacionUnion(Operacion):
  def __init__(self, operacion_1 , operacion_2):
    self.operacion_1 = operacion_1
    self.operacion_2 = operacion_2
    self.id = lineage_graph.V
    if operacion_1.nivel > operacion_2.nivel:
      self.nivel = operacion_1.nivel
    else:
      self.nivel = operacion_2.nivel
    lineage_graph.V = lineage_graph.V + 1
    lineage_graph.addEdge(operacion_1.id,self.id)
    lineage_graph.addEdge(operacion_2.id,self.id)
    if len(paralelo) == self.nivel:
      array_aux_paral = [self.id]
      paralelo.append(array_aux_paral)
    else:
      paralelo[self.nivel].append(self.id)

  def resultado(self):
    self.datos = self.operacion_1.datos + self.operacion_2.datos
    self.datos.sort()
    return self.datos

class OperacionGroup(Operacion):
  def __init__(self, operacion_anterior):
    self.operacion_anterior = operacion_anterior
    self.id = lineage_graph.V
    lineage_graph.V = lineage_graph.V + 1
    self.nivel = operacion_anterior.nivel + 1
    lineage_graph.addEdge(operacion_anterior.id,self.id)
    if len(paralelo) == self.nivel:
      array_aux_paral = [self.id]
      paralelo.append(array_aux_paral)
    else:
      paralelo[self.nivel].append(self.id)

  def resultado(self):
    self.datos = self.operacion_anterior.resultado()
    #array de tuplas
    self.datos = group(self.datos)
    return self.datos


class OperacionJoin(Operacion):
  def __init__(self, operacion_anterior, operacion_anterior2):
    self.operacion_anterior = operacion_anterior
    self.operacion_anterior2 = operacion_anterior2
    self.id = lineage_graph.V
    if operacion_anterior.nivel > operacion_anterior2.nivel:
      self.nivel = operacion_anterior.nivel
    else:
      self.nivel = operacion_anterior2.nivel
    lineage_graph.V = lineage_graph.V + 1
    lineage_graph.addEdge(operacion_anterior.id,self.id)
    lineage_graph.addEdge(operacion_anterior2.id,self.id)
    if len(paralelo) == self.nivel:
      array_aux_paral = [self.id]
      paralelo.append(array_aux_paral)
    else:
      paralelo[self.nivel].append(self.id)
  
  def resultado(self):
    resultado_anterior = self.operacion_anterior.datos + self.operacion_anterior2.datos
    self.datos = group(resultado_anterior)
    return self.datos


def buscarKey(val, lista):
    print(val)
    for index, item in enumerate(lista):
      print(item)
      if val == item[0]:
        print(index)
        return index

def group(datos):
  arrayResultado = []
  tupla_aux = []
  array_aux = []
  keys = []
  for item in datos:
    if item[0] in keys:
      indice = buscarKey(item[0], arrayResultado)
      tupla_aux = arrayResultado[indice]
      tupla_aux[1].append(item[1])
      tupla_aux[1].sort()
      arrayResultado[indice] = tupla_aux
      tupla_aux = []
    else:
      keys.append(item[0])
      array_aux.append(item[1])
      arrayResultado.append((item[0], array_aux))
      array_aux = []
  return arrayResultado

def printInfo():
  print('Ordenamiento topológico')
  lineage_graph.topologicalSort()
  print("Tareas que se pueden ejecutar paralelamente:")
  for index, nivel in enumerate(paralelo):
    print(str(index + 1) + ':')
    print(nivel)


def main():
  inicio = OperacionInicial([1, 2, 3, 4, 5])
  dobles = OperacionMap(inicio, lambda x: x*2)
  # print(dobles.resultado())
  suma_dobles = OperacionReduce(dobles,lambda a,b: a+b)

  union = OperacionUnion(dobles, inicio)
  # print(union.resultado())

  lista_1 = [1,2,3]
  # # print(lista_1.type)
  lista_2 = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
  lista_group = OperacionGroup(lista_2)
  # print(lista_group.resultado())
  
  # lista3 = OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])
  # lista4 = OperacionReduce(lista3, lambda a,b: a+b)
  # print(lista4.resultado())

  # lista5 = OperacionJoin(lista_2, lista3)
  # print(lista5.resultado()) 
  printInfo()

if __name__ == "__main__":
    main()
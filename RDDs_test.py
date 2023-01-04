import unittest
import Graph
import Operaciones

class TestRDDs(unittest.TestCase):
    def test_join(self):
        inicio = OperacionInicial([1, 2, 3, 4, 5])
        dobles = OperacionMap(inicio, lambda x: x*2) 
        printInfo()

if __name__ == '__main__':
    unittest.main()





    def main():
  
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


import unittest
import Graph
import Operaciones

class TestRDDs(unittest.TestCase):
    def test_operacionMAP(self):
        inicio = OperacionInicial([1, 2, 3, 4, 5])
        dobles = OperacionMap(inicio, lambda x: x*2)
        printInfo()
    def test_operacionReduce(self):
        lista= OperacionInicial([2,4,6,8,10])
        lista2 = OperacionReduce(lista, lambda a,b: a+b)
        printInfo()
    def test_operacionReduceTupla(self):
        lista = OperacionInicial([('llave1',5), ('llave1',6), ('llave2', 3), , ('llave2', 8)])
        lista_reduce = OperacionReduce(lista3, lambda a,b: a+b)
    def test_operacionUnion(self):
         primero = OperacionInicial([1, 2, 3, 4, 5])
         segundo = OperacionInicial([6, 7, 8, 9, 10])
         union = OperacionUnion(primero, segundo)
         printInfo()
    def test_operacionGroup(self):
        lista = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
        lista_group = OperacionGroup(lista)
        printInfo()
    def test_operacionJoin(self):
         lista_uno = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
         lista_dos = OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])
         lista_join = OperacionJoin(lista_uno, lista_dos)
         printInfo()
    def test_grafoComplejo(self):
        inicio = OperacionInicial([1, 2, 3, 4, 5])
        dobles = OperacionMap(inicio, lambda x: x*2)
        union = OperacionUnion(inicio, dobles)
        dobles = OperacionMap(union, lambda x: x*2)
        lista_reduce = OperacionReduce(lista3, lambda a,b: a+b)
        printInfo()

if __name__ == '__main__':
    unittest.main()


import unittest
import Graph
from Operaciones import *

class TestRDDs(unittest.TestCase):
    def test_operacionMAP(self):
        print('Caso 1')
        inicio = OperacionInicial([1, 2, 3, 4, 5])
        dobles = OperacionMap(inicio, lambda x: x*2)
        printInfo()
    def test_operacionReduce(self):
        print('Caso 2')
        lista= OperacionInicial([2,4,6,8,10])
        lista2 = OperacionReduce(lista, lambda a,b: a+b)
        printInfo()
    def test_operacionReduceTupla(self):
        print('Caso 3')
        lista = OperacionInicial([('llave1',5), ('llave1',6), ('llave2', 3), ('llave2', 8)])
        lista_reduce = OperacionReduce(lista, lambda a,b: a+b)
        printInfo()
    def test_operacionUnion(self):
        print('Caso 4')
        primero = OperacionInicial([1, 2, 3, 4, 5])
        segundo = OperacionInicial([6, 7, 8, 9, 10])
        union = OperacionUnion(primero, segundo)
        printInfo()
    def test_operacionGroup(self):
        print('Caso 5')
        lista = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
        lista_group = OperacionGroup(lista)
        printInfo()
    def test_operacionJoin(self):
        print('Caso 6')
        lista_uno = OperacionInicial([('llave1',2),('llave2',3), ('llave2',4), ('llave1',3)])
        lista_dos = OperacionInicial([('llave1', 1), ('llave1',2), ('llave2', 3)])
        lista_join = OperacionJoin(lista_uno, lista_dos)
        printInfo()
    def test_grafoComplejo(self):
        print('Caso 7')
        inicio = OperacionInicial([1, 2, 3, 4, 5])
        dobles = OperacionMap(inicio, lambda x: x*2)
        union = OperacionUnion(inicio, dobles)
        dobles = OperacionMap(union, lambda x: x*2)
        lista_reduce = OperacionReduce(dobles, lambda a,b: a+b)
        printInfo()

if __name__ == '__main__':
    unittest.main()
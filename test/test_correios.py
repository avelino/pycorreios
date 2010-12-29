#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

import unittest

from pycorreios.correios import Correios
from pycorreios.model import Cep, Frete, Encomenda

class CorreiosTests(unittest.TestCase):
    def testFrete(self):
        valor_esperado = {'MsgErro': '', 
                          'PrazoEntrega': u'1', 
                          'Erro': u'0', 
                          'ValorValorDeclarado': u'0,00', 
                          'EntregaDomiciliar': u'S', 
                          'ValorMaoPropria': u'0,00', 
                          'EntregaSabado': u'S', 
                          'Valor': u'151,40', 
                          'Codigo': u'40010'
                         }
        valor = Correios().frete(Correios().SEDEX,'44001535',
                                 '03971010',10,18,8)

        assert valor == valor_esperado

    def testCep(self):
        valor_esperado = {'tipo_logradouro': u'Rua', 
                          'bairro': u'Jardim Santa Adelia', 
                          'cidade': u'S\xe3o Paulo', 
                          'uf': u'SP', 
                          'logradouro': u'Pascoal Dias'
                         } 
        valor = Correios().cep('03971010')
        assert valor == valor_esperado
        
    def testEncomenda(self):
        valor_esperado = Encomenda(data='30/11/2010 18:49', local='CEE BRAS - SAO PAULO/SP', status='Entregue')
        valor = Correios().encomenda('SW238151411BR')[0]
        
        assert valor.data == valor_esperado.data
        assert valor.local == valor_esperado.local
        assert valor.status == valor_esperado.status
def main():
    unittest.main()

if __name__ == '__main__':
    main()

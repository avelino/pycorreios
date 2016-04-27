#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pycorreios.correios import Correios
from pycorreios.model import Cep, Frete, Encomenda


class CorreiosTest(unittest.TestCase):

    def test_frete(self):

        valor_esperado = {
            'MsgErro': '',
            'PrazoEntrega': u'2',
            'Erro': u'0',
            'ValorValorDeclarado': u'0,00',
            'EntregaDomiciliar': u'S',
            'ValorMaoPropria': u'0,00',
            'EntregaSabado': u'S',
            'Valor': u'62,40',
            'Codigo': u'40010'
        }
        valor = Correios().frete(Correios.SEDEX, '44001535', '03971010',
                                 1, 1, 18, 9, 13.5, 0)

        self.assertDictEqual(valor_esperado, valor)

    def test_cep(self):

        valor_esperado = {
            'tipo_logradouro': u'Rua',
            'bairro': u'Jardim Santa Adelia',
            'cidade': u'S\xe3o Paulo',
            'uf': u'SP',
            'logradouro': u'Pascoal Dias',
        }

        valor = Correios().cep('03971010')
        self.assertDictEqual(valor_esperado, valor)
        
    def test_encomenda(self):

        valor_esperado = {
            'data': '03/02/2016 17:57',
            'local': u'CDD ITAJUBA - Itajuba/MG',
            'status': 'Entrega Efetuada',
        }

        valor = Correios().encomenda('PJ382325976BR')[0]
        self.assertDictEqual(valor_esperado, valor)

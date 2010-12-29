#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Dilan Nery'

class Cep(object):
    def __init__(self, cep='', uf='', cidade='', bairro='', 
                 tipo_logradouro='', logradouro=''):

        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.bairro = bairro
        self.tipo_logradouro = tipo_logradouro
        self.logradouro = logradouro

class Frete(object):
    def __init__(self, msgErro='', erro='', codigo='', valor='',
                 prazoEntrega='', valorMaoPropria='',
                 valorValorDeclarado='', entregaDomiciliar='',
                 entregaSabado=''):

        self.msgErro = msgErro
        self.erro = erro
        self.codigo = codigo
        self.valor = valor
        self.prazoEntrega = prazoEntrega
        self.valorMaoPropria = valorMaoPropria
        self.valorValorDeclarado = valorValorDeclarado
        self.entregaDomiciliar = entregaDomiciliar
        self.entregaSabado = entregaSabado
        
class Encomenda(object):
    def __init__(self, data='', local='', status=''):
        self.data = data
        self.local = local
        self.status = status
        

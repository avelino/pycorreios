# -*- coding: utf-8 -*-
"""
correios.py
----------

Api para usar dados dos Correios
"""

__version__ = '0.1.0'
__author__ = {
              'Thiago Avelino': 'thiagoavelinoster@gmail.com',
              'Dilan Nery': 'dnerylopes@gmail.com',
             }

import urllib2
import sys
from xml.dom import minidom

import cod

class Correios(object):
    def __init__(self):
        self.status = 'OK'
        self.PAC = 41106
        self.SEDEX = 40010
        self.SEDEX_10 = 40215
        self.SEDEX_HOJE = 40290
        self.E_SEDEX = 81019
        self.OTE = 44105
        self.NORMAL = 41017
        self.SEDEX_A_COBRAR = 40045

    def _getDados(self,tags_name, dom):
        dados = {}

        for tag_name in tags_name:
            try:
                dados[tag_name] = dom.getElementsByTagName(tag_name)[0]
                dados[tag_name] = dados[tag_name].childNodes[0].data
            except:
                dados[tag_name] = ''

        return dados

    def frete(self,cod,GOCEP,HERECEP,peso,
              comprimento,diametro,toback='xml'):
    
        url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?\
               StrRetorno=%s\
               &nCdServico=%s\
               &nVlPeso=%i\
               &sCepOrigem=%s\
               &sCepDestino=%s\
               &nVlComprimento=%s\
               &nVlDiametro=%s" % (toback,cod,peso,HERECEP,
                                   GOCEP,comprimento,diametro)
        dom = minidom.parse(urllib2.urlopen(url))
    
        tags_name = ('MsgErro',
                     'Erro',
                     'Codigo',
                     'Valor',
                     'PrazoEntrega',
                     'ValorMaoPropria',
                     'ValorValorDeclarado',
                     'EntregaDomiciliar',
                     'EntregaSabado',
                    )

        return self._getDados(tags_name, dom)

    def cep(self,numero):
        url = 'http://cep.republicavirtual.com.br/web_cep.php?\
               formato=xml&cep=%s' % (str(numero))
        dom = minidom.parse(urllib2.urlopen(url))

        tags_name = ('uf',
                     'cidade',
                     'bairro',
                     'tipo_logradouro',
                     'logradouro',
                    )

        resultado = dom.getElementsByTagName('resultado')[0]
        resultado = int(resultado.childNodes[0].data)
        if resultado != 0:
            return self._getDados(tags_name, dom)
        else:
            return {}

# Delete the modules to not show up in the namespace
# del  urllib2, sys, minidom

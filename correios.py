# -*- coding: utf-8 -*-
"""
correios.py
----------

Api para usar dados dos Correios
"""

__version__ = 1.0
__author__ = {
              'Thiago Avelino': 'thiagoavelinoster@gmail.com',
              'Dilan Nery': 'dnerylopes@gmail.com',
             }

import urllib2
import sys
from xml.dom import minidom

import cod

"""
FRETE_PAC = 41106
FRETE_SEDEX = 40010
FRETE_SEDEX_10 = 40215
FRETE_SEDEX_HOJE = 40290
FRETE_E_SEDEX = 81019
OTE = 44105
FRETE_NORMAL = 41017
SEDEX_A_COBRAR = 40045
"""

def frete(cod,GOCEP,HERECEP,peso,
          comprimento,diametro,toback='xml'):

    dados = {}

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

    for tag_name in tags_name:
        try:
            dados[tag_name] = dom.getElementsByTagName(tag_name)[0]
            dados[tag_name] = dados[tag_name].childNodes[0].data
        except:
            dados[tag_name] = ''

    return dados

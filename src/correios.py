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

def cep(numero):
    dados = {}

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
        for tag_name in tags_name:
            try:
                dados[tag_name] = dom.getElementsByTagName(tag_name)[0]
                dados[tag_name] = dados[tag_name].childNodes[0].data
            except:
                dados[tag_name] = ''

    return dados

# Delete the modules to not show up in the namespace
# del  urllib2, sys, minidom

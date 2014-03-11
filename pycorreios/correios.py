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

import urllib
import urllib2
import re
from xml.dom import minidom
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    raise ImportError, 'Você não tem o modulo BeautifulSoup'

from model import Encomenda
    
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

    # Vários campos viraram obrigatórios para cálculo de frete:
    # http://www.correios.com.br/webServices/PDF/SCPP_manual_implementacao_calculo_remoto_de_precos_e_prazos.pdf (páginas 2 e 3)
    def frete(self, cod, GOCEP, HERECEP, peso, formato,
              comprimento, altura, largura, diametro, mao_propria='N',
              valor_declarado='0', aviso_recebimento='N',
              empresa='', senha='', toback='xml'):
        
        base_url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"

        fields = [
            ('nCdEmpresa', empresa),
            ('sDsSenha', senha),
            ('nCdServico', cod),
            ('sCepOrigem', HERECEP),
            ('sCepDestino', GOCEP),
            ('nVlPeso', peso),
            ('nCdFormato', formato),
            ('nVlComprimento', comprimento),
            ('nVlAltura', altura),
            ('nVlLargura', largura),
            ('nVlDiametro', diametro),
            ('sCdMaoPropria', mao_propria),
            ('nVlValorDeclarado', valor_declarado),
            ('sCdAvisoRecebimento', aviso_recebimento),
            ('StrRetorno', toback),
        ]

        url = base_url + "?" + urllib.urlencode(fields)
        dom = minidom.parse(urllib2.urlopen(url))
    
        tags_name = ('MsgErro',
                     'Erro',
                     'Codigo',
                     'Valor',
                     'PrazoEntrega',
                     'ValorMaoPropria',
                     'ValorValorDeclarado',
                     'EntregaDomiciliar',
                     'EntregaSabado',)

        return self._getDados(tags_name, dom)

        
    def cep(self,numero):
        url = 'http://cep.republicavirtual.com.br/web_cep.php?formato=xml&cep=%s' % (str(numero),)
        dom = minidom.parse(urllib2.urlopen(url))

        tags_name = ('uf',
                     'cidade',
                     'bairro',
                     'tipo_logradouro',
                     'logradouro',)

        resultado = dom.getElementsByTagName('resultado')[0]
        resultado = int(resultado.childNodes[0].data)
        if resultado != 0:
            return self._getDados(tags_name, dom)
        else:
            return {}

    def encomenda(self,numero):
        # Usado como referencia o codigo do Guilherme Chapiewski
        # https://github.com/guilhermechapiewski/correios-api-py

        url = 'http://websro.correios.com.br/sro_bin/txect01$.QueryList?P_ITEMCODE=&P_LINGUA=001&P_TESTE=&P_TIPO=001&P_COD_UNI=%s' % (str(numero),)
        html = urllib2.urlopen(url).read()
        table = re.search(r'<table.*</TABLE>', html, re.S).group()
        
        parsed = BeautifulSoup(table)
        
        dados = []
        count = 0
        for tr in parsed.table:
            if count > 4 and str(tr).strip() != '':
                if re.match(r'\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}', tr.contents[0].string):
                    dados.append(
                            Encomenda(data=unicode(tr.contents[0].string),
                                    local=unicode(tr.contents[1].string),
                                    status=unicode(tr.contents[2].font.string))
                    )
                else:
                    dados[len(dados) - 1].detalhes = unicode(tr.contents[0].string)
                    
            count = count + 1
            
        return dados

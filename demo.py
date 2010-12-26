# -*- coding: utf-8 -*-
from correios import frete
from correios import cod

test = frete(cod.FRETE_SEDEX,'44001535','03971010',10,18,8)
print test
if test['Erro'] != '0':
    print 'Deu erro! :('
    print test['Erro']
    print test['MsgErro']
else:
    print "Valor: %s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])

# -*- coding: utf-8 -*-
from correios import frete, cep
from correios import cod

test = frete(cod.SEDEX,'44001535','03971010',10,18,8)
if test['Erro'] != '0':
    print 'Deu erro! :('
    print test['Erro']
    print test['MsgErro']
else:
    print "Valor: %s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])

other_test = cep(44010000)
print other_test['bairro']

# -*- coding: utf-8 -*-
from correios import Correios
from correios import cod

correio = Correios()

test = correio.frete(cod.SEDEX,'44001535','03971010',10,18,8)
if test['Erro'] != '0':
    print 'Deu erro! :('
    print test['Erro']
    print test['MsgErro']
else:
    print "Valor: %s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])

other_test = correio.cep(44010000)
print other_test['bairro']

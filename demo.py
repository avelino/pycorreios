# -*- coding: utf-8 -*-
from pycorreios import Correios

test = Correios().frete(Correios().SEDEX,'44001535','03971010',10,18,8)
if test['Erro'] != '0':
    print 'Deu erro! :('
    print test['Erro']
    print test['MsgErro']
else:
    print "Valor: R$%s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])

print

other_test = Correios().cep('03971010')
for tag_name in other_test.keys():
    print tag_name + ': ' + other_test[tag_name]

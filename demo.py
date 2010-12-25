# -*- coding: utf-8 -*-
from correios import frete

FRETE_PAC = 41106
FRETE_SEDEX = 40010
FRETE_SEDEX_10 = 40215
FRETE_SEDEX_HOJE = 40290
FRETE_E_SEDEX = 81019
OTE = 44105
FRETE_NORMAL = 41017
SEDEX_A_COBRAR = 40045

if __name__ == '__main__':
   
   test = frete(FRETE_SEDEX,'44001535','03971010',10,18,8)
   if test['Erro'] != '0':
      print 'Deu erro! :('
      print test['Erro']
      print test['MsgErro']
   else:
      print "Valor: %s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])

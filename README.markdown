API Correios
============

Installation
------------
If you have _setuptools_ you can use 

    $ easy_install -U pycorreios

Otherwise, you can download the source from [GitHub][git] and run 

    $ python setup.py install

[git]: https://github.com/avelino/pycorreios "PyCorreios"

Examples
--------
Some simple examples of what pyCorreios code looks like:

```python
from pycorreios import Correios

# with a dictionary paramenter - the field order doesn't matter
fields = {"cod": Correios().SEDEX, 
          "GOCEP": "44001535",
          "HERECEP": "03971010",
          "peso": "2",
          "formato": "1", # caixa/pacote
          "comprimento": "18",
          "altura": "8",
          "largura": "24",
          "diametro": "12"}

test = Correios().frete(**fields)   # remember to call with **

# or with positional parameters - same result as above
test = Correios().frete(Correios().SEDEX,'44001535','03971010',2,1,18,8,24,12)

if test['Erro'] != '0':
    print 'Deu erro! :('
    print test['Erro']
    print test['MsgErro']
else:
    print "Valor: R$%s\nPrazo de Entrega: %s" % (test['Valor'],test['PrazoEntrega'])


other_test = Correios().cep('03971010')
for tag_name in other_test.keys():
    print tag_name + ': ' + other_test[tag_name]
```
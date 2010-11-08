import urllib2
from xml.dom import minidom

class correios(object):
		
	def frete(self,cod,GOCEP,HERECEP,peso,comprimento,diametro,toback='xml'):
		
		# FRETE PAC = 41106
		# FRETE SEDEX = 40010
		# FRETE SEDEX 10 = 40215
		# FRETE SEDEX HOJE = 40290
		# FRETE E-SEDEX = 81019
		# FRETE MALOTE = 44105
		# FRETE NORMAL = 41017
		# SEDEX A COBRAR = 40045
		
		url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?StrRetorno=%s&nCdServico=%s&nVlPeso=%i&sCepOrigem=%s&sCepDestino=%s&nVlComprimento=%s&nVlDiametro=%s" % (toback,cod,peso,HERECEP,GOCEP,comprimento,diametro)
		dom = minidom.parse(urllib2.urlopen(url))
		
		self.codigo					= dom.getElementsByTagName('Codigo')[0].childNodes[0].data
		self.valor					= dom.getElementsByTagName('Valor')[0].childNodes[0].data
		self.prazoentrega			= dom.getElementsByTagName('PrazoEntrega')[0].childNodes[0].data
		self.valormaopropria		= dom.getElementsByTagName('ValorMaoPropria')[0].childNodes[0].data
		self.valoravisorecebimento	= dom.getElementsByTagName('ValorAvisoRecebimento')[0].childNodes[0].data
		self.valorvalordeclarado	= dom.getElementsByTagName('ValorValorDeclarado')[0].childNodes[0].data
		self.entregadomiciliar		= dom.getElementsByTagName('EntregaDomiciliar')[0].childNodes[0].data
		self.entregasabado			= dom.getElementsByTagName('EntregaSabado')[0].childNodes[0].data
		self.erro					= dom.getElementsByTagName('Erro')[0].childNodes[0].data
		# self.msgerro				= dom.getElementsByTagName('MsgErro')[0].childNodes[0].data
		
		return self

correio = correios()
test = correio.frete(40215,'03971050','03971010',10,18,8)

print "Valor: %s\nPrazo de Entrega: %s" % (test.valor,test.prazoentrega)
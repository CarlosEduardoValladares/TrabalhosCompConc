#Define funcoes para verificar a logica de execucao de uma aplicacao produtor/consumidor

class PC:
	def __init__(self):
		self.produtores = 0
		self.consumidores = 0
		self.itens = 0
		
	def setItens(self, qtd):
		self.itens = qtd

	def consumidorBloqueado(self,id):
		'''Recebe o id do consumidor. Verifica se a decisao de bloqueio esta correta.'''
		if(self.itens!=0 and self.produtores!=0):
			print("ERRO: consumidor " + str(id) + " bloqueado quando ha produtores ou itens!")

	def produtorBloqueado(self,id):
		'''Recebe o id do produtor. Verifica se a decisao de bloqueio esta correta.'''
		if(self.produtores!=0 and self.itens!=0):
			print("ERRO: produtor " + str(id) + " bloqueado quando nao ha produtores ou com buffer vazio!")

	def consumidorConsumindo(self,id):
		'''Recebe o id do consumidor, verifica se pode consumir e registra que esta consumindo.'''
		if(self.produtores>0):
			print("ERRO: consumidor " + str(id) + " esta consumindo quando ha produtor produzindo!")
		self.consumidores+=1
		self.itens -= 1

	def produtorProduzindo(self,id):
		'''Recebe o id do produtor, verifica se pode produzir e registra que esta produzindo'''
		if(self.produtores>0):
			print("ERRO: produtor " + str(id) + " esta produzindo quando ha outro produtor ou consumidores!")
		self.produtores+=1

	def consumidorSaindo(self,id):
		'''Recebe o id do consumidor e registra que terminou a leitura.'''
		self.consumidores-=1

	def produtorSaindo(self,id):
		'''Recebe o id do produtor e registra que terminou a leitura.'''
		self.produtores-=1

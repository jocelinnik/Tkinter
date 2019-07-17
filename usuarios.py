from Bancao import Bancao

class Usuarios(object):
	def __init__(self, idusuario=0, nome="", telefone="",
				 email="", usuario="", senha=""):
		self.info = {}
		self.idusuario = idusuario
		self.nome = nome
		self.telefone = telefone
		self.email = email
		self.usuario = usuario
		self.senha = senha

	def insertUser(self):
		bancao = Bancao()

		try:
			c = bancao.conexao.cursor()

			c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values ('" + self.nome + "','" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "')")
			bancao.conexao.commit()
			c.close()

			return "Usuário cadastrado com sucesso!"
		except:
			return "Deu ruim na insercao do usuário!"

	def updateUser(self):
		bancao = Bancao()

		try:
			c = bancao.conexao.cursor()

			c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = '" + self.idusuario + "'")

			bancao.conexao.commit()
			c.close()

			return "Usuário atualizado com sucesso!"
		except:
			return "Deu ruim na atualizacao do usuario!"

	def deleteUser(self)
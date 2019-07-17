from tkinter import *

class Application:
	def __init__(self, master=None):
		self.widget1 = Frame(master)
		self.widget1.pack()
		self.msg = Label(self.widget1, text="TESTE VIOLENTO")
		self.msg["font"] = ("Calibri", "9", "italic", "bold")
		self.msg.pack()
		self.sair = Button(self.widget1)
		self.sair["text"] = "Clique aqui"
		self.sair["font"] = ("Calibri", "9")
		self.sair["width"] = 10
		self.sair["command"] = self.mudarTexto
		#self.sair.bind("<Button-1>", self.mudarTexto)
		self.sair.pack()

	def mudarTexto(self):
		if self.msg["text"] == "TESTE VIOLENTO":
			self.msg["text"] = "TESTADO VIOLENTAMEMTE"
		else:
			self.msg["text"] = "TESTE VIOLENTO"

root = Tk()
Application(root)
root.mainloop()
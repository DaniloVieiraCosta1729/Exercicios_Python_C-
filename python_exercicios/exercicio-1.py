# Exercício 1 - Perguntar ao usuário seu nome e a data de seu nasciment0; responder uma mensagem de cumprimento e informá-lo quantos anos ele tem.

import datetime

agora = datetime.datetime.now()

hoje = agora.date()

ano = int(hoje.strftime("%Y"))

class Usuario:

    def __init__(self, nome, dataNascimento):
        self.nome = nome
        self.dataNascimento = dataNascimento
        
        idade = ano - self.dataNascimento;
        
    def ola(self):
        cumprimento = f"Olá, {self.nome}! É um prazer te conhecer. De acordo com a sua data de nascimento, sua idade é {ano - self.dataNascimento} anos."
        print(cumprimento)

Danilo = Usuario("Danilo Vieira Costa", 1997)

Danilo.ola()    

a = input()

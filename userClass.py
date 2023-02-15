class Usuario: 
    def __init__(self, nome="", sobrenome=""):
        self.nome = nome
        self.sobrenome = sobrenome

    def hello(self):
        return "Olá, " + self.nome + " " + self.sobrenome + "!"

usuario1 = Usuario("Gabriela", "Andrade")
print(usuario1.hello())

usuario2 = Usuario("Jane", "Silva")
print(usuario2.hello())

#Resposta dos exercícios teóricos: 
#1. c) É a personificação de um objeto da vida real.
#2. b) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.
#3. c) Uma variável dentro de uma classe.
#4. a) Uma função dentro de uma classe.
#5. Nome da classe: Usuario
#   Propriedades: nome, sobrenome
#   Método: hello()


from platform import python_version
print('Exercícios de programação orientada a objetos utilizando python')

"""## Exercícios"""

# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
roc1 = Rocket(3,4)
roc1.move_rocket(1,1)
roc1.print_rocket()

# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.
class Pessoa():
  def __init__(self,nome,cidade,telefone,email):
    self.nome = nome
    self.cidade = cidade
    self.telefone = telefone
    self.email = email

  def __len__(self):
    cont = len(self.nome) + len(self.cidade) + \
    len(self.telefone) + len(self.email)
    return cont

  def print_pes(self):
    print(str(self.nome))
    print(self.cidade)
    print(self.telefone)
    print(self.email)
   
pessoa1 = Pessoa('Lucas Tiago de Oliveira','Uberlândia','954782408','lucastiago')
pessoa1.print_pes()
len(pessoa1)

# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():

  def __init__(self, tamanho, interface):
    self.tamanho = tamanho
    self.interface = interface


class MP3Player (Smartphone):

  def __init__ (self, storage, tamanho = '1', interface = '2'):
    self.storage = storage
    Smartphone.__init__(self,tamanho,interface)
  def print_mp3(self):
    print('O tamanho do objeto e', self.tamanho)

device = MP3Player('16','12','android')
device.print_mp3()

"""### FIM

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
"""
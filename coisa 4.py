class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
        
    def cancular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
# EXEMPLO
p1 = Pessoa("Mashutan", 25, 70, 1.75) # Inclui peso e altura
p1.apresentar
print(f"Meu Imc é {p1.cancular_imc():.2f}")

print(type(p1))


#modulos e bibliotecas

import math

print(math.sqrt(16)) # Raiz quadrada 
print(math.pi) # Valor de PI
print(math.pow(10,2)) # Elevar o primeiro valor pelo segundo

# Exemplo pratico com random

import random

print(random.randint(1,10)) #numero aleatorio entre 1 e 10

# Exemplo prático com datetime

import datetime

agora = datetime.datetime.now()
print("Data e hora atual:", agora)
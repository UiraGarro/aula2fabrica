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
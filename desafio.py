class Pokemon:
    def __init__(self, nome, ataque, defesa, velocidade):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        
    def apresentar(self):
        print(f"Seu {self.nome} tem: {self.ataque} de ataque, {self.defesa} de defesa e {self.velocidade} de velocidade.")
            
    def calcular_média(self):
        média = (self.ataque + self.defesa + self.velocidade) / 3
        return média
   
   #Exemplo
   
p1 = Pokemon("Zoroark", 25, 30, 30)
p1.apresentar()
print(f"Sua média é {p1.calcular_média():.1f}")         
        
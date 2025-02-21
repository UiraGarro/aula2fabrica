for i in range(5): #repete 5 vezes (de 0 a 4)>>> conta ate x, sendo range(x)
    print("Repetição número: ", i) 

counter = 0
max = 10
while counter <= max -1:
    counter += 1
    print(counter)
    
names = ['Pedro', 'Joao', 'Leticia']
for name in names:
    print(name)
    
    
#7 - python possui estruturas de dados que nos ajudam a armazenar e manipular informações de forma eficiente dentre as quatro principais são:
    
 #listas - coleção mutável e ordenada
 #tuplas - coleção imutável e ordenada
 #dicionários - armazena dados no formado chave-valor
 #conjuntos(set) - coleção mutável, não ordenada e sem elementos repetidos

numeros = [10, 20, 30 , 40]

numeros.append(50) # Adiciona um novo numero no final
print(numeros)

numeros.insert(2,25) # Adiciona 25 na posição 2
print(numeros)

numeros.remove(20) # Remove o numero 20
print(numeros)

print(numeros[0]) # Acessa o primeiro elemento

print(len(numeros)) # Retorna a quantidade de elementos na lista

numeros.pop() # Remove o ultimo elemento
print(numeros)

numeros.clear() # Remove todos os elementos
print(numeros)

#TUPLAS

# Quando usar tuplas?
# Quando os valores não devem mudar(exemplo: coordenadas, cores, configurações fixas)
# Para armazenar dados imutáveis que precisam ser protegidos

#exemplo:

coordenadas = (10,20)

print(coordenadas[0]) # Acessa o primeiro valor
print(coordenadas[1]) # Acessa o segundo valor

# coordenadas[0] = 30 # Isso daria erro, pois tuplas são imutáveis

# DICIONÁRIOS

# CARACTERÍSTICAS DOS DICIONÁRIOS:
# Armazena pares chaves-valor (exemplo: { "nome": "Carlos", "idade": 25})
# Mutáveis - Podemos modificar, adicionar e remover valores

# Exemplo

pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

print(pessoa["nome"]) # Acessa o valor da chave "nome"

pessoa["idade"] = 31 # Modifica um valor
print(pessoa)

pessoa["profissão"] = "Engenheiro" # Adiciona uma nova chave-valor

del pessoa["cidade"] # Remove um item do dicinario
print(pessoa)

# Conjuntos(Set)

# CARACTERÍSTICAS
# Não ordenados
# Mutáveis
# Não permitem elementos duplicados

#Exemplo

numero = {1, 2, 3, 4, 5}

numero.add(6) # Adiciona um novo número
print(numero) 

numero.remove(3) # Remove o número 3
print(numero) 

numero.add(2) # Tentando adicionar um número já existente (não faz nada)
print(numero)

#Operações com Conjuntos

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B) # União (valores presentes em A ou B)
print(A & B) # Interseção (valores presentes em A e B)
print (A - B) # Diferença (valores em A que não estão em B)
print(A ^ B) # Diferença simétrica (valores que estão em A ou B, mas não em ambos)

# FUNÇÕES

def greetings(nome):
    print(f"Olá, (nome)!")

greetings("Roudgi")
greetings("Vikitu")

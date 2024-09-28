nome = input("Qual é o seu nome?")
print(f"O seu nome é {nome}")
notas = 0
somafinal = 0
mediafinal = 0
while(notas < 4):
    nota = input(f"Qual a nota que voce tirou na prova {notas+1} ")
    somafinal += float(nota)
    notas += 1
    
print(f"Sua soma de notas é {somafinal}")
mediafinal = somafinal / notas
print(f"sua media final é {mediafinal}")
if mediafinal >= 7:
    print(f"Olha {nome}, Voce tirou {mediafinal}, e voce passou")
else: 
    print(f"Olha {nome}, Voce tirou {mediafinal}, e voce nao passou")
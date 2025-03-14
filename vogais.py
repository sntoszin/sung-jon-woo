palavra = input("Digite uma palavra: ")


contador_vogais = 0


vogais = "aeiouAEIOU"

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
    

print(f"A quantidade de vogais na palavras '(palavra)' é: {contador_vogais}")
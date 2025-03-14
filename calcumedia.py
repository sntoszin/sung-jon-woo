

nota1 = eval(input('Digite a 1ª nota: '))
nota2 = eval(input('Digite a 2ª nota: '))
nota3 = eval(input('Digite a 3ª nota: '))
nota4 = eval(input('Digite a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4


## print(f'A media do aluno é: {media:.2f}')


print('\nClassificação:')
if media >=7:
    print("O aluno foi aprovado!")
    print(f'A media do aluno é: {media:.2f}')
else:
    print("O aluno foi reprovado!")
    print(f'A media do aluno é: {media:.2f}')
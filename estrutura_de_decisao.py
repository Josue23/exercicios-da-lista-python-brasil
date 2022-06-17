'''https://wiki.python.org.br/EstruturaDeDecisao'''
import string


def maior_de_dois_numeros(numero_1, numero_2):
    '''Faça um Programa que peça dois números e imprima o maior deles. '''
    if numero_1 > numero_2:
        print(f'O maior número é: {numero_1}')
    else:
        print(f'O maior número é: {numero_2}')


def positivo_ou_negativo(valor):
    '''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''
    if valor > 0:
        print(f'O valor {valor} é positivo.')
    elif valor < 0:
        print(f'O valor {valor} é negativo.')


def genero(letra):
    '''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
    F - Feminino, M - Masculino, Sexo Inválido. '''
    if letra in ['F', 'f', 'M', 'm']:
        letra = letra.upper()
        if letra == 'F':
            print(f'{letra} é feminino.')
        else:
            print(f'{letra} é masculino')
    else:
        print(f'{letra} é inválido.')


def vogal_ou_consoante(letra):
    '''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''
    letra = str(letra)
    letras = string.ascii_letters
    vogais = 'AaEeIiOoUu'
    if letra in letras:
        if letra in vogais:
            print(f'{letra} é vogal.')
        else:
            print(f'{letra} é consoante.')
    else:
        print(f'{letra} não é vogal nem consoante.')


def media_aluno(nota_1, nota_2):
    '''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
    por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez. '''
    media = (nota_1 + nota_2) / 2
    if media == 10:
        print(f'Média: {media}, Aprovado com Distinção.')
    elif media >= 7:
        print(f'Média: {media}, Aprovado.')
    elif media < 7:
        print(f'Média: {media}, Reprovado.')


def maior_de_tres_numeros(numero_1, numero_2, numero_3):
    '''Faça um Programa que leia três números e mostre o maior deles. '''
    maior = numero_1
    if numero_2 > maior:
        maior = numero_2
    if numero_3 > maior:
        maior = numero_3

    return maior


def maior_e_menor_de_tres_numeros(numero_1, numero_2, numero_3):
    '''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
    maior = numero_1
    if numero_2 > maior:
        maior = numero_2
    if numero_3 > maior:
        maior = numero_3

    menor = numero_1
    if numero_2 < menor:
        menor = numero_2
    if numero_3 < menor:
        menor = numero_3

    return f'Maior: {maior}, menor: {menor}'


def produto_mais_barato(**kwargs):
    '''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''
    produto_mais_barato = list(kwargs.items())[0]  # cria uma tupla
    # transforma a tupla em lista
    produto_mais_barato = list(produto_mais_barato)
    for produto, valor in kwargs.items():
        if valor < produto_mais_barato[1]:
            produto_mais_barato[:2] = [produto, valor]

    return produto_mais_barato[:2]


'''Como usar exercício 8:
>>> produtos = {'ovo': 3, 'banana': 1.5, 'laranja': 1.25, 'cenoura': 2.75, 'melancia': 0.99}
>>> produto_mais_barato(**produtos)'''


def quick_sort(sequencia):
    '''Faça um Programa que leia três números e mostre-os em ordem decrescente. '''
    tamanho = len(sequencia)
    if tamanho <= 1:
        return sequencia
    else:
        pivot = sequencia.pop()

    menor_que_pivot = []
    maior_que_pivot = []

    for numero in sequencia:
        if numero < pivot:
            menor_que_pivot.append(numero)
        else:
            maior_que_pivot.append(numero)

    a = quick_sort(menor_que_pivot)
    b = [pivot]
    c = quick_sort(maior_que_pivot)
    '''mostra em ordem crescente'''
    # return a + b + c

    '''mostra em ordem decrescente'''
    return c + b + a
# return quick_sort(menor_que_pivot) + [pivot] + quick_sort(maior_que_pivot)


'''Como usar exercício 9:
lista = [3, 1, 9]
quick_sort(lista)'''


def cumprimentar(letra):
    '''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
    N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''

    letras = ['M', 'm', 'V', 'v', 'N', 'n']
    if letra in letras:
        if letra in ['M', 'm']:
            cumprimento = 'Bom dia!'
        elif letra in ['V', 'v']:
            cumprimento = 'Boa tarde!'
        else:
            cumprimento = 'Boa noite!'

        return cumprimento

    else:
        print(f'Valor {letra}  inválido.')

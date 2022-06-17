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


def aumento_de_salario(salario):
    '''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
    desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
    salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''
    if salario <= 280:
        percentual_de_aumento = 0.20
        aumento = salario * percentual_de_aumento
        salario_com_aumento = salario + aumento
    elif 280 < salario < 700:
        percentual_de_aumento = 0.15
        aumento = salario * percentual_de_aumento
        salario_com_aumento = salario + aumento
    elif 700 < salario < 1500:
        percentual_de_aumento = 0.10
        aumento = salario * percentual_de_aumento
        salario_com_aumento = salario + aumento
    else:
        percentual_de_aumento = 0.05
        aumento = salario * percentual_de_aumento
        salario_com_aumento = salario + aumento
    print(f'''
Salario: {salario}
Percentual de aumento: {percentual_de_aumento * 100}
Valor do aumento: {aumento:.2f}
Salário reajustado: {salario_com_aumento:.2f}
    ''')


'''Como usar exercício 11:
>>> aumento_de_salario(200)'''


def folha_de_pagamentos(valor_hora, horas_trabalhadas_mes):
    '''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
    Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
    os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme
        o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00'''

    salario_bruto = valor_hora * horas_trabalhadas_mes
    if salario_bruto <= 900:
        imposto_renda = 0
    elif salario_bruto <= 1500:
        imposto_renda = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        imposto_renda = salario_bruto * 0.10
    else:
        imposto_renda = salario_bruto * 0.20

    inss = salario_bruto * 0.10
    # sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11  # não é descontado do salario bruto

    descontos = imposto_renda + inss
    salario_liquido = salario_bruto - descontos

    print(f'''
Salário Bruto: ({valor_hora} * {horas_trabalhadas_mes})        : R$ {salario_bruto:.2f}
(-) IR (5%)                     : R$ {imposto_renda:.2f}
(-) INSS ( 10%)                 : R$ {inss:.2f}
FGTS (11%)                      : R$ {fgts:.2f}
Total de descontos              : R$ {descontos:.2f}
Salário Liquido                 : R$ {salario_liquido:.2f}''')


def dia_da_semana(entrada):
    '''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido. '''

    dias_da_semana = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    if entrada in range(1, 8):
        for chave, valor in dias_da_semana.items():
            if entrada == chave:
                return valor
    else:
        return f'Valor {entrada} inválido.'


'''Como usar exercício 13:
dia_da_semana(1)'''

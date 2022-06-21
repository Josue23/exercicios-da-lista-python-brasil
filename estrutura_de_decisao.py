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


def aprovado_reprovado_duas_notas(nota_1, nota_2):
    '''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
    e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se
    o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''
    media = (nota_1 + nota_2) / 2

    if 9 < media <= 10:
        conceito = 'A'
    elif 7.5 < media <= 9:
        conceito = 'B'
    elif 6 < media <= 7.5:
        conceito = 'C'
    elif 4 < media <= 6:
        conceito = 'D'
    elif 0 <= media <= 4:
        conceito = 'E'

    if conceito in ['A', 'B', 'C']:
        mensagem = 'APROVADO'
    else:
        mensagem = 'REPROVADO'

    print(f'''
Primeira nota: {nota_1}
Segunda nota: {nota_2}
Média: {media}
Conceito: {conceito}
Mensagem: {mensagem}
    ''')


def triangulo(lado_a, lado_b, lado_c):
    '''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
    triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; '''

    condicao_1 = lado_a + lado_b > lado_c
    condicao_2 = lado_a + lado_c > lado_b
    condicao_3 = lado_b + lado_c > lado_a

    if True in [condicao_1, condicao_2, condicao_3]:
        if lado_a == lado_b == lado_c:
            return 'Equilátero'
        elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
            return 'Isósceles'
        else:
            return 'Escaleno'


'''Como usar exercício 15:
>>> estrutura_de_decisao.triangulo(2, 0, 3) '''


def equacao_segundo_grau(**kwargs):
    '''Onde testar:
    https://www.calculadoraonline.com.br/equacao-2-grau'''

    '''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
    pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
    os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
    equação do segundo grau: ax² + bx + c = 0
    delta: b² - 4ac '''
    a, b, c = [valor for valor in kwargs.values()]
    if a == 0:
        print('Equação do segundo grau não pode ter a == 0')
        return None
    else:
        # descobrindo o delta
        delta = b ** 2 - 4 * a * c
        raiz_1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz_2 = (-b - (delta ** 0.5)) / (2 * a)
        if delta < 0:
            print(
                f'Delta: {delta}. A equação não possui raizes reais porque o delta é negativo.')
            return None
        # raiz_1 = (-b + (delta ** 0.5)) / (2 * a)
        # raiz_2 = (-b - (delta ** 0.5)) / (2 * a)

        elif delta == 0:
            print(f'Delta: {delta}, Raiz: {raiz_1}')
        else:
            print(f'''
    Delta: {delta}
    Primeira raiz: {raiz_1}
    Segunda raiz: {raiz_2}''')


'''Como usar exercício 16:
>>> valores = {'a': 1, 'b': -6, 'c': 5}
>>> equacao_segundo_grau(**valores)'''


def ano_bissexto(ano):
    '''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
    não bissexto.'''

    bissexto = ano % 4 == 0 and ano % 400 == 0

    if bissexto:
        return f'{ano}: bissexto.'
    else:
        return f'{ano}: não bissexto.'


'''Como usar exercício 17:
>>> ano_bissexto(2000)'''


def data_valida(data):
    '''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''

    lista_de_datas = data.split('/')
    lista_de_datas = [int(data) for data in lista_de_datas]
    dia, mes, ano = [x for x in lista_de_datas]

    if dia in range(32) and mes in range(1, 13) and ano in range(-5000, 5000):
        dia in range(32)
        mes in range(1, 13)
        ano in range(-5000, 5000)
        return dia, mes, ano


'''Como usar exercício 18:
>>> data_valida('23/09/1989')'''


def centenas_dezenas_unidades(entrada: int):
    '''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
    unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e
    16 '''
    assert entrada < 1000, f"{entrada} não é menor que 1000"
    centena = 100
    dezena = 10

    centenas = entrada // centena
    restante = entrada % centena

    dezenas = restante // dezena
    restante = restante % dezena

    unidades = restante

    '''Python Ternary operator'''
    centenas_str = 'centenas' if centenas != 1 else 'centena'
    dezenas_str = 'dezenas' if dezenas != 1 else 'dezena'
    unidades_str = 'unidades' if unidades != 1 else 'unidade'

    print(f'{centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}')


'''Como usar exercício 18:
>>> centenas_dezenas_unidades(326)'''


def aprovado_reprovado_tres_notas(nota_1, nota_2, nota_3):
    '''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
    aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
    media = (nota_1 + nota_2 + nota_3) / 3
    resultado = 'Aprovado com Distinção' if media == 10 else 'Reprovado' if media < 7 else 'Aprovado'

    return nota_1, nota_2, nota_3, media, resultado

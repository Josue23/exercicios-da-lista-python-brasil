#! /usr/bin/python
'''https://wiki.python.org.br/EstruturaSequencial
Python Brasil
EstruturaSequencial'''


def alo_mundo():
    '''Faça um Programa que mostre a mensagem "Alo mundo" na tela. '''
    return 'Alo mundo'


'''Como usar exercício 1:
>>> alo_mundo()'''


def mostra_numero(numero):
    '''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. '''
    return f'O número informado foi {numero}'


'''Como usar exercício 2:
>>> mostra_numero(5)'''


def soma(numero, numero_2):
    '''Faça um Programa que peça dois números e imprima a soma. '''
    resultado = f'{numero} + {numero_2} = {numero + numero_2}'
    return resultado


'''Como usar exercício 3:
>>> soma(numero = 2, numero_2 = 3)'''


def calcula_media(nota, nota_1, nota_2, nota_3):
    '''Faça um Programa que peça as 4 notas bimestrais e mostre a média. '''
    return f'{nota} + {nota_1} + {nota_2} + {nota_3} / 4 = {(nota + nota_1 + nota_2 + nota_3) / 4}'


'''Como usar exercício 4:
>>> calcula_media(nota = 8, nota_1 = 8.5, nota_2 = 9, nota_3 = 9.2)'''


def converte_metros_para_centimetros(metros):
    '''Faça um Programa que converta metros para centímetros. '''
    return metros * 100


'''Como usar exercício 5:
>>> converte_metros_para_centimetros(1.1)'''


def calcula_area_circulo(raio):
    '''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
    area = 3.14_15_92 * raio**2
    return area


'''Como usar exercício 6:
>>> calcula_area_circulo(3.5)'''


def calcula_area_quadrado(entrada):
    '''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. '''
    area_quadrado = entrada*entrada
    return area_quadrado*2


'''Como usar exercício 7:
>>> calcula_area_quadrado(6)'''


def calcula_salario(valor_hora, horas_trabalhadas):
    '''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
    mostre o total do seu salário no referido mês. '''
    salario = valor_hora * horas_trabalhadas
    return salario


'''Como usar exercício 8:
>>> calcula_salario(valor_hora=10, horas_trabalhadas=8)'''


def fahrenheit_para_celsius(fahrenheit):
    '''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9). '''
    celsius = 5 * (fahrenheit - 32) / 9
    return celsius


'''Como usar exercício 9:
>>> fahrenheit_para_celsius(99)'''


def celsius_para_fahrenheit(celsius):
    '''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. '''
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


'''Como usar exercício 10:
>>> celsius_para_fahrenheit(45)'''


def tres_calculos(numero: None, numero_2: None, numero_3: None):
    '''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
            a. o produto do dobro do primeiro com metade do segundo .
            b. a soma do triplo do primeiro com o terceiro.
            c. o terceiro elevado ao cubo. '''
    def produto(numero: int, numero_2: int):
        '''o produto do dobro do primeiro com metade do segundo . '''
        # resultado = (numero * 2) * (numero_2 / 2)
        print(f'{numero} * 2 * {numero_2} / 2 = {numero * 2 * numero_2 / 2}')
    produto(numero, numero_2)

    def soma(numero: int, numero_3: float):
        '''a soma do triplo do primeiro com o terceiro. '''
        print(f'{numero * 3} + {numero_3} = {numero * 3 + numero_3}')
    soma(numero, numero_3)

    def cubo(numero_3: float):
        '''o terceiro elevado ao cubo. '''
        print(f'{numero_3} ** 3 = {numero_3 ** 3}')
    cubo(numero_3)


'''Como usar exercício 11:
>>> tres_calculos(4, 5, 7)'''


def peso_ideal(altura: float):
    '''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58 '''
    peso = (72.7 * altura) - 58
    return peso


'''Como usar exercício 12:
>>> peso_ideal(1.71)'''


def peso_ideal_por_genero(altura: float):
    '''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
            a. Para homens: (72.7*h) - 58
            b. Para mulheres: (62.1*h) - 44.7 '''
    peso_masculino = (72.7 * altura) - 58
    peso_feminino = (62.1 * altura) - 44.7
    print(f'Para homem: {peso_masculino:.2f}')
    print(f'Para mulher: {peso_feminino:.2f}')


'''Como usar exercício 13:
>>> peso_ideal_por_genero(1.71)'''


def peso_de_peixes(peso):
    '''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
    trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
    São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
    que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
    além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa
    com as mensagens adequadas. '''
    peso_maximo_permitido = 50
    multa_kilo_excedente = 4
    if peso > peso_maximo_permitido:
        excesso = peso - peso_maximo_permitido
    else:
        excesso = 0
    multa = excesso * multa_kilo_excedente
    print(f'Excesso: {excesso} quilos, multa: R$ {multa:.2f}')


'''Como usar exercício 14:
>>> peso_de_peixes(55)'''


def salario_impostos(valor_hora, horas_trabalhadas_mes):
    '''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido. '''
    salario_bruto = valor_hora * horas_trabalhadas_mes
    impoto_renda = 11 / 100 * salario_bruto
    inss = 8 / 100 * salario_bruto
    sindicato = 5 / 100 * salario_bruto
    descontos = impoto_renda + inss + sindicato
    salario_liquido = salario_bruto - descontos
    print(f'Salário bruto: {salario_bruto:.2f}')
    # print(f'Descontos: {descontos:.2f}')
    print(f'IR: R$ {impoto_renda:.2f}')
    print(f'INSS: R$ {inss:.2f}')
    print(f'Sindicato: R$ {sindicato:.2f}')
    print(f'Salário líquido: R$ {salario_liquido:.2f}')


'''Como usar exercício 15:
>>> salario_impostos(valor_hora=10, horas_trabalhadas_mes = 160)'''


def loja_de_tinta(area_em_metros):
    '''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
    pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
    latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
    preço total. '''
    litros_de_tinta = area_em_metros / 3

    '''math.ceil without importing math module
    https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
    latas_de_tinta = -(-litros_de_tinta // 18)
    # latas_de_tinta = litros_de_tinta / 18

    # if latas_de_tinta % 1 == 0:
    #     latas_de_tinta = latas_de_tinta
    # else:
    #     latas_de_tinta = int(latas_de_tinta) + 1

    valor_total = latas_de_tinta * 80
    return latas_de_tinta, valor_total


'''Como usar exercício 16:
>>> loja_de_tinta(18)'''


def loja_de_tinta_1(area_a_ser_pintada):
    '''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
    pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
    latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 3,6 litros;
        misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
        arredonde os valores para cima, isto é, considere latas cheias. '''

    def apenas_latas(area_a_ser_pintada):
        area_a_ser_pintada = area_a_ser_pintada * 1.1
        litros_por_metro = 6
        litros_de_tinta = area_a_ser_pintada / litros_por_metro

        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        litros_por_lata = 18
        latas_de_tinta = -(-litros_de_tinta // litros_por_lata)

        valor_total = latas_de_tinta * 80
        print(
            f'''
            Apenas latas
Latas: {latas_de_tinta},  Valor: {valor_total:.2f}''')
    apenas_latas(area_a_ser_pintada)

    def apenas_galoes(area_a_ser_pintada):
        area_a_ser_pintada = area_a_ser_pintada * 1.1
        litros_por_metro = 6
        litros_de_tinta = area_a_ser_pintada / litros_por_metro

        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        litros_por_galao = 3.6
        galoes_de_tinta = -(-litros_de_tinta // litros_por_galao)

        valor_total = galoes_de_tinta * 25

        print(
            f'''
            Apenas galões
Galôes: {galoes_de_tinta},  Valor: {valor_total:.2f}''')
    apenas_galoes(area_a_ser_pintada)

    def latas_e_galoes(area_a_ser_pintada):
        area_a_ser_pintada = area_a_ser_pintada * 1.1
        metros_por_litro = 6
        litros_de_tinta = area_a_ser_pintada / metros_por_litro

        litros_por_lata = 18
        litros_por_galao = 3.6
        if area_a_ser_pintada >= 108:
            # latas_de_tinta = -(-litros_de_tinta // litros_por_lata)
            latas_de_tinta = litros_de_tinta // litros_por_lata
        else:
            latas_de_tinta = 0

        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        # galoes_de_tinta = -(-area_em_metros_restante // litros_de_tinta)
        litros_faltantes = litros_de_tinta % litros_por_lata
        galoes_de_tinta = -(-litros_faltantes // litros_por_galao)
        # print(f'galoes_de_tinta: {galoes_de_tinta}')

        # galoes_de_tinta = area_em_metros_restante // litros_de_tinta

        valor_latas = latas_de_tinta * 80

        valor_galoes = galoes_de_tinta * 25
        print(
            f'''
            Latas e Galões
Latas: {latas_de_tinta}, Valor latas: {valor_latas:.2f}
Galôes: {galoes_de_tinta}, Valor galões: {valor_galoes:.2f}''')

    latas_e_galoes(area_a_ser_pintada)


'''Como usar exercício 17:
>>> loja_de_tinta_1(200)'''


def tempo_download_arquivo(tamanho_arquivo_em_mega, velocidade_link_internet):
    '''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
    (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

    '''Testar no link abaixo:
    https://www.omnicalculator.com/other/download-time'''
    # velocidade_link_internet em Mbps, Megabits por segundo

    # tamanho_arquivo_em_bits = tamanho_arquivo_em_mega * \
    #     (8 / 1) * (1.000 / 1) * (1.000 / 1)
    tamanho_arquivo_em_bits = tamanho_arquivo_em_mega * 1.000 * 1.000 * 8

    tempo_aproximado_download_em_segundos = tamanho_arquivo_em_bits / \
        velocidade_link_internet
    minutos = tempo_aproximado_download_em_segundos / 60
    minutos = int(minutos)

    segundos = tempo_aproximado_download_em_segundos % 60
    segundos = int(-1 * segundos // 1 * -1)  # arredonda os segundos para cima
    return f'Tempo aproximado de download é de {minutos} minutos e {segundos} segundos.'


'''Como usar exercício 18:
tempo_download_arquivo(tamanho_arquivo=20, velocidade_link_internet=10)'''

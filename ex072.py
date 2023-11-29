"""Crie um programa que tenha uma tupla totalmente preenchida com
uma contagem por extenso, de zero até vinte"""

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
        print("Digite um número de 0 a 20")
        try:
                entrada_num = input("NÚMERO:")
                if entrada_num.isnumeric():
                        numero_extenso = int(entrada_num)
                        if numero_extenso >= 0 and numero_extenso < 21:
                                numero_extenso = numeros[numero_extenso]
                                print(numero_extenso, '\n')
                        else:  #um número não válido (maior que vinte ou menor que zero)
                                raise ValueError
                else:  #não digitar um número
                        raise ValueError
        except ValueError:
                print("Não é um número válido"+"\n")
                continue


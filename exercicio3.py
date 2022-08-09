"""
=========== Sistema de combustível ============
Digite a quantidade de litros padrão:

Digite a quantidade de litros para preencher a quantidade total:

Digite a valor do litro:

A quantidade que litros que ficou no posto foi: xxx
Estamos com a capacidade de xxx% de litros em nossos tanques
O valor total investido em litros no posto de gasolina é R$xxx

:::: Chegou um cliente, bora vender ? ::::
Digite o nome do cliente:
Digite o R$ "valor" que o senhor(a) xxx que deseja colocar:

:::: Ficou com xxxx litros de um total de yyy de combustível no tanque do posto :::::
:::: O posto está operando agora com x% de sua capacidade de combustivel :::::
"""
import os

print("========== Sistema de combustível ===============")
print("Digite a quantidade de litros padrão:")
litro_posto = float(input())
print("Digite a quantidade de litros para preencher a quantidade total:")
atual_posto = float(input())

valor_compra = float(1)
total_investido = atual_posto * valor_compra
print(f"A capacidade de nossos tanques é de: {litro_posto} litros \n")
print(f"Quantidade restante em nossos tanques é de: {atual_posto} litros \n")
total_porcentagem = atual_posto / litro_posto * 100

print("Estamos operando com uma capacidade de {:0.2f} % em nossos tanques. \n".format(total_porcentagem))
print("O valor total investido em litros no posto de gasolina é de R$ {:0.2f}. \n".format(total_investido))
print(f":::: Chegou um cliente, bora vender? ::::: \n")
print(f"Digite o nome do cliente:")
nome_consumidor = input()

print(f"Qual valor em reais (R$) que o senhor(a), {nome_consumidor}, deseja colocar ? \n")

valor_litro = float(5)
valor_do_cliente = float(input())
valor_litro_cliente = valor_do_cliente / valor_litro
quantidade_litro_cliente = valor_litro_cliente * valor_do_cliente
os.system("clear")

print("==============================================================================================================================")
print(f"Senhor(a) {nome_consumidor}, \n")
print("o valor de R$ {:1.2f} ".format(valor_do_cliente) + "foi adicionado. \n")
print("O que representa uma quantidade total de {:0.1f} litros de combustivel \n".format(valor_litro_cliente))
print("==============================================================================================================================")

sobrou_no_tanque_do_posto = atual_posto - valor_litro_cliente
total_porcentagem = sobrou_no_tanque_do_posto / litro_posto * 100

print(f"::: Estamos operando com uma capacidade de {sobrou_no_tanque_do_posto} litros de um total de {atual_posto} litros de combustível no tanque do posto ::: \n")
print("::: O posto está operando nesse momento com {:0.2f} % de sua capacidade de combustível :::\n".format(total_porcentagem))
investimento_restante = total_investido*total_porcentagem / 100
print("::: O que representa um investimento de R$ {:0.2f} ::: \n".format(investimento_restante))
print(f"::: Tenha um bom dia Sr(a) {nome_consumidor} ::: \n")
print("==============================================================================================================================")
"""
Leandro tem um posto de combustivel, e precisa encher tanque de gasolina do posto.
Faca um programa que digite a quantidade de litros do tanque atual e receba um valor para preencher o tanque,
deixando o mesmo cheio. E quando chegar o cliente colocar o combustivel. Depois  mostrar  quantidade no tanque do posto


=== Sistem de combustivel ===

digite quantidade litros padrao

digite quantidade para preencher quantidade total

a quantidade de litros que ficou no posto foi de:

:::::Chegou um cliente, bora vender:::::

digite o nome do cliente:

digite o valor que deseja para colocar de combustivel:

digite o valor que o senhor(a) xxxx deseja colocar..

::::Ficou com xxxx litros de combustivel de um total yyyy no tanque do posto::::
::::O posto esta operand com X% da sua capacidade de combustivel no posto::::

Mostrar a porcentagem de litros restante no posto



====== CODIGO DANILO REFERENCIA =======

print("------ SISTEMA DE COMBUSTÍVEL--------")
print("digite a quantidade de litro padrão")
litro_padrao = input()

print("digite a quantidade de litros para preencher a qtd total")
qtd_atual_posto = input()

print("A quantidade de litro que ficou no posto foi " + qtd_atual_posto)

print("------ Chegou um cliente, bora vender???------")
print("digite o nome do cliente")
Nome = input()

print("digite o valor que o senhor(a) " + Nome + " deseja colocar")
qtd_cliente = input()

sobra = float(qtd_atual_posto) - float(qtd_cliente)

print(f"Ficou com {sobra} litros de um total de {qtd_atual_posto} de combustivel no tanque do posto")




"""
print("------ SISTEMA DE COMBUSTÍVEL--------")
print("digite a quantidade de litro padrão")
litro_padrao = float(input())

print("digite a quantidade de litros para preencher a qtd total")
qtd_atual_posto = float(input())

print("A quantidade de litro que ficou no posto foi " + qtd_atual_posto)

print("------ Chegou um cliente, bora vender???------")
print("digite o nome do cliente")
Nome = float(input())

print("digite o valor que o senhor(a) " + Nome + " deseja colocar")
qtd_cliente = float(input())

sobra = float(qtd_atual_posto) - float(qtd_cliente)

print(f"Ficou com {sobra} litros de um total de {qtd_atual_posto} de combustivel no tanque do posto")


porcentagem = sobra / qtd_atual_posto * 100 
printprint("Estamos operando com {:0.1f}% da capacidade ".format(porcentagem))
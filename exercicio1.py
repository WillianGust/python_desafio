# Danilo precisa mostra informacoes importantes na tela.
#fazer program que capture as informcaoes e mostre na tela organizada
#Oraganicao exemplo: +++++++Program Formatacao de dados++++++++
# Nome:
# Telefone:
# Endereco:
# ==================
import os

print("======= Bem vindo por favor preencha os dados =======")
print("Digite teu nome:")
nome = input()
print("Digite teu telefone:")
telefone = input()
print("Digite teu endereco:")
endereco = input()
os.system("clear")

print("=======Por favor verifique se as informacoes estao corretas ========")
print("Nome: " + nome)
print("Telefon: " + telefone)
print("Endereco: " + endereco)

print("====================================================================")

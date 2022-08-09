"""
Utilizadno Dict

"""
"""
Utilizando Dict, faça:

Danilo é dono de uma escola de programação, faça um programa
solicite a quantidade de alunos, capture 3 notas de alunos
no final do programa mostre um relatório identificando se os alunos
estão aprovados, reprovados ou em recuperação

Calculo da média
media = (n1+n2+n3)/3

Regra de aprovação:
Notas abaixo de 5 = Reprovado
Notas de 5 até 7 = Recuperção
Notas acima de 7 = Aprovado

Exemplo de lista:

=============[Lista de alunos]==============
Nome: Danilo
Média: 7.5
Situação: Aprovado
-----------------------
Nome: Lana
Média: 5.5
Situação: Recuperacao
-----------------------
"""

print("===============[Bem vindo ao programa de alunos]==============")
qtd = int(input("Digite a quantidade de alunos:\n"))
alunos = []
for indice in range(0, qtd):
  # aluno = []
  aluno = {}
  aluno["nome"] = ""
  aluno["notas"] = "notas"
  aluno["media"] = "media"
  aluno["situacao"] = "situacao"
  nome = input(f"Digite o nome do aluno de número {indice+1}:\n")
  aluno.update(aluno)
  

  notas = {}
  for i in range(0, 3):
    notas.update(float(input(f"Digite a nota {i+1} do(a) {nome}\n")))

  aluno.update(notas)
  media = sum(notas) / len(notas)
  aluno.update(media)

  situacao = "Aprovado"
  if media < 5:
    situacao = "Reprovado"
  elif media >=5 and media <= 7:
    situacao = "Recuperação"
  
  aluno.update(situacao)

  alunos.update(aluno)

print("=============[Lista de alunos]==============")
for aluno in alunos:
  print(f"Nome: {aluno['nome']}")
  print(f"Notas: {aluno['notas']}")
  print(f"Média: {aluno['media']}")
  print(f"Situação: {aluno['situacao']}")
  print("-----------------------")

"""https://www.youtube.com/watch?v=RexybLcGewA
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
"""

tabela_brasileirao = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo', 'internacional', 'Bragantino', 'São Paulo', 'Santos', 'Botafogo', 'Ceará SC', 'Goiás', 'Avaí', 'Cuiabá', 'Coritiba', 'América-MG', 'Atlético-GO', 'Fortaleza', 'Juventude'

print("Esses são os primeiros 5 colocados no brasileirão:")
for time in range(0,5):
  print(time+1, tabela_brasileirao[time])

print('\n'+'E esses são os últimos 4 colocados (rebaixados)')
for rebaixados in range(16, 20):
  print(f'{rebaixados+1}.{tabela_brasileirao[rebaixados]}')

#Em que posição está o time da Chapecoense.
tem_chapecoense = False
for time in range(0, 21):
  if tabela_brasileirao[time].upper() == "CHAPECOENSE":
    tem_chapecoense = True
else:
  if tem_chapecoense:
    print(f'O time da Chapecoense está na posição {time+1} da Série A do Brasileirão')
  else:
    print('O time da Chapecoense não está na Série A do Brasileirão')

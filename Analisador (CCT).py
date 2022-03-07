import pandas as pd
import matplotlib.pyplot as plt
import os
from time import sleep

dados = pd.read_excel('Base_de_Dados_CCT.xlsx')

def grafico(curso, nome, inicio, fim):
  anos = curso['Ano de Referência']
  TAP = curso['Taxa de Permanência - TAP']
  TCA = curso['Taxa de Conclusão Acumulada - TCA']
  TODA = curso['Taxa de Desistência Acumulada - TODA']
  TCAN = curso['Taxa de Conclusão Anual - TCAN']
  TDAN = curso['Taxa de Desistência Anual - TDAN']
  plt.figure(figsize=(26, 32))
  w = 0.16
  plt.bar(anos-w*2, TAP, width = 0.16, color = 'royalblue', edgecolor = 'black' , label = 'Taxa de Permanência - TAP')
  plt.bar(anos-w, TDAN, width = 0.16, color = 'violet', edgecolor = 'black', label = 'Taxa de Desistência Anual - TDAN')
  plt.bar(anos, TODA, width = 0.16, color = 'blueviolet', edgecolor = 'black' , label = 'Taxa de Desistência Acumulada - TODA')
  plt.bar(anos+w, TCAN, width = 0.16, color = 'limegreen', edgecolor = 'black' , label = 'Taxa de Conclusão Anual - TCAN')
  plt.bar(anos+w*2, TCA, width = 0.16, color = 'forestgreen', edgecolor = 'black' , label = 'Taxa de Conclusão Acumulada - TCA')

  for i in range(inicio, fim, 1):
      plt.text(dados['Ano de Referência'].loc[i]-w*2, dados['Taxa de Permanência - TAP'].loc[i], f"{dados['Taxa de Permanência - TAP'].loc[i]:.1f}\n", fontsize = 9, ha = 'center')
      plt.text(dados['Ano de Referência'].loc[i]-w, dados['Taxa de Desistência Anual - TDAN'].loc[i], f"{dados['Taxa de Desistência Anual - TDAN'].loc[i]:.1f}\n", fontsize = 9, ha = 'center')
      plt.text(dados['Ano de Referência'].loc[i], dados['Taxa de Desistência Acumulada - TODA'].loc[i], f"{dados['Taxa de Desistência Acumulada - TODA'].loc[i]:.1f}\n", fontsize = 9, ha = 'center')
      plt.text(dados['Ano de Referência'].loc[i]+w, dados['Taxa de Conclusão Anual - TCAN'].loc[i], f"{dados['Taxa de Conclusão Anual - TCAN'].loc[i]:.1f}\n", fontsize = 9, ha = 'center')
      plt.text(dados['Ano de Referência'].loc[i]+w*2, dados['Taxa de Conclusão Acumulada - TCA'].loc[i], f"{dados['Taxa de Conclusão Acumulada - TCA'].loc[i]:.1f}\n", fontsize = 9, ha = 'center')

  plt.yticks(range(0, 118, 5))
  plt.title(f'\nAnálise dos Indicadores de Fluxo do Curso de {nome} (CCT)\n')
  plt.ylabel('\n%\n')
  plt.xlabel('\nAnos de Referência\n')
  plt.legend()
  plt.show()
  escolha()

def menu():
  print('\nAnalisador Gráfico dos Indicadores de Fluxo dos Cursos da UDESC (CCT)')
  try:
    opcao=int(input('\nDeseja realizar a análise de qual curso?\n\n1) Ciência da Computação\n2) Engenharia Civil\n3) Engenharia Elétrica\n4) Engenharia Mecânica\n5) Engenharia de Produção e Sistemas\n6) Física\n7) Matemática\n8) Química\n9) Tecnologia em Análise e Desenvolvimento de Sistemas\n10) Informações\n11) Finalizar a Execução\n\nDigite aqui a sua resposta: '))
    os.system('cls')
  except (ValueError, TypeError):
    os.system('cls')
    print('\nInfelizmente ocorreu algum erro com o tipo de dado que você digitou. Por favor, tente novamente.')
    menu()
  else:
    if(opcao == 1):
      grafico(dados[20:25], 'Ciência da Computação', 20, 25)
    if(opcao == 2):
      grafico(dados[10:15], 'Engenharia Civil', 10, 15)
    if(opcao == 3):
      grafico(dados[0:5], 'Engenharia Elétrica', 0, 5)
    if(opcao == 4):
      grafico(dados[5:10], 'Engenharia Mecânica', 5, 10)
    if(opcao == 5):
      grafico(dados[30:35], 'Engenharia de Produção e Sistemas', 30, 35)
    if(opcao == 6):
      grafico(dados[15:20], 'Física', 15, 20)
    if(opcao == 7):
      grafico(dados[35:40], 'Matemática', 35, 40)
    if(opcao == 8):
      grafico(dados[40:45], 'Química', 40, 45)
    if(opcao == 9):
      grafico(dados[25:30], 'Tecnologia em Análise e Desenvolvimento de Sistemas', 25, 30)
    if(opcao == 10):
      info()
    if(opcao == 11):
      fim()
    if(opcao < 1 or opcao > 11):
      print(f'\nInfelizmente a opção {opcao} não é válida. Por favor, tente novamente.')
      menu()

def escolha():
  try:
    opcao=int(input('\nO que deseja fazer?\n\n1) Voltar ao Menu Inicial\n2) Finalizar a Execução\n\nDigite aqui a sua resposta: '))
    os.system('cls')
  except (ValueError, TypeError):
    os.system('cls')
    print('\nInfelizmente ocorreu algum erro com o tipo de dado que você digitou. Por favor, tente novamente.')
    escolha()
  else:
    if(opcao == 1):
      menu()
    if(opcao == 2):
      fim()
    if(opcao < 1 or opcao > 2):
      print(f'\nInfelizmente a opção {opcao} não é válida. Por favor, tente novamente.')
      escolha()

def info():
  print('\nEste analisador utilizou os dados fornecidos pela base de dados do INEP (Indicadores de Trajetória da Educação Superior de 2015 até 2019).\n\nLink: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-fluxo-da-educacao-superior\n\n')
  escolha()

def fim():
  print('\nFim de execução.\n\n\nCódigo desenvolvido por Guilherme Tomaselli Borchardt.\nNovembro de 2021.')
  sleep(5)

if __name__ == '__main__':
  menu()
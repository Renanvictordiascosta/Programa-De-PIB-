# bibliotecas usadas
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

# separar elementos em duas listas
def chamada_de_ano_e_valor_de_pib():
    i = 0
    j = 1
    for i in range(0, 7):
        for j in range(0, 1):
            lista_pib_anos.append(lista_do_pib[i][j])
        for j in range(1, 2):
            lista_pib.append(lista_do_pib[i][j])

# chamar as duas listas para mostrar o gráfico
def mostrar_grafico ():
    plot.plot(lista_pib_anos, lista_pib, color = "green", marker = "o", linestyle = "solid")
    plot.title("PIB De Um País Imaginário")
    plot.ylabel("PIB Em Bilhões de Dólares")
    plot.show()

# leitura da planilha em excel e sua transformação numa array com numpy
# para chamar a planilha no seu código, edite o caminho percorrido na sua máquina
dados_do_pib = pd.read_excel("PIB.xlsx")
lista_do_pib = np.array(dados_do_pib)
# criação das funções que receberão os valores da array
lista_pib_anos = []
lista_pib = []
# chamar as funções
chamada_de_ano_e_valor_de_pib()
mostrar_grafico()

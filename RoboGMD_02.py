# Passo a passo do projeto Robô GMD 02

# Passo 1: Entrar no sistema da empresa / formulario / site etc...
    # https://forms.gle/1nme99bup6Ckf6fb6

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link do formulário de teste
pyautogui.write("https://forms.gle/1nme99bup6Ckf6fb6")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("dados.csv")

print(tabela)


# Passo 3: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=429, y=654)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "cod ID"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preenchendo os campos
    pyautogui.write(str(tabela.loc[linha, "nome do item"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "valor"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "nome do comprador"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "telefone"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "e-mail"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click(x=477, y=465)
    pyautogui.click(x=429, y=654)

 # Para este formulário usado no teste, a solução para que seja ativada a página seguinte e localizada a primeira 
 # caixa de resposta eu optei por enquanto pela localização atraves do codigo auxiliar - Buscador de Posição 
 # que forneceu a localização X,Y do objeto a ser clicado na tela.
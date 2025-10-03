import pyautogui 
import time 

pyautogui.PAUSE = 1 #tempo de pausa de cada comando para dar tempo a maquina entender o que fazer

#comandos para abri o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#acessar o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#login no site da empresa
# selecionar o campo de email
pyautogui.click(x=685, y=451)
pyautogui.write("karlarenata@teste.com")

#selecionar o campo senha
pyautogui.press("tab")
pyautogui.write("Password")

#selecionar o botao enviar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5) #comando para esperar a pagina carregar

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv") #guardou os dados numa variavel

print(tabela) #mostrar que armazenou os dados

#cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim


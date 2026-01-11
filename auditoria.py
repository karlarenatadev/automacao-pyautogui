import pandas as pd
import os

# leitura do arquivo csv
tabela = pd.read_csv("produtos.csv")

# listas para separar os conteudos
produtos_com_erro = []
indices_remove =[]

print("Iniciando auditoria...")

for linha in tabela.index:
    
    nome = tabela.loc[linha, "marca"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    tipo = tabela.loc[linha, "tipo"]

#Regra: se o custo for maior que o valor da venda = prejuizo
if custo > preco:
    mensagem = f"Erro no produto {nome}: Custo ({custo}) maior que Venda ({preco})"
    produtos_com_erro.append(mensagem)
    indices_remove.append(linha)

#Regra para caso tenha dados nulos
elif pd.isna(tipo):
    mensagem = f"Erro no produto {nome}: O Tipo não foi preenchido."
    produtos_com_erro.append(mensagem)
    indices_remove.append(linha)

# Cria uma tabela nova só com os válidos (removendo os ruins)
tabela_valida = tabela.drop(indices_remove)
tabela_valida.to_csv("produtos_aprovados.csv", index=False)

# Cria um arquivo de texto com os erros (Log)
with open("relatorio_erros.txt", "w") as arquivo:
    for erro in produtos_com_erro:
        arquivo.write(erro + "\n")

print("Auditoria finalizada! Verifique os arquivos gerados.")

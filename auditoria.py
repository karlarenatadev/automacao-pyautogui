import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot  as plt

# criação de pastas para organização
pastas = ["Aprovados", "Reprovados", "Logs"]
for pasta in pastas:
    if not os.path.exists(pasta):
        os.mkdir(pasta)


# leitura do arquivo csv
tabela = pd.read_csv("produtos.csv")
print(f"Total de produtos analisados: {len(tabela)}")

# listas para separar os conteudos
produtos_com_erro = []
indices_remove =[]

print("Iniciando auditoria...")

for linha in tabela.index:
    
    marca = tabela.loc[linha, "marca"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    tipo = tabela.loc[linha, "tipo"]
# regra de negócio:
    erro_encontrado = False
    motivo = ""

#Regra: se o custo for maior que o valor da venda = prejuizo
    if custo > preco:
        erro_encontrado = True
        motivo = f"Prejuízo: Custo ({custo}) > Venda ({preco})"

#Regra para caso tenha dados nulos
    elif pd.isna(tipo):
        erro_encontrado = True
        motivo = 'Cadastro incompleto. Tipo Vazio!'

    if erro_encontrado:
        produtos_com_erro.append(f"Produto {marca} (Linha {linha}): {motivo}")
        indices_remove.append(linha)

# Cria uma tabela nova só com os válidos (removendo os ruins)
tabela_aprovada = tabela.drop(indices_remove)
#gera um nome único com data
timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%M")

nome_arquivo_aprovado = f"Aprovados/produtos_aprovados_{timestamp}.csv"
nome_arquivo_erros = f"Reprovados/erros_{timestamp}.txt"
nome_arquivo_kpi = f"Logs/resumo_gerencial_{timestamp}.txt"

#salvar os arquivos
tabela_aprovada.to_csv(nome_arquivo_aprovado, index=False)

# Cria um arquivo de texto com os erros (Log)
with open(nome_arquivo_erros, "w") as arquivo:
    for erro in produtos_com_erro:
        arquivo.write(erro + "\n")

#cálculo de métricas para saber o que foi aprovado
valor_estoque = tabela_aprovada["custo"].sum()
ticket_medio = tabela_aprovada["preco_unitario"].mean()
marca_top = tabela_aprovada["marca"].value_counts().idxmax()

resumo = f"""
--- RESUMO DA OPERAÇÃO ---
Data: {timestamp}
Total Processado: {len(tabela)}
Aprovados: {len(tabela_aprovada)}
Reprovados: {len(indices_remove)}

--- INDICADORES FINANCEIROS (APROVADOS) ---
Valor Total de Custo: R$ {valor_estoque:.2f}
Preço Médio de Venda: R$ {ticket_medio:.2f}
Principal Fornecedor: {marca_top}
"""

# Salvando o resumo gerencial
with open(nome_arquivo_kpi, "w", encoding='utf-8') as arquivo:
    arquivo.write(resumo)

print("Processo finalizado!")
print(f"Relatórios gerados nas pastas: {pastas}")
print(f"Resumo rápido: R$ {valor_estoque:.2f} em estoque validado.")

#gerar o gráfico 
print("Gerando gráfico gerencial...")
#preparar os dados
contagem_marcas = tabela_aprovada["marca"].value_counts()
# Criar o gráfico
plt.figure(figsize=(10, 6)) # Tamanho da imagem
contagem_marcas.plot(kind='bar', color='skyblue') # Tipo barra

plt.title("Produtos Aprovados por Marca")
plt.xlabel("Marca")
plt.ylabel("Qtd. Produtos")
plt.xticks(rotation=45) # Gira os nomes das marcas para ler melhor
plt.tight_layout() # Ajusta para não cortar textos

#salvar o gráfico
nome_arquivo_grafico = f"Logs/grafico_marcas_{timestamp}.png"
plt.savefig(nome_arquivo_grafico)
print(f"Gráfico salvo em: {nome_arquivo_grafico}")


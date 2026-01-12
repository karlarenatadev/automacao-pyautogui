# 🛡️ Auditor de Qualidade de Dados (Data Quality Pipeline)

Este projeto simula um pipeline de Engenharia de Dados focado em garantir a qualidade de uma base de produtos (Ecommerce/Varejo) antes de ela ser utilizada para análises ou inserida em banco de dados.

O script automatiza o processo de validação, separando dados corrompidos, gerando logs de erro e entregando um relatório gerencial com KPIs e gráficos.

## 💼 O Problema de Negócio
Em muitas empresas, receber bases de dados "sujas" (com preços negativos, cadastro incompleto, etc.) é comum. Processar esses dados manualmente é lento e propenso a falhas.
**Solução:** Criar um script que audita 100% das linhas em segundos e segrega o que é "Dado Confiável" do que precisa de ajuste.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12**
* **Pandas:** Manipulação e filtragem de dados (ETL).
* **Matplotlib:** Geração de gráficos para visualização de dados.
* **OS & Datetime:** Automação de sistema de arquivos e versionamento de relatórios.

## 🚀 Funcionalidades
1.  **Ingestão de Dados:** Leitura automática de arquivos CSV (`produtos.csv`).
2.  **Validação de Regras de Negócio:**
    * *Regra 1:* Verifica integridade financeira (Custo > Preço de Venda = Erro).
    * *Regra 2:* Verifica completude de cadastro (Tipo não pode ser nulo).
3.  **Segregação Automática:**
    * Move registros válidos para pasta `Aprovados`.
    * Gera logs detalhados dos erros na pasta `Reprovados`.
4.  **Reporting:**
    * Gera um resumo executivo (`.txt`) com KPIs (Valor de Estoque, Ticket Médio).
    * Plota gráfico de barras (`.png`) com a distribuição de produtos por marca.

## 📂 Estrutura do Projeto

├── auditoria.py # Script principal (ETL) 
├── produtos.csv # Base de dados bruta (Input) 
├── requirements.txt # Bibliotecas necessárias 
├── Aprovados/ # Saída dos dados limpos (CSV) 
├── Reprovados/ # Logs de erros explicativos (TXT) 
└── Logs/ # Relatórios gerenciais e Gráficos (TXT/PNG)

## 📊 Exemplo de Saída (Log Gerencial)
```text
--- RESUMO DA OPERAÇÃO ---
Data: 2025-01-11_16h00
Total Processado: 236
Aprovados: 231
Reprovados: 5

--- INDICADORES FINANCEIROS (APROVADOS) ---
Valor Total de Custo: R$ 54.300,00
Preço Médio de Venda: R$ 450,00


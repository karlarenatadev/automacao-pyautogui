import pyautogui
import time
import pandas as pd
import glob
import os
import subprocess
import sys

# Configurações globais
pyautogui.PAUSE = 0.5 
pyautogui.FAILSAFE = True 

def carregar_dados_auditados():
    """Busca o arquivo CSV mais recente na pasta Aprovados"""
    lista_arquivos = glob.glob('Aprovados/produtos_aprovados_*.csv')
    if not lista_arquivos:
        print("Erro: Nenhum arquivo encontrado.")
        sys.exit()
    arquivo_recente = max(lista_arquivos, key=os.path.getmtime)
    print(f"--- Usando base: {arquivo_recente} ---")
    return pd.read_csv(arquivo_recente)

def iniciar_sistema_ficticio():
    """Abre o ERP e dá tempo para o usuário focar a janela"""
    print("Abrindo Sistema ERP...")
    subprocess.Popen(["python", "sistema_erp.py"])
    print(">>> JANELA ABERTA. CLIQUE NO CAMPO 'CÓDIGO' AGORA!")
    time.sleep(5) 

def cadastrar_produto(linha, tabela):
    # Lista de campos sequenciais
    colunas = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]
    
    for coluna in colunas:
        valor = tabela.loc[linha, coluna]
        # interval=0.1 torna a digitação visível (simula um humano digitando)
        pyautogui.write(str(valor), interval=0.1)
        pyautogui.press("tab")
    
    # Preenchimento condicional da Observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs) and str(obs) != "nan":
        pyautogui.write(str(obs), interval=0.1)
    
    # Envio do formulário (Tab para focar no botão, Space para apertar)
    pyautogui.press("tab")   
    pyautogui.press("space") 

    print(f"Produto {linha} enviado. Aguardando limpeza...")
    time.sleep(3) 

# --- Execução Principal ---
try:
    tabela = carregar_dados_auditados()
    tabela = tabela.fillna("") # Tratamento de valores vazios
    
    iniciar_sistema_ficticio()
    
    for linha in tabela.index:
        cadastrar_produto(linha, tabela)
        
    print("\n✅ Automação finalizada com sucesso!")

except KeyboardInterrupt:
    print("\n🛑 Interrompido pelo usuário.")
except pyautogui.FailSafeException:
    print("\n🚫 Segurança ativada: Mouse encostou no canto da tela.")
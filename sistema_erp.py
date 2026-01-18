import tkinter as tk
from tkinter import messagebox

def salvar_dados():
    # Simula o salvamento pegando os dados dos campos
    dados = [
        ent_codigo.get(), ent_marca.get(), ent_tipo.get(),
        ent_categoria.get(), ent_preco.get(), ent_custo.get(), ent_obs.get()
    ]
    
    # Validação simples (só para ter feedback visual)
    if not dados[0]: # Se não tiver código
        return
        
    print(f"Produto Cadastrado: {dados}") # Mostra no terminal
    
    # Limpar campos para o próximo
    ent_codigo.delete(0, tk.END)
    ent_marca.delete(0, tk.END)
    ent_tipo.delete(0, tk.END)
    ent_categoria.delete(0, tk.END)
    ent_preco.delete(0, tk.END)
    ent_custo.delete(0, tk.END)
    ent_obs.delete(0, tk.END)
    
    # Volta o foco para o primeiro campo (Código)
    ent_codigo.focus_set()

# Configuração da Janela
janela = tk.Tk()
janela.title("Sistema ERP - Cadastro de Produtos")
janela.geometry("400x350")

# Criação dos Campos (Labels e Inputs)
campos = ["Código", "Marca", "Tipo", "Categoria", "Preço Unitário", "Custo", "Obs"]
entradas = []

for i, campo in enumerate(campos):
    tk.Label(janela, text=campo).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entrada = tk.Entry(janela, width=30)
    entrada.grid(row=i, column=1, padx=10, pady=5)
    entradas.append(entrada)

# Dando nomes às variáveis para usar na função salvar
ent_codigo, ent_marca, ent_tipo, ent_categoria, ent_preco, ent_custo, ent_obs = entradas

# Botão Salvar
btn_salvar = tk.Button(janela, text="Cadastrar Produto", command=salvar_dados, bg="green", fg="white")
btn_salvar.grid(row=8, column=0, columnspan=2, pady=20)

# Foco inicial no código
ent_codigo.focus_set()

janela.mainloop()
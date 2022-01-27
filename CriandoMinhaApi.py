from flask import Flask
import pandas as pd
import openpyxl

app = Flask(__name__) # Cria o site
tabela = pd.read_excel("Vendas - Dez.xlsx")

@app.route("/") #decorator
def fatu(): #função
    faturamento = float(tabela["Valor Final"].sum())
    return {"faturamento": faturamento}

@app.route("/vendas/produtos") #decorator
def vendas_produtos(): #função
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

@app.route("/vendas/produtos/<produto>") #decorator
def fat_produto(produto): #função
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produtos = vendas_produto.to_dict()
        return dic_vendas_produtos
    else:
        return {produto: "Inexistente"}

app.run() # Coloca o site no ar


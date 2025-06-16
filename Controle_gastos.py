# Criação de arquivo csv
from datetime import datetime
import os
import csv

os.makedirs('data', exist_ok=True)

caminho_arquivo = 'data/gastos.csv'

dados = [
    ['Data', 'Descrição', 'Valor'],
    ['14/06/2025', 'Supermercado', '150.00'],
    ['13/06/2025', 'Transporte', '20.00']
]

with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print(f"Arquivo salvo em: {'C:/Users/joaog/Desktop/Estudos/Projetos/Python/Controle_de_gastos/data'}")

## função de adicionar as movimentações

def registrar_movimentacao():
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$ "))
    data = input("Data (DD/MM/AAAA): ")
    tipo = input("Receita ou Despesa: ")

    return {
        "descricao": descricao,
        "valor": valor,
        "data": data,
        "tipo": tipo
    }
print(f"Arquivo salvo em: {'C:\Users\joaog\Desktop\Estudos\Projetos\Python\Controle_de_gastos\data\gastos.csv'}")

## Listar movimentações

def listar_movimentacoes(nome_arquivo='gastos.csv'):
    
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            print("\n" + "=" * 50)
            print("EXTRATO FINANCEIRO".center(50))
            print("=" * 50)



    
   



from datetime import datetime
import os
import csv

os.makedirs('data', exist_ok=True)
caminho_arquivo = 'data/gastos.csv'

if not os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Data', 'Descrição', 'Valor', 'Tipo'])

def registrar_movimentacao():
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$ "))
    data = input("Data (DD/MM/AAAA): ")
    tipo = input("Receita ou Despesa: ").lower()
    
    with open(caminho_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([data, descricao, valor, tipo])
    
    print("Movimentação registrada com sucesso!")

def listar_movimentacoes():
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        
        print("\n" + "=" * 50)
        print("EXTRATO FINANCEIRO".center(50))
        print("=" * 50)
        
        next(leitor)  
        for linha in leitor:
            data, descricao, valor, tipo = linha
            print(f"{data} | {descricao:20} | R${float(valor):9.2f} | {tipo}")

def mostrar_saldo():
    receitas = 0
    despesas = 0
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  
        for linha in leitor:
            valor = float(linha[2])
            if linha[3].lower() == 'receita':
                receitas += valor
            else:
                despesas += valor
    
    saldo = receitas - despesas
    
    print("\n--- SALDO ---")
    print(f"Total Receitas: R${receitas:.2f}")
    print(f"Total Despesas: R${despesas:.2f}")
    print(f"Saldo Atual: R${saldo:.2f}")


while True:
    print("\n--- CONTROLE DE GASTOS ---")
    print("1. Adicionar movimentação")
    print("2. Listar movimentações")
    print("3. Mostrar saldo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        registrar_movimentacao()
    elif opcao == '2':
        listar_movimentacoes()
    elif opcao == '3':
        mostrar_saldo()
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")


    







    
   



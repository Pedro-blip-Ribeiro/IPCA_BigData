import pandas as pd
import pymongo
from pymongo import MongoClient

#Conectar ao MongoDB
try:
    client = MongoClient('mongodb+srv://pedrotechribeiro:pedro2501@cluster0.z6kzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['big_data_ibge'] # Nome do Banco de dados
    collection = db['inflacao']
except Exception as e:
    print(f"Erro ao se conectar ao MongoDB: {e}")

# Ler o arquivo CSV
csv_ano = pd.read_csv(r'c:\Users\Lenovo\OneDrive\Documents\IPCA.prn', delimiter=r"\s+")
csv_mes_ano = pd.read_csv(r'c:\Users\Lenovo\Downloads\20241111093200.csv')

# Converte os DataFrames para dicionários
data_ano = csv_ano.to_dict(orient='records')
data_mes_ano = csv_mes_ano.to_dict(orient='records')

# Inserir dados no MongoDB
collection.insert_many(data_ano)
#collection.insert_many(data_mes_ano)

print("Dados importados com sucesso!")
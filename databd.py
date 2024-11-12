import pandas as pd
from pymongo import MongoClient

#Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['big_data_ibge'] # Nome do Banco de dados
collection = db['inflacao']

# Ler o arquivo CSV
csv_ano = pd.read_csv(r'c:\Users\Lenovo\OneDrive\Documents\IPCA.prn', delimiter="\s+")
csv_mes_ano = pd.read_csv(r'c:\Users\Lenovo\Downloads\20241111093200.csv')

# Converte os DataFrames para dicionários
data_ano = csv_ano.to_dict(orient='records')
data_mes_ano = csv_mes_ano.to_dict(orient='records')

# Inserir dados no MongoDB
collection.insert_many(data_ano)
#collection.insert_many(data_mes_ano)

print("Dados importados com sucesso!")
from pymongo import MongoClient
from dotenv import load_dotenv
import tweepy
import os
import json

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API do Twitter.
bearer_token = os.getenv('BEARER_TOKEN')

# Conexão com o MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['bd_api']
collection = db['tweets'] # Nome da coleção onde os tweets serão armazenados.

# Autenticação com a API do Twitter
twitter_client = tweepy.Client(bearer_token=bearer_token)

# Palavras-chave para buscar
keywords = ['Inteligência Artificial', '#InteligenciaArtificial', '#AI']

# Função para coletar tweets
def collect_tweets(keywords):
    for keywords in keywords:
        print(f"Coletando tweets sobre: {keywords}")
        # Quantidade e tipo a serem coletados
        tweets = twitter_client.search_recent_tweets(query=keywords, max_results=10, tweet_fields=['created_at', 'author_id', 'public_metrics'])

        if tweets.data:
            for tweet in tweets.data:
            # Estrutura para armazenar dados do tweet
                tweet_data = {
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'author_id': tweet.author_id,
                    'public_metrics': tweet.public_metrics
                }
            # Salva no MongoDB
                collection.insert_one(tweet_data)
                print(f"Tweet salvo: {tweet.text}")
        else:
            print("Nenhum tweet encontrado com a palavra-chave.")

# Executar a coleta
collect_tweets(keywords)
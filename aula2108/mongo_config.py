from pymongo import MongoClient


def mongo_connection():

    # Conectar ao MongoDB (localhost na porta padrão 27017)
    client = MongoClient("mongodb://localhost:27017/")
    # Selecionar o banco de dados e a coleção
    db = client['meu_banco_de_dados']
    colecao = db['minha_colecao']

    return colecao
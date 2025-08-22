from mongo_config import mongo_connection

con = mongo_connection()

# Exemplo de documento
documento = {
    "nome": "Roberto Cândido",
    "idade": 30,
    "profissao": "Desenvolvedor"
    }
# Inserir um único documento
resultado = con.insert_one(documento)
print("Documento inserido com o ID:", resultado.inserted_id)

# Inserir múltiplos documentos
documentos = [
{"nome": "Ana", "idade": 25, "profissao": "Engenheira"},
{"nome": "Carlos", "idade": 40, "profissao": "Arquiteto"},
{"nome": "Renan", "idade": 22, "profissao": "Analista Junior"},
{"nome": "Giovana", "idade": 21, "profissao": "Designer"}
]
resultado = con.insert_many(documentos)
print("IDs dos documentos inseridos:", resultado.inserted_ids)

# Buscar um único documento
documento = con.find_one({"nome": "Roberto Cândido"})
print("Documento encontrado:", documento)

# Buscar múltiplos documentos
documentos = con.find({"idade": {"$gt": 20}})
for doc in documentos:
    print(doc)

# Atualizar múltiplos documentos
resultado = con.update_many(
{"idade": {"$lt": 30}}, # Filtro
{"$set": {"status": "jovem"}} # Atualização
)
print("Número de documentos modificados:", resultado.modified_count)

# Atualizar um único documento
resultado = con.update_one(
{"nome": "Renan"}, # Filtro
{"$set": {"idade": 21}} # Atualização
)
print("Número de documentos modificados:", resultado.modified_count)

# Remover um único documento
resultado = con.delete_one({"nome": "José Roberto"})
print("Número de documentos deletados:", resultado.deleted_count)
# Remover múltiplos documentos
resultado = con.delete_many({"idade": {"$lt": 50}})
print("Número de documentos deletados:", resultado.deleted_count)

# Buscar todos com idade maior que 25 e profissão 'Designer' ou 'Analista'
filtro = {
"idade": {"$gt": 25},
"profissao": {"$in": ["Designer", "Analista"]}
}

resultados = con.find(filtro)
for doc in resultados:
    print(doc)

    # Buscar documentos, mas retornar apenas os campos 'nome' e 'idade'
    projecao = {"_id": 0, "nome": 1, "idade": 1}  
    # 1 para incluir, 0 para excluir
    resultados = con.find({}, projection=projecao)
    for doc in resultados:
        print(doc)
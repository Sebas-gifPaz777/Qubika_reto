import chromadb
import numpy as np
import json
def get_data():
    client = chromadb.HttpClient(host='chromadb', port=8000)
    collection_name = "news"
    collection = client.get_or_create_collection(collection_name)

    if(collection.count() == 0):
        # Cargar el archivo JSON
        with open("./docs/collection_backup.json", "r") as f:
            backup_data = json.load(f)

        # Convertir embeddings de listas a numpy arrays
        backup_data["embeddings"] = [np.array(embedding) for embedding in backup_data["embeddings"]]

        # Insertar los documentos en la nueva colección
        collection.add(
            documents=backup_data["documents"],
            metadatas=backup_data["metadatas"],
            ids=backup_data["ids"],
            embeddings=backup_data["embeddings"]
        )
    
    return collection

def query_chroma(summary, client, model):
    
    summary = model.encode(summary, show_progress_bar=False)
    results = client.query(
        query_embeddings=[summary],
        n_results=3
    )
    # Concatenar los textos relacionados
    context = "\n".join(doc for doc, metadata in zip(results["documents"], results["metadatas"]))
    return context

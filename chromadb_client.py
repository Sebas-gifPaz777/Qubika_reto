
def query_chroma(summary, client, model):
    
    summary = model.encode(summary, show_progress_bar=False)
    results = client.query(
        query_embeddings=[summary],
        n_results=1
    )
    # Concatenar los textos relacionados
    context = context = "\n".join(" ".join(doc) if isinstance(doc, list) else doc
                    for doc, metadata in zip(results["documents"], results["metadatas"]))
    return context

import re

def split_text(text, max_length=1024):
    sentences = text.split(". ")  # Dividir por oraciones
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    
    # Agregar el último fragmento
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def summarize(text, summarizer):

    news = split_text(text)
    summaries = []
    for chunk in news:
        summary = summarizer(chunk, max_length=100, min_length=50, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    final_summary = " ".join(summaries)
    
    text = final_summary.lower()  # Convertir a minúsculas
    text = re.sub(r'\s+', ' ', text)  # Normalizar espacios
    text = re.sub(r'[^\w\s]', '', text)  # Eliminar puntuación
    return final_summary,text


    
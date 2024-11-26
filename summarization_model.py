import re

def dividir_texto(texto, tamaño=2000):
    fragmentos = [texto[i:i+tamaño] for i in range(0, len(texto), tamaño)]
    return fragmentos

def split_text(text, max_length=1000):
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
    
    text = dividir_texto(text)[0]
    print(f"Text: {text}")
    news = split_text(text)
    summaries = []
    for chunk in news:
        prompt = f'Haz un resumen de esta fracción de la noticia: {chunk}'
        response = summarizer.generate_content((prompt))
        summary = response.text
        summaries.append(summary)
    final_summary = " ".join(summaries)
    
    text = final_summary.lower()  # Convertir a minúsculas
    text = re.sub(r'\s+', ' ', text)  # Normalizar espacios
    text = re.sub(r'[^\w\s]', '', text)  # Eliminar puntuación
    return final_summary,text


    
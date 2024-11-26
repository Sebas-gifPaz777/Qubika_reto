def dividir_texto(texto, tamaño=10000):
    fragmentos = [texto[i:i+tamaño] for i in range(0, len(texto), tamaño)]
    return fragmentos

def compare_texts(summary1, summary2, context1, modelGemini):
    print(f" N1: {summary1}")
    print(f" N2: {summary2}")
    print(f" CONTEXT: {context1}")
    prompt = f"Teniendo en cuenta el siguiente contexto, responder consulta: Contexto: {context1}\n Compara las dos noticias y hazlo en español: Noticia 1:{summary1}\n Noticia 2:{summary2}\nRespuesta:"
    response = modelGemini.generate_content((prompt))
    answer = response.text
    return answer
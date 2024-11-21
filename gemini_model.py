def compare_texts(summary1, summary2, context1, context2, modelGemini):
    prompt = f"A continuación tenemos los siguiente contexto separado con saltos de linea para cada noticia, las partes que esten relacionados con la consulta usalos: Contexto noticia 1{context1}\n Contexto noticia 2{context2}\n ---------------- \n Compara las dos noticias teniendo en cuenta las partes de sus contextos que son utiles y hazlo en español: Noticia 1:{summary1}\n Noticia 2:{summary2}\n --------------- \nRespuesta:"
    response = modelGemini.generate_content((prompt))
    answer = response.text
    return answer
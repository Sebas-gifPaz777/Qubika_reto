import streamlit as st
from scraping_functions import scrape_content
from summarization_model import summarize
from chromadb_client import query_chroma
from gemini_model import compare_texts
from chroma_collection import get_data
import os
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from transformers import pipeline
from gtts import gTTS
import chromadb
import json
import re 

genai.configure(api_key="AIzaSyCFma-VNWVHgNPKHrFnfuyHKc8q1t8klT0")

modelGemini = genai.GenerativeModel(
    model_name='gemini-1.5-pro',
    tools='code_execution')

model = SentenceTransformer('all-MiniLM-L6-v2')
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


client = get_data()


# Configuración de la página
st.set_page_config(page_title="Comparador de Noticias", layout="centered")

# Título
st.title("Comparador de Noticias")

# Inputs para URLs
st.markdown("### Ingresa las URLs de las noticias para comparar:")
url1 = st.text_input("URL de la noticia 1", placeholder="https://...")
url2 = st.text_input("URL de la noticia 2", placeholder="https://...")
regex = r"^https:\/\/(www\.bbc\.com\/mundo\/|www\.eltiempo\.com\/mundo\/).*"

    

# Botón para iniciar la comparación
if st.button("Comparar"):
    if url1 and url2:
        if re.match(regex, url1) & re.match(regex, url2):
        
            with st.spinner("Analizando noticias..."):
                try:
                    # Scrapeo del contenido
                    content1 = scrape_content(url1,"bbc")
                    content2 = scrape_content(url2,"el_tiempo")

                    # Resumen de los contenidos
                    summary1,process1 = summarize(content1, summarizer)
                    summary2,process2 = summarize(content2,summarizer)

                    # Consultas a ChromaDB para obtener contexto
                    context1 = query_chroma(process1, client, model)
                    context2 = query_chroma(process2, client, model)

                    # Preparar la comparación con Gemini
                    comparison_result = compare_texts(summary1, summary2, context1, context2, modelGemini)

                    os.makedirs("docs", exist_ok=True)

                    # Texto para convertir a voz
                    text = "Este es un ejemplo de narración de voz generada automáticamente."

                    # Configuración de idioma y creación del archivo de audio
                    audio_path = "docs/narracion.mp3"
                    tts = gTTS(text=text, lang='es', slow=False)
                    tts.save(audio_path)

                    st.write("Archivo de audio guardado como narracion.mp3")

                    # Reproducir el audio en Streamlit
                    st.audio(audio_path, format="audio/mp3")
                
                except Exception as e:
                    st.error(f"Error durante el proceso: {e}")
        else:
            st.warning(f"No válida una o dos de la urls")
    else:
        st.warning("Por favor, ingresa las dos URLs para comparar.")

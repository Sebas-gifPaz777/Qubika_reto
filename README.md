# Sebastián Paz - Reto de Qubika

Hola, soy **Sebastián Paz** y este es mi reto de **Qubika**. 🎯

## Instrucciones para ejecutar la aplicación:

   1. Asegúrate de tener instalado **Docker** y **Docker Compose** en tu máquina.
   2. Descarga el documento **collection_back** en esta url: [url](https://drive.google.com/file/d/1Q0zyHFbLH1MxrMb9RMxWMCh3O2215uxH/view?usp=sharing) y agregar en la carpeta docs
   3. Ejecuta el siguiente comando para construir y levantar los servicios:

   ```bash
   docker-compose up --build
   ```
   4. Ejecuta el [local](http://localhost:8501) para usarlo.
   5. Para la primera entrada de texto solo se puede ingresar articulos de este portal [BBC mundo portal](https://www.bbc.com/mundo) y para el segundo de este portal [EL TIEMPO portal](https://www.eltiempo.com/mundo)            
     
     
Nota: Cabe aclarar que, ya que se está usando Gemini como modelo para hacer la comparación y resumen de las noticias, puede llegar a presentar fallas por exceder los tokens permitidos por minuto (32,000 tokens/minuto), siendo un token 4 caracteres.  
Muchas gracias!!

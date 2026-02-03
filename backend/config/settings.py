import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def get_gemini_model():
    """
    Configura la API de Google y selecciona el mejor modelo disponible 
    que soporte la generación de contenido.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: No se encontró GEMINI_API_KEY en el archivo .env")

    # Configurar la llave de API
    genai.configure(api_key=api_key)

    try:
        # Lógica de descubrimiento de modelos (tu código original)
        available_models = [
            m.name for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        
        selected_model_name = available_models[0] if available_models else 'gemini-1.5-flash'
        
        print(f"--- Configuración Exitosa ---")
        print(f"Modelo seleccionado: {selected_model_name}")
        
        return genai.GenerativeModel(selected_model_name)
    
    except Exception as e:
        print(f"Error al listar modelos: {e}")
        # Fallback por seguridad
        return genai.GenerativeModel('gemini-1.5-flash')
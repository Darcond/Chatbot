import os
import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("--- BUSCANDO MODELOS DISPONIBLES ---")
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
print(f"Modelos encontrados: {available_models}")

selected_model = available_models[0] if available_models else 'gemini-pro'
print(f"Usando modelo: {selected_model}")

model = genai.GenerativeModel(selected_model)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(data: ChatMessage):
    try:
        user_text = data.message
        
        model_name = 'gemini-1.5-flash' 
        
        contexto = "Eres un asesor experto de un Banco. Responde de forma concisa."
        
        response = model.generate_content(f"{contexto}\nUsuario: {user_text}")
        
        return {"reply": response.text}
        
    except Exception as e:
        print(f"Error detectado: {e}")
        return {"reply": "Lo siento, tuve un problema técnico. ¿Podemos intentarlo de nuevo?"}
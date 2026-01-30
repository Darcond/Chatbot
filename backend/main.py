from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configuración de CORS para que React Native no sea bloqueado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definimos qué datos esperamos recibir del chat
class ChatMessage(BaseModel):
    message: str

@app.get("/")
def home():
    return {"mensaje": "Servidor del Chatbot encendido 🚀"}

@app.post("/chat")
async def chat(data: ChatMessage):
    # Aquí es donde el bot recibe el texto
    user_text = data.message
    return {"reply": f"Recibí tu mensaje: {user_text}"}
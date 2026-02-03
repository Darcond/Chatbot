from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Importamos nuestras piezas personalizadas
from config.settings import get_gemini_model
from services.ai_service import ChatService

# 1. Inicialización de la App
app = FastAPI(title="Davivienda ChatBot API")

# 2. Configuración de Seguridad (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Inicialización de Componentes (Inyección de dependencias simple)
# settings.py se encarga de buscar el modelo
gemini_model = get_gemini_model()
# ai_service.py se encarga de la lógica del asesor
chat_service = ChatService(gemini_model)

# 4. Modelo de datos
class ChatMessage(BaseModel):
    message: str

# 5. Punto de entrada (Endpoint)
@app.post("/chat")
async def chat(data: ChatMessage):
    # Delegamos la respuesta al servicio especializado
    reply = await chat_service.get_chat_response(data.message)
    return {"reply": reply}

# Opcional: Ruta de salud para verificar que el servidor vive
@app.get("/")
def read_root():
    return {"status": "online", "bank": "Davivienda"}
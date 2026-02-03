class ChatService:
    def __init__(self, model):
        """
        Inicia el servicio de chat con el modelo configurado.
        """
        self.model = model
        # Aquí definimos la "Personalidad" del bot (Davivienda Style)
        self.contexto = (
            "Eres un asesor experto de Davivienda. "
            "Responde de forma amable, profesional y concisa. "
            "Tu lema es 'En Davivienda, aquí lo tiene todo'."
        )

    async def get_chat_response(self, user_text: str):
        """
        Envía el mensaje a Gemini y devuelve la respuesta procesada.
        """
        try:
            # Construimos el prompt uniendo el contexto con la duda del usuario
            full_prompt = f"{self.contexto}\nUsuario: {user_text}\nAsesor:"
            
            # Llamada al método que explicamos antes
            response = self.model.generate_content(full_prompt)
            
            return response.text
            
        except Exception as e:
            print(f"Error en AI Service: {e}")
            return "Lo siento, en este momento no puedo procesar tu solicitud. Por favor, intenta más tarde."
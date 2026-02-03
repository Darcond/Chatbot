$content = @"
# ChatBot IA 🚀 (v1.0.0)

Asistente virtual inteligente. El proyecto utiliza una arquitectura desacoplada con un frontend móvil/web en **React Native** y un backend robusto en **FastAPI** integrado con la última tecnología de **Google Gemini 2.5 Flash**.

## 🏗️ Arquitectura del Sistema
El sistema se comunica mediante peticiones HTTP POST, enviando mensajes en formato JSON desde la interfaz de usuario hacia el servidor.



## 🛠️ Tecnologías Utilizadas
### Frontend
* **React Native / Expo**
* **Gifted Chat**
* **TypeScript**

### Backend
* **FastAPI**
* **Python 3.10+**
* **Google Generative AI (Gemini 2.5 Flash)**

## 🚀 Instalación
### Backend
1. Entrar a la carpeta: `cd backend`
2. Crear entorno virtual: `python -m venv .venv`
3. Activar entorno: `.\.venv\Scripts\activate`
4. Instalar librerías: `pip install fastapi uvicorn google-generativeai python-dotenv`

### Frontend
1. Entrar a la carpeta: `cd frontend`
2. Instalar librerías: `npm install`

## 🏷️ Versionamiento Semántico
Este proyecto sigue el estándar de **Semantic Versioning (SemVer)**.
* **v1.0.0**: Lanzamiento inicial.
"@; Set-Content -Path "README.md" -Value $content -Encoding utf8
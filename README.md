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

## 🏃‍♂️ Ejecución (En terminales separadas)

### 1. Iniciar el Backend (Puerto 8000)
```bash
cd backend
.\.venv\Scripts\activate
uvicorn main:app --reload
```


### 1. Iniciar el FrontEnd
```bash
cd frontend
npx expo start --web
```

* **v1.0.0**: Lanzamiento inicial.
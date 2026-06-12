# AI Study Assistant

Aplicación Streamlit para cargar PDF y generar material de estudio con IA.

## Requisitos mínimos

- Python 3.10 o superior
- `pip` instalado
- `requirements.txt` con las dependencias del proyecto

> Recomendado: use Python 3.11 o 3.12 para compatibilidad con las librerías modernas.

## Instalación y ejecución completa

1. Abrir una terminal en la carpeta del proyecto:

```powershell
cd "C:\Users\marco\Escritorio\prueba_tecnica"
```

2. Crear un entorno virtual:

```powershell
python -m venv .venv
```

3. Activar el entorno virtual:

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:

```cmd
.\.venv\Scripts\activate
```

4. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

5. Establecer variables de entorno:

PowerShell (temporal para la sesión actual):

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
$env:GEMINI_MODEL = "gemini-2.5-flash"  # opcional
```

PowerShell (persistente):

```powershell
setx GEMINI_API_KEY "your_api_key_here"
setx GEMINI_MODEL "gemini-2.5-flash"
```

Bash (Linux / macOS):

```bash
export GEMINI_API_KEY="your_api_key_here"
export GEMINI_MODEL="gemini-2.5-flash"
```

6. Ejecutar la aplicación:

```powershell
streamlit run app.py
```

## Configuración del modelo

Esta app usa el cliente Gemini y, por defecto, intentará cargar el modelo:

- `gemini-2.5-flash`

Variables de entorno disponibles:

- `GEMINI_API_KEY`: clave de API de Gemini (obligatoria)
- `GEMINI_MODEL`: nombre opcional del modelo

Si el modelo no está disponible en tu cuenta, cambia `GEMINI_MODEL` a un ID
válido proporcionado por tu proveedor.

## Comando opcional para listar modelos

Si tu librería `google-generativeai` lo soporta, puedes listar los modelos
compatibles con un comando Python corto:

```powershell
python -c "import os, google.generativeai as genai; genai.configure(api_key=os.environ['GEMINI_API_KEY']); print(genai.list_models())"
```

Si recibes un error aquí, verifica tu clave de API y revisa la documentación de tu
proveedor o dashboard para ver qué modelos están disponibles.

## Troubleshooting

- **Error: Gemini API key not found**
  - Asegúrate de tener `GEMINI_API_KEY` establecido.
  - En PowerShell, usa `$env:GEMINI_API_KEY = "your_api_key_here"` antes de ejecutar.

- **Error generando respuesta o modelo no disponible**
  - Cambia `GEMINI_MODEL` a `gemini-2.5-flash` u otro modelo soportado.
  - Revisa tu dashboard de Gemini para modelos válidos.

- **ImportError: google-generativeai library not installed**
  - Ejecuta `pip install -r requirements.txt` dentro del entorno virtual.

- **Streamlit no se encuentra**
  - Verifica que el entorno virtual esté activado.
  - Ejecuta `pip install -r requirements.txt` de nuevo.

- **Error al leer el PDF**
  - Comprueba que el archivo es un PDF válido y no está dañado.
  - Asegúrate de que el tamaño del PDF no exceda lo que el sistema pueda procesar.

- **La aplicación se queda atascada o no responde**
  - Revisa tu conexión de red.
  - Confirma que tu clave de API sigue siendo válida y que no ha expirado.

## Notas

- Esta aplicación procesa PDFs mediante `pypdf` y envía el texto a Gemini.
- La ejecución principal es `streamlit run app.py`.
- Si migras a una versión más reciente del SDK de Gemini, revisa la nueva
  documentación del cliente `google.genai`.

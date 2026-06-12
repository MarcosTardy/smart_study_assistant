# AI Study Assistant

Aplicación Streamlit para cargar PDF y generar material de estudio con IA.

## Model configuration

This project uses the Gemini LLM. To run the app you must provide your API
key and (optionally) select a model.

- `GEMINI_API_KEY`: your Gemini API key (required).
- `GEMINI_MODEL`: optional model name to use. If not set, the app defaults to
	`gemini-2.5-flash`.

If you encounter errors about a model not being available (e.g. `gemini-pro`),
switch `GEMINI_MODEL` to one of the recommended names above or consult your
provider dashboard for supported model IDs.

### Set environment variables

PowerShell (temporary for the session):

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
$env:GEMINI_MODEL = "gemini-2.5-flash"  # optional
```

PowerShell (persist across sessions):

```powershell
setx GEMINI_API_KEY "your_api_key_here"
setx GEMINI_MODEL "gemini-2.5-flash"
```

Bash (Linux / macOS):

```bash
export GEMINI_API_KEY="your_api_key_here"
export GEMINI_MODEL="gemini-2.5-flash"
```

After setting environment variables, run the app with:

```bash
streamlit run app.py
```

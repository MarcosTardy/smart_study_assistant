## smart_study_assistant
Smart_study_assistant es una solución IA cuyo objetivo es ayudar a los estudiantes. Esta herramienta genera resumenes, conceptos clave y preguntas de examen a partir de un PDF.

## 1er Prompt 
Act as a senior Python software engineer. I want to build a Streamlit application called AI Study Assistant.
The application should:
•	Allow users to upload PDF files.

•	Extract the text from the PDF.

•	Use an LLM (Gemini API) to generate a summary, key concepts and exam questions

•	Display results in separate tabs.

Requirements:
•	Use Python.

•	Use Streamlit for the UI.

•	Follow clean architecture principles.

•	Organize the code into modules.

•	Keep the project simple enough for a junior developer

•	Suggest the folder structure and responsibilities of each file.
Do not generate code yet. Only propose the architecture and development plan.


A partir de este prompt el modelo LLM me generó una arquitectura demasiado compleja, con muchas carpetas y subcarpetas para estructurar el backend de la aplicación. Decidí proponerle otra más simple. 

## 2o Prompt
You should implement a class GeminiClient:

Use an API key from environment variables (GEMINI_API_KEY).

It should have a method generate_response(text: str) -> str.

It receives text extracted from a PDF and returns a response from the model.

Do not hardcode any keys.

Include basic error handling (try/except).

Leave the code prepared so that it can later be integrated with custom prompts.

Use a clean structure and separate responsibilities.


El modelo sugería un modelo desfasado que no permitía ejecutar las funcionalidades de la aplicación. Después de estudiar los diferentes modelos se escogió implementar "gemini-2.5-flash" que es gratuito. 

## 3er Prompt
Now I need to build app.py.

Requirements:

1. Use Streamlit to create a simple but clean UI.

2. The app should allow users to:

   - Upload a PDF file

   - Click a button "Analyze PDF"

3. When clicked:

   - Extract text using pdf_reader.py

   - Send text to GeminiClient

   - Generate:
   
     - Summary

     - Key concepts

     - Exam questions

4. Display results in Streamlit tabs:

   - Tab 1: Summary

   - Tab 2: Key Concepts

   - Tab 3: Exam Questions

5. Show a loading spinner while processing.

6. Handle empty uploads gracefully.

7. Keep UI clean and minimal (no overengineering).

8. Use proper error handling so the app never crashes.

9. Keep code readable for a junior developer.

Constraints:

- Do NOT modify any other file.

- Do NOT add unnecessary complexity.

- Focus on a working MVP.

Output only the full app.py file.


Este es el script principal por lo tanto el prompt debe describir perfectamente los requisitos y las restricciones. Anterior a este se hizo otro menos detallado que no devolvia los resultados esperados. 


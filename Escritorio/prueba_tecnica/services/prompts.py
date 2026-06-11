"""Plantillas de prompts para generar resúmenes, conceptos clave y preguntas."""

SUMMARY_PROMPT = (
    "Resume el siguiente texto de forma clara y breve:\n\n" "{text}"
)

KEY_CONCEPTS_PROMPT = (
    "Extrae los conceptos clave del siguiente texto. Devuelve una lista clara:\n\n" "{text}"
)

EXAM_QUESTIONS_PROMPT = (
    "Genera preguntas de examen basadas en el siguiente texto. Incluye entre 3 y 5 preguntas:\n\n" "{text}"
)

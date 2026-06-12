"""Cliente para interactuar con la API de Gemini y generar contenido con IA."""

import os
from typing import Optional

from services.prompts import EXAM_QUESTIONS_PROMPT, KEY_CONCEPTS_PROMPT, SUMMARY_PROMPT


class GeminiClient:
    """
    Client for interacting with the Gemini API.

    Responsibilities:
    - Load API key and optional model from environment or constructor
    - Initialize and cache the model instance
    - Send formatted prompts to the model and return text responses
    """

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Initialize the Gemini client.

        Args:
            api_key: Optional API key. If not provided, loads from GEMINI_API_KEY.
            model_name: Optional model name. If not provided, loads from GEMINI_MODEL
                or falls back to a safe default.

        Raises:
            ValueError: If no API key is found.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. Set GEMINI_API_KEY environment variable"
            )

        # Allow choosing a different model via env var `GEMINI_MODEL` or constructor
        self.model_name = (
            model_name or os.getenv("GEMINI_MODEL") or "gemini-2.5-flash"
        )
        self._model = None

    def _initialize_model(self):
        """
        Initialize and cache the Gemini model instance.

        Returns:
            The initialized Gemini model object.
        """
        if self._model is not None:
            return self._model

        import google.generativeai as genai

        genai.configure(api_key=self.api_key)
        # Create and cache model instance
        self._model = genai.GenerativeModel(self.model_name)
        return self._model

    def generate_response(self, text: str) -> str:
        """
        Generate a plain text response from the Gemini model for the given prompt.

        Args:
            text: The full prompt text to send to the model.

        Returns:
            The text response from the model, or an error message string.
        """
        try:
            model = self._initialize_model()
            response = model.generate_content(text)
            return response.text if response else ""

        except ImportError:
            return "Error: google-generativeai library not installed."
        except Exception as e:
            return f"Error generating response: {e}"

    def generate_summary(self, text: str) -> str:
        """Generate a summary using the shared prompt template."""
        prompt = SUMMARY_PROMPT.format(text=text)
        return self.generate_response(prompt)

    def generate_key_concepts(self, text: str) -> str:
        """Generate key concepts using the shared prompt template."""
        prompt = KEY_CONCEPTS_PROMPT.format(text=text)
        return self.generate_response(prompt)

    def generate_exam_questions(self, text: str) -> str:
        """Generate exam questions using the shared prompt template."""
        prompt = EXAM_QUESTIONS_PROMPT.format(text=text)
        return self.generate_response(prompt)

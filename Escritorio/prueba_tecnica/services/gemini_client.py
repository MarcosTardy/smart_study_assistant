"""Cliente para interactuar con la API de Gemini y generar contenido con IA."""

import os
from typing import Optional

from .prompts import EXAM_QUESTIONS_PROMPT, KEY_CONCEPTS_PROMPT, SUMMARY_PROMPT


class GeminiClient:
    """
    Client for interacting with the Gemini API.

    Handles API key management, model initialization, and prompt-based requests.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini client with an API key.

        Args:
            api_key: Optional API key. If not provided, loads from GEMINI_API_KEY
                environment variable.

        Raises:
            ValueError: If no API key is found in arguments or environment variables.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API key not found. Please set the GEMINI_API_KEY "
                "environment variable or pass it to the constructor."
            )

        self.model_name = "gemini-pro"
        self._model = None

    def _initialize_model(self):
        """
        Initialize and cache the Gemini model instance.

        Returns:
            The initialized Gemini model.
        """
        if self._model is not None:
            return self._model

        import google.generativeai as genai

        genai.configure(api_key=self.api_key)
        self._model = genai.GenerativeModel(self.model_name)
        return self._model

    def generate_response(self, text: str) -> str:
        """
        Generate a response from the Gemini model for the given text.

        Args:
            text: The input text to send to the model.

        Returns:
            The model's response as a string.
            Returns an error message if generation fails.
        """
        try:
            model = self._initialize_model()
            response = model.generate_content(text)
            return response.text if response else ""

        except ImportError:
            return "Error: google-generativeai library not installed."
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def generate_summary(self, text: str) -> str:
        ""
        Generate a summary of the given text using the shared prompt template.
        ""
        prompt = SUMMARY_PROMPT.format(text=text)
        return self.generate_response(prompt)

    def generate_key_concepts(self, text: str) -> str:
        ""
        Generate key concepts from the given text using the shared prompt template.
        ""
        prompt = KEY_CONCEPTS_PROMPT.format(text=text)
        return self.generate_response(prompt)

    def generate_exam_questions(self, text: str) -> str:
        ""
        Generate exam questions from the given text using the shared prompt template.
        ""
        prompt = EXAM_QUESTIONS_PROMPT.format(text=text)
        return self.generate_response(prompt)

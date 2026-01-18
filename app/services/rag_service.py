import logging
from core.pipeline import PDFRAGPipeline
from core.intent_classifier import IntentClassifier
from core.retrieval_strategy import RETRIEVAL_CONFIG
from core.prompt_registry import PROMPTS
from core.intent import QueryIntent
from core.errors import (
    RetrievalError,
    GenerationError,
    IntentError
)

logger = logging.getLogger(__name__)

class RAGService:
    def __init__(self):
        self.intent_classifier = IntentClassifier()

    def _get_pipeline(self, reset: bool = False) -> PDFRAGPipeline:
        return PDFRAGPipeline(reset_vectorstore=reset)

    def ingest_pdf(self, pdf_path: str, reset: bool):
        pipeline = self._get_pipeline(reset=reset)
        pipeline.ingest_pdf(pdf_path)

    def generate(self, user_input: str) -> str:
        """
        Docstring for generate response
        
        :param self: Description
        :param user_input: Description
        :type user_input: str
        :return: Description
        :rtype: str
        """
        try:
            intent = self.intent_classifier.classify(user_input)
        except Exception:
            intent = QueryIntent.QA  # fallback intent

        pipeline = self._get_pipeline(reset=False)

        k = RETRIEVAL_CONFIG[intent]["k"]
        prompt_variant = "v1"  # configurable later
        system_instruction = PROMPTS[intent][prompt_variant]

        try:
            return pipeline.generate(
                user_input=user_input,
                system_instruction=system_instruction,
                k=k
            )
        except RetrievalError:
            logger.warning(
                "Retrieval failed",
                extra={"query": user_input, "intent": intent}
            )
            # Fallback: answer without context
            return pipeline.generator.generate(
                user_input=user_input,
                context_chunks=[],
                system_instruction=(
                    "Answer the question to the best of your ability. "
                    "State clearly if context is missing."
                )
            )
        except GenerationError:
            return (
                "I encountered an error while generating a response. "
                "Please try again later."
            )

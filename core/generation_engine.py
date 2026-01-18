from typing import List

from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage

from core.models import DocumentChunk
from core.errors import GenerationError
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class GenerationEngine:
    """
    Generic LLM-based generation engine.

    This engine generates text based on:
    - user input
    - retrieved document context
    - external instructions (prompt strategy)

    It does NOT assume Q&A, summarization, extraction, or reasoning.
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.llm_model,
            temperature=0.0,
            openai_api_key=settings.openai_api_key
        )

    def generate(
        self,
        user_input: str,
        context_chunks: List[DocumentChunk],
        system_instruction: str
    ) -> str:
        """
        Generate an LLM response based on user input and context.

        Args:
            user_input (str): User query or instruction.
            context_chunks (List[DocumentChunk]): Retrieved document chunks.
            system_instruction (str): High-level instruction defining behavior.

        Returns:
            str: Generated response.
        """
        logger.info("Generating response using LLM")

        context_text = "\n\n".join(
            f"[Page {c.metadata.get('page')}] {c.text}"
            for c in context_chunks
        )

        messages = [
            SystemMessage(content=system_instruction),
            HumanMessage(
                content=f"Context:\n{context_text}\n\nInput:\n{user_input}"
            )
        ]

        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            raise GenerationError(str(e))


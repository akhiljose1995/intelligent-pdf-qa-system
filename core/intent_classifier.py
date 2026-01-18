import re
from core.intent import QueryIntent


class IntentClassifier:
    """
    Classifies user intent using deterministic rules.

    This is intentionally simple and explainable.
    """

    def classify(self, user_input: str) -> QueryIntent:
        text = user_input.lower().strip()

        # Summarization
        if any(word in text for word in ["summarize", "summary", "overview"]):
            return QueryIntent.SUMMARY

        # Extraction
        if any(word in text for word in ["extract", "list", "find all", "identify"]):
            return QueryIntent.EXTRACTION

        # Search / discovery
        if any(word in text for word in ["find", "search", "show me"]):
            return QueryIntent.SEARCH

        # Reasoning
        if any(word in text for word in ["why", "how", "explain"]):
            return QueryIntent.REASONING

        # Default
        return QueryIntent.QA

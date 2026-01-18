from core.intent import QueryIntent


RETRIEVAL_CONFIG = {
    QueryIntent.QA: {"k": 5},
    QueryIntent.REASONING: {"k": 10},
    QueryIntent.SUMMARY: {"k": 30},
    QueryIntent.EXTRACTION: {"k": 50},
    QueryIntent.SEARCH: {"k": 5},
}

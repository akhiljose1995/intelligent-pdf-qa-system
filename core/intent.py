from enum import Enum


class QueryIntent(str, Enum):
    QA = "qa"
    SUMMARY = "summary"
    EXTRACTION = "extraction"
    REASONING = "reasoning"
    SEARCH = "search"

from core.intent import QueryIntent


PROMPTS = {
    QueryIntent.QA: {
        "v1": (
            "You are a question-answering assistant. "
            "Answer strictly using the provided context."
        ),
        "v2": (
            "Answer the question using only the context below. "
            "If the answer is missing, explicitly say so."
        ),
    },

    QueryIntent.SUMMARY: {
        "v1": (
            "Summarize the document clearly and concisely."
        ),
        "v2": (
            "Produce a structured summary highlighting key themes "
            "and conclusions."
        ),
    },

    QueryIntent.EXTRACTION: {
        "v1": (
            "Extract the requested information accurately from the context."
        )
    },
}

from core.pipeline import PDFRAGPipeline
from core.prompt_registry import PROMPTS
from core.intent import QueryIntent
from eval.eval_cases import EVAL_CASES

pipeline = PDFRAGPipeline(reset_vectorstore=False)

for case in EVAL_CASES:
    intent = QueryIntent(case["intent"])

    for variant, prompt in PROMPTS[intent].items():
        output = pipeline.generate(
            user_input=case["input"],
            system_instruction=prompt,
            k=5
        )

        print("\n---")
        print(f"Intent: {intent}, Variant: {variant}")
        print("Output:", output)

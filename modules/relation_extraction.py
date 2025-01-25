import re

RELATION_MAP = {
    r"(father of|dad of)": "dbo:father",
    r"(spouse of|married to)": "dbo:spouse",
    r"(capital of)": "dbo:capital",
    # add more patterns
}

def extract_relation(question: str) -> str:
    """
    Simple rule-based approach that checks for known phrases
    and returns a mapped relation URI/predicate.
    """
    question_lower = question.lower()
    for pattern, relation_uri in RELATION_MAP.items():
        if re.search(pattern, question_lower):
            return relation_uri
    return ""  # or a 'None' if no relation found

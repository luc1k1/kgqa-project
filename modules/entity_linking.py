import spacy
from typing import List, Dict

nlp = spacy.load("en_core_web_sm")

# Example dictionary for basic linking
ENTITY_MAP = {
    "Simba": "http://dbpedia.org/resource/Simba",
    "Mufasa": "http://dbpedia.org/resource/Mufasa",
    "Lion King": "http://dbpedia.org/resource/LionKing",
}

def extract_and_link_entities(question: str) -> Dict[str, str]:
    """
    1) Use spaCy to detect named entities.
    2) Link recognized entity text to a KG URI (if found).
    """
    doc = nlp(question)
    linked = {}
    for ent in doc.ents:
        text_lower = ent.text.strip()
        if text_lower in ENTITY_MAP:
            linked[ent.text] = ENTITY_MAP[text_lower]
        else:
            # fallback or advanced search
            pass
    return linked

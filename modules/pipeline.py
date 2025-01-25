from modules.entity_linking import extract_and_link_entities
from modules.relation_extraction import extract_relation
from modules.query_builder import build_sparql_query, execute_query
from kg.build_kg import load_graph


class KGQAPipeline:
    def __init__(self, kg_path: str):
        self.graph = load_graph(kg_path)

    def answer_question(self, question: str):
        # 1) Entity Linking
        linked_entities = extract_and_link_entities(question)
        if not linked_entities:
            return "No entities recognized or linked."

        # For simplicity, assume there's only one main entity
        entity_uri = list(linked_entities.values())[0]

        # 2) Relation Extraction
        relation_uri = extract_relation(question)
        if not relation_uri:
            return "No known relatio found in the question."

        # 3) Query
        sparql_query = build_sparql_query(entity_uri, relation_uri)
        answers = execute_query(self.graph, sparql_query)

        if len(answers) == 0:
            return "No answer found."
        else:
            return answers

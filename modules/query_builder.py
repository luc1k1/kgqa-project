from rdflib import Graph

def build_sparql_query(entity_uri: str, relation_uri: str) -> str:
    query_template = """
    SELECT ?answer WHERE {
      <ENTITY> <RELATION> ?answer .
    }
    LIMIT 10
    """
    return query_template.replace("<ENTITY>", entity_uri).replace("<RELATION>", relation_uri)

def execute_query(graph: Graph, query: str):
    results = graph.query(query)
    answers = []
    for row in results:
        answers.append(str(row["answer"]))
    return answers

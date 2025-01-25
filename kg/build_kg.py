import rdflib

def load_graph(ttl_file_path: str) -> rdflib.Graph:
    """
    Loads a Turtle file into an rdflib Graph.
    """
    g = rdflib.Graph()
    g.parse(ttl_file_path, format="turtle")
    print(f"Graph has {len(g)} triples.")
    return g

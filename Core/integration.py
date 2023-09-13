from rdflib import Graph, Namespace, RDFS, RDF, OWL, XSD, URIRef


def matching(concept_list_1, original_concept_list_1, concept_list_2, original_concept_list_2, matcher, similarity_threshold=0.6, save_path=None):
    """
    Ontology matching is the first step of ontology integration.
    We provide two types of matchers: 1. wordNet based matcher 2. LLM based matcher (see in matcher)
    :param concept_list_1: The concept list of main ontology, where there is no prefix
    :param original_concept_list_1: The concept list of associated ontology, where there is no prefix
    :param concept_list_2: The concept list of main ontology, where the prefixes are kept
    :param original_concept_list_2:The concept list of associated ontology, where the prefixes are kept
    :param matcher: the matcher
    :param similarity_threshold: similarity threshold is used to control the consequence
    :param save_path: the file path to save the generated correspondences
    :return: a graph that contains the generated correspondences
    """
    g = Graph()
    for concept_1,original_concept_1 in zip(concept_list_1, original_concept_list_1):
        max_sim = 0.
        the_original_concept_2 = None
        for concept_2, original_concept_2 in zip(concept_list_2, original_concept_list_2):
            sim = 0.
            try:
                sim = matcher.sim(concept_1, concept_2)
            except:
                continue
            if max_sim < sim:
                max_sim = sim
                the_original_concept_2 = original_concept_2
        if max_sim > similarity_threshold:
            g.add((original_concept_1, OWL['equivalentClass'], the_original_concept_2))
            g.add((the_original_concept_2, OWL['equivalentClass'], original_concept_1))
    if save_path is not None:
        g.serialize(save_path, format='ttl')
    return g


def merge():
    pass

def repair():
    pass
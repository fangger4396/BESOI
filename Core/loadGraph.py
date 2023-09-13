"""
Input: An ontology file in xml or ttl format.
Output: The concept list of the ontology

A concept of an ontology consist two part: 1. prefix; 2. name
For easy usage for later steps, every concept is split to prefix and name.
Two types of concept lists are output: 1. only contain the name; 2. contain both the prefix and the name (the original format)
A couple of function are provided to parse the ontology.
The main issue is each ontology may have its own splits and delimiters.
The user may need to develop customized functions to parse specific ontology.
"""
import rdflib

base_query = '''
select ?s where {?s a owl:Class.}
'''


def load_ontology(file, format='xml'):
    g = rdflib.Graph()
    if type(file) is type(list()):
        for f in file:
            g.parse(f, format=format)
    else:
        g.parse(file, format=format)
    return g


def camel_case_split(str):
    words = [[str[0]]]

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]


def extract_concept_list(g: rdflib.Graph, split='camel', delimiter='#'):
    extract_query = '''select ?s where {?s a/rdfs:subClassOf* owl:Class.}'''
    res = g.query(extract_query)
    concept_list = []
    original_list = []
    if split == 'camel':
        for term in res:
            if '#' in term[0]:
                temp = term[0].split(delimiter)[-1]
                concept_list.append(' '.join(camel_case_split(temp)))
                original_list.append(term[0])
    if split == '_':
        for term in res:
            if '#' in term[0]:
                temp = term[0].split(delimiter)[-1].split('_')
                if 'Setpoint' in temp:
                    temp.remove('Setpoint')
                    temp.extend(['Set', 'Point'])
                concept_list.append(' '.join(temp))
                original_list.append(term[0])
    return concept_list, original_list


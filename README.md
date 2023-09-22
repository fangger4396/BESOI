# BESOI
The BESOI is a building-energy storagy system ontology integration system.
It takes the ontologies from different domains as input, it outputs an integrated ontology.
##  Pipeline
1. Use the `load_ontology` function in `Core/loadGraph` to load the ontology in the format of .ttl or .xml.

2. Use the `matching` function in the `Core/integration` to match two input ontologies. We provide two types of matchers: 1. wordNet based matcher 2. LLM based matcher (see in matcher).
3. Use the `conflict_detect` function in `Core/integration` to find the conflict in the matched ontology.

## Installation

### Dependency
+ python 3
+ pip packages: `requirements.txt`

### Install
`git clone https://github.com/fangger4396/BESOI.git`

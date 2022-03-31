import spacy
from spacy.matcher import Matcher
import json

import pprint
pp = pprint.PrettyPrinter()

# NLP and Matcher object
nlp = spacy.load("en_core_web_trf")
matcher = Matcher(nlp.vocab)

# Define pattern class with corresponding patterns
pattern1_attention_distraction = [
    {"LOWER": {"IN": ["yes", "no", "maybe", "may"]}},
    {"POS": "PUNCT", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["agree", "thank", "thanks", "later"]}}
]

matcher.add("attention_distraction", [pattern1_attention_distraction])


# on match event handler
def on_match(doc, match_id, start, end, text_segment, segments):
    id = text_segment["id"] # segment id`
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span
    print(span.text)

# match patterns
doc = nlp("Maybe Later")
matches = matcher(doc)
for match_id, start, end in matches:
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span
    print("doc.text", doc.text)
    print("span.text", span.text)

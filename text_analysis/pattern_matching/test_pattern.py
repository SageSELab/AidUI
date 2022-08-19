import spacy
from spacy.matcher import Matcher
import json

import pprint
pp = pprint.PrettyPrinter()

# NLP and Matcher object
nlp = spacy.load("en_core_web_trf")
matcher = Matcher(nlp.vocab)

# Define pattern class with corresponding patterns
pattern8_countdown_timer = [
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}},
    {"LOWER": {"IN": [":"]}},
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}},
    {"LOWER": {"IN": [":"]}},
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}}
]

matcher.add("pattern8_countdown_timer", [pattern8_countdown_timer])


# on match event handler
def on_match(doc, match_id, start, end, text_segment, segments):
    id = text_segment["id"] # segment id`
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span
    print(span.text)

# match patterns
doc = nlp("End of Summer Sale See Discounts ! Sale starts in : 02 Days : 10 Hours : 38 Minutes : 28 Seconds")
matches = matcher(doc)
for match_id, start, end in matches:
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span
    print("doc.text", doc.text)
    print("span.text", span.text)

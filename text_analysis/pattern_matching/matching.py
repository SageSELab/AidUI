import spacy
from spacy.matcher import Matcher
import glob
import json
import patterns

# NLP and Matcher object
nlp = spacy.load("en_core_web_trf")
matcher = Matcher(nlp.vocab)

# Callback on pattern match
def on_match_callback(matcher, doc, i, matches):
    print("ocr text: ", doc) # Original OCR'd text
    match_id, start, end = matches[i]
    string_id = nlp.vocab.strings[match_id]  # Get string representation of the match ID
    span = doc[start:end]  # The matched span
    print(string_id, " : " , span.text)

# Define pattern match ID with corresponding patterns and callback
matcher.add("patterns_activity_message", patterns.patterns_activity_message, on_match=on_match_callback)
matcher.add("patterns_high_demand_message", patterns.patterns_high_demand_message, on_match=on_match_callback)
matcher.add("patterns_low_stock_message", patterns.patterns_low_stock_message, on_match=on_match_callback)
matcher.add("patterns_limited_time_message", patterns.patterns_limited_time_message, on_match=on_match_callback)
matcher.add("patterns_countdown_timer", patterns.patterns_countdown_timer, on_match=on_match_callback)
matcher.add("patterns_false_hierarchy", patterns.patterns_false_hierarchy, on_match=on_match_callback)
matcher.add("patterns_attention_distraction", patterns.patterns_attention_distraction, on_match=on_match_callback)
matcher.add("patterns_default_choice", patterns.patterns_default_choice, on_match=on_match_callback)
matcher.add("patterns_friend_spam", patterns.patterns_friend_spam, on_match=on_match_callback)
matcher.add("patterns_forced_enrollment", patterns.patterns_forced_enrollment, on_match=on_match_callback)
matcher.add("patterns_disguised_ads", patterns.patterns_disguised_ads, on_match=on_match_callback)
matcher.add("patterns_social_pyramid", patterns.patterns_social_pyramid, on_match=on_match_callback)
matcher.add("patterns_privacy_zuckering", patterns.patterns_privacy_zuckering, on_match=on_match_callback)
matcher.add("patterns_intermediate_currency", patterns.patterns_intermediate_currency, on_match=on_match_callback)
matcher.add("patterns_price_comparison_prevention", patterns.patterns_price_comparison_prevention, on_match=on_match_callback)

# Test: OCR JSON file
def match_patterns(file):
    doc = None
    f = open(file)
    data = json.load(f)
    for text_segment in data["texts"]:
        doc = nlp(text_segment["content"])
        matches = matcher(doc)

files = [file for file in glob.glob("../../UIED/data/output/ocr/" + "*.json")]
files.sort()
for file in files:
    print('----------- processing: ', file, '-------------')
    match_patterns(file)

# # Test: single sentence
# doc = nlp("decline the bonus Stone Magazine subscription Rolling to")
# matches = matcher(doc)

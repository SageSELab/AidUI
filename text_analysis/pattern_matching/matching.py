import spacy
from spacy.matcher import Matcher
import json

import text_analysis.pattern_matching.patterns as patterns

import pprint
pp = pprint.PrettyPrinter()

# NLP and Matcher object
nlp = spacy.load("en_core_web_trf")
matcher = Matcher(nlp.vocab)

# Define pattern match ID with corresponding patterns
matcher.add("patterns_activity_message", patterns.patterns_activity_message)
matcher.add("patterns_high_demand_message", patterns.patterns_high_demand_message)
matcher.add("patterns_low_stock_message", patterns.patterns_low_stock_message)
matcher.add("patterns_limited_time_message", patterns.patterns_limited_time_message)
matcher.add("patterns_countdown_timer", patterns.patterns_countdown_timer)
matcher.add("patterns_false_hierarchy", patterns.patterns_false_hierarchy)
matcher.add("patterns_attention_distraction", patterns.patterns_attention_distraction)
matcher.add("patterns_default_choice", patterns.patterns_default_choice)
matcher.add("patterns_friend_spam", patterns.patterns_friend_spam)
matcher.add("patterns_forced_enrollment", patterns.patterns_forced_enrollment)
matcher.add("patterns_disguised_ads", patterns.patterns_disguised_ads)
matcher.add("patterns_social_pyramid", patterns.patterns_social_pyramid)
matcher.add("patterns_privacy_zuckering", patterns.patterns_privacy_zuckering)
matcher.add("patterns_intermediate_currency", patterns.patterns_intermediate_currency)
matcher.add("patterns_price_comparison_prevention", patterns.patterns_price_comparison_prevention)

# on match event handler
def on_match(doc, match_id, start, end, text_segment, segments):
    id = text_segment["id"] # segment id`
    # segment_info = text_segment # segment info
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span

    # update segments object
    if id not in segments.keys():
        segments[id] = {}
        segments[id]["segment_info"] = text_segment
        segments[id]["text_analysis"] = {}
        segments[id]["text_analysis"][pattern] = {"doc": doc, "span": span.text, "span_length": len(span.text)}
    else:
        if pattern not in segments[id]["text_analysis"].keys():
            segments[id]["text_analysis"][pattern] = {"doc": doc, "span": span.text, "span_length": len(span.text)}
        else:
            current_span_length = segments[id]["text_analysis"][pattern]["span_length"]
            if(len(span.text) > current_span_length):
                segments[id]["text_analysis"][pattern] = {"doc": doc, "span": span.text, "span_length": len(span.text)}

# match patterns
def match_patterns(file):
    doc = None
    f = open(file)
    data = json.load(f)
    segments = {}
    for text_segment in data["texts"]:
        doc = nlp(text_segment["content"])
        matches = matcher(doc)
        for match_id, start, end in matches:
            on_match(doc, match_id, start, end, text_segment, segments)
    pp.pprint(segments)

import spacy
from spacy.matcher import Matcher
import json

import text_analysis.pattern_matching.patterns as patterns
from config import *

import pprint
pp = pprint.PrettyPrinter()

# NLP and Matcher object
nlp = spacy.load("en_core_web_trf")
matcher = Matcher(nlp.vocab)

# Define pattern class with corresponding patterns
matcher.add(class_dp["nagging"], patterns.patterns_nagging)
# matcher.add(class_dp["forced_continuity"], patterns.patterns_forced_continuity)
# matcher.add(class_dp["roach_motel"], patterns.patterns_roach_motel)
# matcher.add(class_dp["price_comparison_prevention"], patterns.patterns_price_comparison_prevention)
# matcher.add(class_dp["intermediate_currency"], patterns.patterns_intermediate_currency)
# matcher.add(class_dp["privacy_zuckering"], patterns.patterns_privacy_zuckering)
# matcher.add(class_dp["social_pyramid"], patterns.patterns_social_pyramid)
matcher.add(class_dp["gamification"], patterns.patterns_gamification)
# matcher.add(class_dp["forced_enrollment"], patterns.patterns_forced_enrollment)
matcher.add(class_dp["default_choice"], patterns.patterns_default_choice)
matcher.add(class_dp["attention_distraction"], patterns.patterns_attention_distraction)
matcher.add(class_dp["disguised_ads"], patterns.patterns_disguised_ads)
# matcher.add(class_dp["friend_spam"], patterns.patterns_friend_spam)
matcher.add(class_dp["countdown_timer"], patterns.patterns_countdown_timer)
matcher.add(class_dp["limited_time_message"], patterns.patterns_limited_time_message)
matcher.add(class_dp["low_stock_message"], patterns.patterns_low_stock_message)
matcher.add(class_dp["high_demand_message"], patterns.patterns_high_demand_message)
matcher.add(class_dp["activity_message"], patterns.patterns_activity_message)

# on match event handler
def on_match(doc, match_id, start, end, text_segment, segments):
    id = text_segment["id"] # segment id`
    # segment_info = text_segment # segment info
    pattern = nlp.vocab.strings[match_id]  # pattern match ID
    span = doc[start:end]  # matched span
    # print(span.text)

    # update segments object
    if str(id) not in segments.keys():
        text_segment["span"] = span.text
        segments[str(id)] = {}
        segments[str(id)]["segment_info"] = text_segment
        segments[str(id)]["text_analysis"] = {}
        segments[str(id)]["text_analysis"][pattern] = {"doc": doc.text, "span": span.text, "span_length": len(span.text)}
    else:
        if str(pattern) not in segments[str(id)]["text_analysis"].keys():
            segments[str(id)]["text_analysis"][str(pattern)] = {"doc": doc.text, "span": span.text, "span_length": len(span.text)}
        else:
            current_span_length = segments[str(id)]["text_analysis"][str(pattern)]["span_length"]
            if(len(span.text) > current_span_length):
                segments[str(id)]["text_analysis"][str(pattern)] = {"doc": doc.text, "span": span.text, "span_length": len(span.text)}

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
    return segments

# # Test: single sentence
# doc = nlp("958 viewed in last 24 hours | bbox info")
# matches = matcher(doc)
# =============================================================================================================
# # Callback on pattern match
# def on_match_callback(matcher, doc, i, matches):
#     # ranking.print_matched_pattern_info(nlp, matcher, doc, i, matches) # print matched pattern info
#     ranking.update_candidate_per_pattern(nlp, matcher, doc, i, matches) # update candidate per pattern
# =============================================================================================================
# def print_matched_pattern_info(nlp, matcher, doc, i, matches):
#     print("ocr text: ", doc) # Original OCR'd text
#     match_id, start, end = matches[i]
#     string_id = nlp.vocab.strings[match_id]  # Get string representation of the match ID
#     span = doc[start:end]  # The matched span
#     print(string_id, " : " , span.text)
# =============================================================================================================
# # global variables
# candidate_per_matchID = {}
# max_length = 0

# def update_candidate_per_pattern(nlp, matcher, doc, i, matches):
#     match_id, start, end = matches[i]
#     string_id = nlp.vocab.strings[match_id]  # Get string representation of the match ID
#     span = doc[start:end]  # The matched span
#
#     # create or update candidate per match ID
#     if string_id not in candidate_per_matchID.keys():
#         candidate_per_matchID[string_id] = {}
#         candidate_per_matchID[string_id]["length"] = len(span.text)
#         candidate_per_matchID[string_id]["text"] = span.text
#         candidate_per_matchID[string_id]["bbox"] = {}
#     else:
#         current_candidate_length = candidate_per_matchID[string_id]["length"]
#         if(len(span.text) > current_candidate_length):
#             candidate_per_matchID[string_id]["length"] = len(span.text)
#             candidate_per_matchID[string_id]["text"] = span.text
#             candidate_per_matchID[string_id]["bbox"] = {}
#     global max_length
#     max_length = candidate_per_matchID[string_id]["length"]
# =============================================================================================================
# def rank_candidates():
#     global max_length
#     # print(max_length)
#     for key, value in candidate_per_matchID.items():
#         candidate_per_matchID[key]["rank"] = value["length"] / max_length
#     pp.pprint(candidate_per_matchID)
#     utils.write_json_file(candidate_per_matchID)
# =============================================================================================================
# # JSON object from text analysis
# {'patterns_attention_distraction': {'bbox': {'column_max': 628,
#                                              'column_min': 452,
#                                              'content': 'CONTINUE',
#                                              'height': 31,
#                                              'id': 9,
#                                              'row_max': 1290,
#                                              'row_min': 1259,
#                                              'width': 176},
#                                     'length': 8,
#                                     'text': 'CONTINUE'},
#  'patterns_default_choice': {'bbox': {'column_max': 628,
#                                       'column_min': 452,
#                                       'content': 'CONTINUE',
#                                       'height': 31,
#                                       'id': 9,
#                                       'row_max': 1290,
#                                       'row_min': 1259,
#                                       'width': 176},
#                              'length': 8,
#                              'text': 'CONTINUE'},
#  'patterns_false_hierarchy': {'bbox': {'column_max': 628,
#                                        'column_min': 452,
#                                        'content': 'CONTINUE',
#                                        'height': 31,
#                                        'id': 9,
#                                        'row_max': 1290,
#                                        'row_min': 1259,
#                                        'width': 176},
#                               'length': 8,
#                               'text': 'CONTINUE'}}

# =============================================================================================================
# segments object
# {
#     "1" : {
#         "segment_info": {},
#         "text_analysis": {
#             "patterns_default_choice": {"org_text": , "matched_text":, "length":},
#             "patterns_attention_distraction": {"org_text": , "matched_text":, "length":}
#         }
#     }
# }

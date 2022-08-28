import utils.utils as utils
import text_analysis.pattern_matching.patterns as patterns
from config import *

high_contrast_patterns = [class_dp["attention_distraction"], class_dp["roach_motel"]]
high_size_diff_patterns = [class_dp["attention_distraction"], class_dp["default_choice"], class_dp["roach_motel"]]

text_pattern_candidates = [
    class_dp["activity_message"]
    , class_dp["high_demand_message"]
    , class_dp["low_stock_message"]
    , class_dp["limited_time_message"]
    , class_dp["countdown_timer"]
    , class_dp["intermediate_currency"]
    , class_dp["forced_continuity"]
    , class_dp["social_pyramid"]
    , class_dp["friend_spam"]
    , class_dp["privacy_zuckering"]
]

object_detection_candidates = [
    class_dp["nagging"]
    , class_dp["gamification"]
    , class_dp["disguised_ads"]
]

co_existing_group_1 = [
    class_dp["nagging"]
    , class_dp["disguised_ads"]
    , class_dp["default_choice"]
]

co_existing_group_2 = [
    class_dp["high_demand_message"]
    , class_dp["low_stock_message"]
    , class_dp["limited_time_message"]
]

def filter_segment_dp(segment_dp):
    segment_ids = []
    segment_contents = []
    segment_spans = []
    segment_categories = []
    selected_segment_ids = []
    selected_segment_categories = []
    for segment_id, value in segment_dp.items():
        if(class_dp["default_choice"] in value.keys()):
            segment_ids.append(segment_id)
            segment_contents.append(value[class_dp["default_choice"]]["segment_info"]["content"])
            segment_spans.append(value[class_dp["default_choice"]]["segment_info"]["span"])
            segment_categories.append(class_dp["default_choice"])
        if(class_dp["nagging"] in value.keys()):
            segment_ids.append(segment_id)
            segment_contents.append(value[class_dp["nagging"]]["segment_info"]["content"])
            segment_spans.append(value[class_dp["nagging"]]["segment_info"]["span"])
            segment_categories.append(class_dp["nagging"])
    for i in range(len(segment_contents)):
        content = segment_contents[i]
        span = segment_spans[i]
        category = segment_categories[i]
        if(category == class_dp["default_choice"]):
            if((len(span)/len(content)) < .40):
                selected_segment_ids.append(segment_ids[i])
                selected_segment_categories.append(segment_categories[i])
        else:
            if((len(span)/len(content)) < .40):
                selected_segment_ids.append(segment_ids[i])
                selected_segment_categories.append(segment_categories[i])
    # for segment_id in selected_segment_ids:
    #     segment_dp[segment_id][class_dp["default_choice"]]["score"] = 0
    for i in range(len(selected_segment_ids)):
        if(selected_segment_categories[i] == class_dp["default_choice"]):
            segment_id = selected_segment_ids[i]
            segment_dp[segment_id][class_dp["default_choice"]]["score"] = 0
        else:
            segment_id = selected_segment_ids[i]
            segment_dp[segment_id][class_dp["nagging"]]["score"] = 0
    return segment_dp

def get_labels_binarization(dps):
    # dp_predicted = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dp_predicted = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(dps) != 0:
        for dp in dps:
            index = class_dp_bin_index[dp]
            dp_predicted[index] = 1
    return dp_predicted

def predict_dp_multi_class(ui_dp, score_threshold_value):
    # score_threshold = .50
    score_threshold = score_threshold_value
    dp = []
    votes = []
    labels = []
    scores = []
    votes_above_threshold = []
    segments = []
    patterns_below_threshold = []
    scores_below_threshold = []
    votes_below_threshold = []
    segments_below_threshold = []
    # finding candidates above threshold
    for key, value in ui_dp.items():
        if value["score"] >= score_threshold:
            votes.append(value["votes"])
        else:
            patterns_below_threshold.append(key)
            scores_below_threshold.append(value["score"])
            votes_below_threshold.append(value["votes"])
            segments_below_threshold.append(value["segment_info"])
    # finding top votes
    votes.sort()
    top_votes = []
    while(len(votes) != 0):
        top_votes.append(votes.pop())
        if(len(top_votes) == 2):
            break
    # finding candidates with top votes with threshold
    if(len(top_votes) != 0):
        for vote in top_votes:
            for key, value in ui_dp.items():
                if value["votes"] == vote and value["score"] >= score_threshold and key not in labels:
                    labels.append(key)
                    segments.append(value["segment_info"])
                    scores.append(value["score"])
                    votes_above_threshold.append(value["votes"])
    # if nothing qualifies above threshold
    if(len(labels) == 0):
        if(len(patterns_below_threshold) != 0):
            # print("patterns_below_threshold", patterns_below_threshold)
            # print("segments_below_threshold", segments_below_threshold)
            # print("scores_below_threshold", scores_below_threshold)
            # print("votes_below_threshold", votes_below_threshold)
            if(patterns_below_threshold[0] not in [class_dp["default_choice"]]):
                labels.append(patterns_below_threshold[0])
                segments.append(segments_below_threshold[0])
                scores.append(scores_below_threshold[0])
                votes_above_threshold.append(votes_below_threshold[0])
            # for i in range(len(patterns_below_threshold)):
            #     if(patterns_below_threshold[0] != class_dp["default_choice"]):
            #         labels.append(patterns_below_threshold[i])
            #         segments.append(segments_below_threshold[i])
            #         scores.append(scores_below_threshold[i])
            #         votes_above_threshold.append(votes_below_threshold[i])


    ######################### filtering candidates #########################
    ########################################################################

    # removing COUNTDOWN TIMER (depending on co_existing_flag_1 & co_existing_flag_2)
    if(len(labels) != 0):
        co_existing_flag_1 = 0
        co_existing_flag_2 = 0
        if(class_dp["countdown_timer"] in labels):
            index_label_countdown_timer = labels.index(class_dp["countdown_timer"])
            for label in labels:
                if(label != class_dp["countdown_timer"] and label in co_existing_group_1):
                    co_existing_flag_1 = 1
                if(label != class_dp["countdown_timer"] and label in co_existing_group_2):
                    co_existing_flag_2 = 1
        if(co_existing_flag_1 == 1 and co_existing_flag_2 == 0):
            del labels[index_label_countdown_timer]
            del segments[index_label_countdown_timer]
            del scores[index_label_countdown_timer]
            del votes_above_threshold[index_label_countdown_timer]

    ################################ NO DP #################################
    ########################################################################
    if(len(labels) == 0):
        # print("::::::::::: NO DP :::::::::::")
        labels.append(class_dp["no_dp"])

    return {"labels": labels, "segments": segments}

def is_relative_height_beyond_threshold(height_diff_threshold, segment_height, neighbor_height):
    if abs(segment_height - neighbor_height) > height_diff_threshold:
        return True
    return False

def is_relative_width_beyond_threshold(width_diff_threshold, segment_width, neighbor_width):
    if abs(segment_width - neighbor_width) > width_diff_threshold:
        return True
    return False

def resolve_size(segment_dp_resolution, analysis_result, segment_id, neighbor):
    height_diff_threshold = 0.10
    width_diff_threshold = 0.10
    detected_patterns = list(analysis_result[segment_id]["text_analysis"].keys())
    relative_height = analysis_result[segment_id]["size_analysis"]["relative_height"]
    relative_width = analysis_result[segment_id]["size_analysis"]["relative_width"]
    for id in relative_height.keys():
        if id != segment_id and is_relative_height_beyond_threshold(height_diff_threshold, relative_height[segment_id], relative_height[id]):
            for pattern in detected_patterns:
                if pattern in high_size_diff_patterns:
                    # segment_dp_resolution[pattern]["votes"] += 0.5
                    # if(segment_dp_resolution[pattern]["votes"] < 4):
                    if(segment_dp_resolution[pattern]["votes"] + 0.5 <= 4):
                        segment_dp_resolution[pattern]["votes"] += 0.5
                    segment_dp_resolution[pattern]["vote_from"][3] = 1
    for id in relative_width.keys():
        if id != segment_id and is_relative_width_beyond_threshold(width_diff_threshold, relative_width[segment_id], relative_width[id]):
            for pattern in detected_patterns:
                if pattern in high_size_diff_patterns:
                    # segment_dp_resolution[pattern]["votes"] += 0.5
                    # if(segment_dp_resolution[pattern]["votes"] < 4):
                    if(segment_dp_resolution[pattern]["votes"] + 0.5 <= 4):
                        segment_dp_resolution[pattern]["votes"] += 0.5
                    segment_dp_resolution[pattern]["vote_from"][3] = 1
    return segment_dp_resolution

def resolve_visual(segment_dp_resolution, analysis_result, segment_id, neighbor):
    detected_patterns = list(analysis_result[segment_id]["text_analysis"].keys())
    opacity = analysis_result[segment_id]["visual_analysis"]["opacity"]
    if neighbor:
        opacity_neighbor = analysis_result[neighbor]["visual_analysis"]["opacity"]
        # if opacity != opacity_neighbor:
        if((opacity == "darker" and opacity_neighbor == "brighter") or (opacity == "brighter" and opacity_neighbor == "darker")):
            for pattern in detected_patterns:
                if pattern in high_contrast_patterns:
                    # segment_dp_resolution[pattern]["votes"] += 1
                    # if(segment_dp_resolution[pattern]["votes"] < 4):
                    if(segment_dp_resolution[pattern]["votes"] + 1 <= 4):
                        segment_dp_resolution[pattern]["votes"] += 1
                    segment_dp_resolution[pattern]["vote_from"][2] = 1
    return segment_dp_resolution

def resolve_text(segment_dp_resolution, analysis_result, segment_id, neighbor=False):
    detected_patterns = list(analysis_result[segment_id]["text_analysis"].keys())
    detected_patterns_neighbor = []
    if neighbor:
        detected_patterns_neighbor = list(analysis_result[neighbor]["text_analysis"].keys())
    for pattern in detected_patterns:
        # segment_dp_resolution[pattern] = 1
        if(pattern not in segment_dp_resolution.keys()):
            segment_dp_resolution[pattern] = {"votes": 1, "vote_from": [1, 0, 0, 0], "segment_info": analysis_result[segment_id]["segment_info"]}
        if len(detected_patterns_neighbor) != 0:
            if pattern in detected_patterns_neighbor:
                # segment_dp_resolution[pattern]["votes"] += 1
                # if(segment_dp_resolution[pattern]["votes"] < 4):
                if pattern in high_size_diff_patterns:
                    if(segment_dp_resolution[pattern]["votes"] + 1 <= 4):
                        segment_dp_resolution[pattern]["votes"] += 1
                    segment_dp_resolution[pattern]["vote_from"][1] = 1
    # print(detected_patterns_neighbor)
    return segment_dp_resolution

def resolve_segment_dp(analysis_result, segment_id):
    neighbors = analysis_result[segment_id]["proximity_analysis"]["neighbors"]
    segment_dp_resolution = {}
    # comparing with neighbors for text, visual, spatial resolve
    for neighbor in neighbors:
        segment_dp_resolution = resolve_text(segment_dp_resolution, analysis_result, segment_id, neighbor)
        segment_dp_resolution = resolve_visual(segment_dp_resolution, analysis_result, segment_id, neighbor)
        resolve_size(segment_dp_resolution, analysis_result, segment_id, neighbor)
    # text resolve if there is no neighbor
    if len(neighbors) == 0:
        segment_dp_resolution = resolve_text(segment_dp_resolution, analysis_result, segment_id)
    # score calculation for each pattern
    for pattern, value in segment_dp_resolution.items():
        score = 0
        visual_vote = False
        spatial_vote = False
        # check if there is visual and/or spatial vote
        if pattern in high_contrast_patterns:
            visual_vote = True
        if pattern in high_size_diff_patterns:
            spatial_vote = True
        # calculate score
        if visual_vote or spatial_vote:
            if visual_vote and spatial_vote:
                score = sum(value["vote_from"]) / len(value["vote_from"])
            else:
                score = sum(value["vote_from"]) / 3
        else:
            if pattern in text_pattern_candidates:
                score = value["vote_from"][0] / 1
            elif pattern in object_detection_candidates:
                score = (.90 * value["vote_from"][0]) / 1
            else:
                score = sum(value["vote_from"]) / 2
        value["score"] = score
    return segment_dp_resolution

def resolve_ui_dp(segment_dp, object_detection_result):
    ui_dp = {}
    # resolve all segments information
    for segment_dp_resolution in segment_dp.values():
        for pattern in list(segment_dp_resolution.keys()):
            if pattern in list(ui_dp.keys()):
                # ui_dp[pattern]["votes"] += segment_dp_resolution[pattern]["votes"]
                # ui_dp[pattern]["votes"] = max(ui_dp[pattern]["votes"], segment_dp_resolution[pattern]["votes"])
                # ui_dp[pattern]["score"] = max(ui_dp[pattern]["score"], segment_dp_resolution[pattern]["score"])
                if(segment_dp_resolution[pattern]["score"] > ui_dp[pattern]["score"]):
                    ui_dp[pattern]["votes"] = segment_dp_resolution[pattern]["votes"]
                    ui_dp[pattern]["score"] = segment_dp_resolution[pattern]["score"]
                    ui_dp[pattern]["segment_info"] = segment_dp_resolution[pattern]["segment_info"]
            else:
                ui_dp[pattern] = {}
                ui_dp[pattern]["votes"] = segment_dp_resolution[pattern]["votes"]
                ui_dp[pattern]["score"] = segment_dp_resolution[pattern]["score"]
                ui_dp[pattern]["segment_info"] = segment_dp_resolution[pattern]["segment_info"]
    # augment object detection information
    if object_detection_result is not None:
        for potential_dp in object_detection_result["potential_dp_classes"]:
            if potential_dp in list(ui_dp.keys()):
                ui_dp[potential_dp]["votes"] += 1
                # ui_dp[potential_dp]["score"] = (.80 * ui_dp[potential_dp]["score"]) + (.20 * object_detection_result["scores"])
                ui_dp[potential_dp]["score"] = ui_dp[potential_dp]["score"] + (.10 * object_detection_result["scores"])
            else:
                ui_dp[potential_dp] = {}
                ui_dp[potential_dp]["votes"] = 1
                # ui_dp[potential_dp]["score"] = object_detection_result["scores"]
                ui_dp[potential_dp]["score"] = .50
                row_min = object_detection_result["boxes"][0]
                column_min = object_detection_result["boxes"][1]
                row_max = object_detection_result["boxes"][2]
                column_max = object_detection_result["boxes"][3]
                ui_dp[potential_dp]["segment_info"] = {'column_min': column_min, 'height': row_max - row_min, 'row_min': row_min, 'column_max': column_max, 'width': column_max - column_min, 'row_max': row_max, 'id': 42}
    return ui_dp

def resolve_dp(input_to_resolver, score_threshold_value):
    analysis_result = input_to_resolver["analysis_result"]
    object_detection_result = input_to_resolver["object_detection_result"]
    segment_dp = {}
    for segment_id in analysis_result.keys():
        segment_dp_resolution = resolve_segment_dp(analysis_result, segment_id)
        segment_dp[segment_id] = segment_dp_resolution
    # utils.print_dictionary(segment_dp, "segment_dp")
    filter_segment_dp(segment_dp)
    ui_dp = resolve_ui_dp(segment_dp, object_detection_result)
    # utils.print_dictionary(ui_dp, "ui_dp")
    multi_class_prediction = predict_dp_multi_class(ui_dp, score_threshold_value)
    # print(dps)
    # dp_predicted = get_dp_predicted(dps)
    # print(dp_predicted)
    dp_predicted = {"labels": multi_class_prediction["labels"], "segments": multi_class_prediction["segments"], "labels_binarization": get_labels_binarization(multi_class_prediction["labels"])}
    return dp_predicted

def get_ui_dp(input_to_resolver):
    analysis_result = input_to_resolver["analysis_result"]
    object_detection_result = input_to_resolver["object_detection_result"]
    segment_dp = {}
    for segment_id in analysis_result.keys():
        segment_dp_resolution = resolve_segment_dp(analysis_result, segment_id)
        segment_dp[segment_id] = segment_dp_resolution
    utils.print_dictionary(segment_dp, "segment_dp")
    ui_dp = resolve_ui_dp(segment_dp, object_detection_result)
    return ui_dp

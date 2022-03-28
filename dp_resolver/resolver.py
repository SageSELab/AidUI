import dp_resolver.resolver_rules as resolver_rules
import utils.utils as utils
from config import *

high_contrast_patterns = [class_dp["attention_distraction"], class_dp["default_choice"]]
high_size_diff_patterns = [class_dp["attention_distraction"], class_dp["default_choice"]]

text_pattern_candidates = [
    class_dp["activity_message"]
    , class_dp["high_demand_message"]
    , class_dp["low_stock_message"]
    , class_dp["limited_time_message"]
    , class_dp["countdown_timer"]
    , class_dp["intermediate_currency"]
]

def get_dp_predicted(dps):
    dp_predicted = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(dps) != 0:
        for dp in dps:
            index = class_dp_bin_index[dp]
            dp_predicted[index] = 1
    return dp_predicted

def predict_dp_multi_class(ui_dp):
    confidence_threshold = .74
    dp = []
    votes = []
    dps = []
    for key, value in ui_dp.items():
        if value["confidence"] >= confidence_threshold:
            votes.append(value["votes"])
    votes.sort()
    top_votes = []
    while(len(votes) != 0):
        top_votes.append(votes.pop())
        if(len(top_votes) == 2):
            break
    if(len(top_votes) != 0):
        for vote in top_votes:
            for key, value in ui_dp.items():
                if value["votes"] == vote and value["confidence"] >= confidence_threshold and key not in dps:
                    dps.append(key)
    return dps

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
                    if(segment_dp_resolution[pattern]["votes"] < 4):
                        segment_dp_resolution[pattern]["votes"] += 0.5
                    segment_dp_resolution[pattern]["vote_from"][3] = 1
    for id in relative_width.keys():
        if id != segment_id and is_relative_width_beyond_threshold(width_diff_threshold, relative_width[segment_id], relative_width[id]):
            for pattern in detected_patterns:
                if pattern in high_size_diff_patterns:
                    # segment_dp_resolution[pattern]["votes"] += 0.5
                    if(segment_dp_resolution[pattern]["votes"] < 4):
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
                    if(segment_dp_resolution[pattern]["votes"] < 4):
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
            segment_dp_resolution[pattern] = {"votes": 1, "vote_from": [1, 0, 0, 0]}
        if len(detected_patterns_neighbor) != 0:
            if pattern in detected_patterns_neighbor:
                # segment_dp_resolution[pattern]["votes"] += 1
                if(segment_dp_resolution[pattern]["votes"] < 4):
                    segment_dp_resolution[pattern]["votes"] += 1
                segment_dp_resolution[pattern]["vote_from"][1] = 1
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
    # confidence calculation for each pattern
    for pattern, value in segment_dp_resolution.items():
        confidence = 0
        visual_vote = False
        spatial_vote = False
        # check if there is visual and/or spatial vote
        if pattern in high_contrast_patterns:
            visual_vote = True
        if pattern in high_size_diff_patterns:
            spatial_vote = True
        # calculate confidence
        if visual_vote or spatial_vote:
            if visual_vote and spatial_vote:
                confidence = sum(value["vote_from"]) / len(value["vote_from"])
            else:
                confidence = sum(value["vote_from"]) / 3
        else:
            if pattern in text_pattern_candidates:
                confidence = value["vote_from"][0] / 1
            else:
                confidence = sum(value["vote_from"]) / 2
        value["confidence"] = confidence
    return segment_dp_resolution

def resolve_ui_dp(segment_dp, object_detection_result):
    ui_dp = {}
    # resolve all segments information
    for segment_dp_resolution in segment_dp.values():
        for pattern in list(segment_dp_resolution.keys()):
            if pattern in list(ui_dp.keys()):
                # ui_dp[pattern]["votes"] += segment_dp_resolution[pattern]["votes"]
                ui_dp[pattern]["votes"] = max(ui_dp[pattern]["votes"], segment_dp_resolution[pattern]["votes"])
                ui_dp[pattern]["confidence"] = max(ui_dp[pattern]["confidence"], segment_dp_resolution[pattern]["confidence"])
            else:
                ui_dp[pattern] = {}
                ui_dp[pattern]["votes"] = segment_dp_resolution[pattern]["votes"]
                ui_dp[pattern]["confidence"] = segment_dp_resolution[pattern]["confidence"]
    # augment object detection information
    if object_detection_result is not None:
        for potential_dp in object_detection_result["potential_dp_classes"]:
            if potential_dp in list(ui_dp.keys()):
                ui_dp[potential_dp]["votes"] += 1
                ui_dp[potential_dp]["confidence"] = (.80 * ui_dp[potential_dp]["confidence"]) + (.20 * object_detection_result["scores"])
            # else:
            #     ui_dp[potential_dp] = {}
            #     ui_dp[potential_dp]["votes"] = 1
            #     ui_dp[potential_dp]["confidence"] = object_detection_result["scores"]
    return ui_dp

def resolve_dp(input_to_resolver):
    analysis_result = input_to_resolver["analysis_result"]
    object_detection_result = input_to_resolver["object_detection_result"]
    segment_dp = {}
    for segment_id in analysis_result.keys():
        segment_dp_resolution = resolve_segment_dp(analysis_result, segment_id)
        segment_dp[segment_id] = segment_dp_resolution
    # utils.print_dictionary(segment_dp, "segment_dp")
    ui_dp = resolve_ui_dp(segment_dp, object_detection_result)
    # utils.print_dictionary(ui_dp, "ui_dp")
    dps = predict_dp_multi_class(ui_dp)
    # print(dps)
    # dp_predicted = get_dp_predicted(dps)
    # print(dp_predicted)
    dp_predicted = {"labels": dps, "labels_binarization": get_dp_predicted(dps)}
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

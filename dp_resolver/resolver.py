import utils.utils as utils

def resolve_size():
    pass

def resolve_visual():
    pass

def resolve_text(segment_dp_resolution, analysis_result, segment_id, neighbor=False):
    detected_patterns = list(analysis_result[segment_id]["text_analysis"].keys())
    detected_patterns_neighbor = []
    if neighbor:
        detected_patterns_neighbor = list(analysis_result[neighbor]["text_analysis"].keys())
    for pattern in detected_patterns:
        segment_dp_resolution[pattern] = 1
        if len(detected_patterns_neighbor) != 0:
            if pattern in detected_patterns_neighbor:
                segment_dp_resolution[pattern] += 1
    return segment_dp_resolution

def resolve_segment_dp(analysis_result, segment_id):
    neighbors = analysis_result[segment_id]["proximity_analysis"]["neighbors"]
    segment_dp_resolution = {}
    for neighbor in neighbors:
        segment_dp_resolution = resolve_text(segment_dp_resolution, analysis_result, segment_id, neighbor)
    if len(neighbors) == 0:
        segment_dp_resolution = resolve_text(segment_dp_resolution, analysis_result, segment_id)
    return segment_dp_resolution

def resolve_ui_dp(segment_dp):
    ui_dp = {}
    for segment_dp_resolution in segment_dp.values():
        for pattern in list(segment_dp_resolution.keys()):
            if pattern in list(ui_dp.keys()):
                ui_dp[pattern] += segment_dp_resolution[pattern]
            else:
                ui_dp[pattern] = segment_dp_resolution[pattern]
    utils.print_dictionary(ui_dp)


def resolve_dp(input_to_resolver):
    analysis_result = input_to_resolver["analysis_result"]
    object_detection_result = input_to_resolver["object_detection_result"]
    segment_dp = {}
    for segment_id in analysis_result.keys():
        segment_dp_resolution = resolve_segment_dp(analysis_result, segment_id)
        segment_dp[segment_id] = segment_dp_resolution
    # utils.print_dictionary(segment_dp)
    resolve_ui_dp(segment_dp)

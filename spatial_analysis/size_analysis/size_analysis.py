def analyze_size(dictionary):
    for key, value in dictionary.items():
        size_analysis = {"relative_height": {}, "relative_weight": {}}
        heights = []
        widths = []
        max_height = 0
        max_width = 0
        height = value["segment_info"]["height"]
        width = value["segment_info"]["width"]
        heights.append(height)
        widths.append(width)

        for neighbor in value["proximity_analysis"]["neighbors"]:
            neighbor_height = dictionary[neighbor]["segment_info"]["height"]
            neighbor_width =  dictionary[neighbor]["segment_info"]["width"]
            heights.append(height)
            widths.append(width)
            max_height = max(heights)
            max_width = max(widths)

        dictionary[key]["size_analysis"] = size_analysis
    return dictionary

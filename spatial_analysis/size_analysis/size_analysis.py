def analyze_size(dictionary):
    for key, value in dictionary.items():
        heights = []
        widths = []
        max_height = 0
        max_width = 0
        height = value["segment_info"]["height"]
        width = value["segment_info"]["width"]
        size_analysis = {"relative_height": {key: height}, "relative_width": {key: width}}
        heights.append(height)
        widths.append(width)
        # populate neighbor height/width
        for neighbor in value["proximity_analysis"]["neighbors"]:
            neighbor_height = dictionary[neighbor]["segment_info"]["height"]
            neighbor_width =  dictionary[neighbor]["segment_info"]["width"]
            size_analysis["relative_height"][neighbor] = neighbor_height
            size_analysis["relative_width"][neighbor] = neighbor_width
            heights.append(neighbor_height)
            widths.append(neighbor_width)
        # max height/width in the neighborhood
        max_height = max(heights)
        max_width = max(widths)
        # calculate relative height/width
        for k, v in size_analysis.items():
            if k == "relative_height":
                for segment_id, height in v.items():
                    height = height / max_height
                    v[segment_id] = height
            else:
                for segment_id, width in v.items():
                    width = width / max_width
                    v[segment_id] = width
        # update dictionary
        dictionary[key]["size_analysis"] = size_analysis
    return dictionary

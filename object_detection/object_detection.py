def get_object_detection_result():
    dummy_object = {"label": None, "bbox_info": None}
    object_detection_result = {"detection": False, "objects": [dummy_object]}
    return object_detection_result

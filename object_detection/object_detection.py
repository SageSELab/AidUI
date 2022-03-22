from config import *
import json

# TBA: intermediate currency,  checkbox selected
object_classes = ["LIKE", "DISLIKE", "STAR", "TSON", "AD", "ADLOADER"]
map_obj_detection_dp = {
    "LIKE": [class_dp["nagging"]]
    , "DISLIKE": [class_dp["nagging"]]
    , "STAR": [class_dp["nagging"]]
    , "TSON": [class_dp["default_choice"]]
    , "AD": [class_dp["nagging"], class_dp["disguised_ads"]]
    , "ADLOADER": [class_dp["nagging"], class_dp["gamification"]]
}

def get_potential_dp_classes(label):
    object_class = object_classes[label]
    return map_obj_detection_dp[object_class]

def get_object_detection_result(ocr_filename):
    inference_output_dir = "./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_output/"
    inference_output_filename = inference_output_dir + ocr_filename.split("/")[4]
    # inference_result_filename = "./object_detection/object_detection_frcnn_mscoco_boilerplate/inference_result.json"
    try:
        # print(inference_output_filename)
        f = open(inference_output_filename)
        data = json.load(f)
        potential_dp_classes = get_potential_dp_classes(data["labels"])
        object_detection_results = {
            "boxes": data["boxes"]
            , "labels": data["labels"]
            , "scores": data["scores"]
            , "potential_dp_classes": potential_dp_classes
        }
        return object_detection_results
    except Exception as e:
        # print("exception occurred: ", e)
        object_detection_results = None
        return object_detection_results

# print("================= INFERENCE ===========================")
# with torch.no_grad():
#     correct = 0
#     total = 0
#     for images, labels in data_loader_test:
#         print("-------batch------------")
#         # pp.pprint(labels)
#         outputs = model(images)
#         print("boxes")
#         pp.pprint(outputs[0]["boxes"][0].numpy().tolist())
#         print("labels")
#         pp.pprint(outputs[0]["labels"][0].numpy().tolist())
#         print("scores")
#         pp.pprint(outputs[0]["scores"][0].numpy().tolist())
#         break
#
# ================= INFERENCE ===========================
# -------batch------------
# boxes
# [35.015377044677734, 693.7750854492188, 1080.0, 1903.0919189453125]
# labels
# 1
# scores
# 0.11882354319095612

from PIL import Image
import glob
import os
import random

import pprint
pp = pprint.PrettyPrinter()
import json

object_classes = ["LIKE", "DISLIKE", "STAR", "TSON", "AD", "ADLOADER"]

def generate_image_and_annotation(background_img, foreground_img, image_id, result):
    # read images
    img1 = Image.open(background_img)
    img2 = Image.open(foreground_img).convert("RGBA")
    # img1.show()

    # filename processing
    basename_without_ext_background_img = os.path.splitext(os.path.basename(background_img))[0]
    basename_without_ext_foreground_img = os.path.splitext(os.path.basename(foreground_img))[0]
    filename = basename_without_ext_background_img + "_" + basename_without_ext_foreground_img

    # extract class name
    object_class = basename_without_ext_foreground_img.split("_")[0]

    # random anchor position in background UI
    background_img_width = img1.size[0]
    background_img_height = img1.size[1]
    x = random.randint(64, background_img_width // 2)
    y = random.randint(64, background_img_height // 2)

    # random width/height of foreground objects
    resized_width = random.randint(64, background_img_width // 2)
    resized_height = random.randint(64, background_img_height // 2)
    size = (resized_width, resized_height)
    img2 = img2.resize(size, Image.ANTIALIAS)

    # generate superimposed UI
    img1.paste(img2, (x,y), img2)
    img1.save("output/images/" + filename + ".png","PNG")

    # populating result["images"]
    image = {}
    image["width"] = background_img_width
    image["height"] = background_img_height
    image["id"] = image_id
    image["file_name"] = "images/" + filename + ".png"
    result["images"].append(image)

    # populating result["annotations"]
    annotation = {}
    annotation["id"] = image_id
    annotation["image_id"] = image_id
    annotation["category_id"] = object_classes.index(object_class)
    annotation["segmentation"] = []
    annotation["bbox"] = [x, y, resized_width, resized_height]
    annotation["ignore"] = 0
    annotation["iscrowd"] = 0
    annotation["area"] = resized_width * resized_height
    result["annotations"].append(annotation)

def generate_synthetic_dataset():
    object_files = [file for file in glob.glob("./input/objects/" + "*.*")]
    object_files.sort()
    # print("object_files: ", object_files)
    ui_files = [file for file in glob.glob("./input/UIs/" + "*.*")]
    ui_files.sort()
    # print("ui_files: ", ui_files)

    # dictionary for image annotations
    result = {
        "images": []
        , "categories": []
        , "annotations": []
        , "info": {
            "year": 2022
            , "version": "1.0"
            , "contributor": "Label Studio"
        }}

    # populating result["categories"]
    for i in range(len(object_classes)):
        result["categories"].append({"id": i, "name": object_classes[i]})

    # generate superimposed UIs and annotations
    image_id = 0
    for i in range(len(object_files)):
        for j in range(len(ui_files)):
            foreground_img = object_files[i]
            background_img = ui_files[j]
            generate_image_and_annotation(background_img, foreground_img, image_id, result)
            print("done: ", image_id)
            image_id += 1
    # print image annotation result
    # pp.pprint(result)
    # write image annotation result
    with open('./output/result.json', 'w') as fp:
        json.dump(result, fp)

generate_synthetic_dataset()

from PIL import Image
import glob
import os

import pprint
pp = pprint.PrettyPrinter()
import json

def generate_image_and_annotation(background_img, foreground_img, image_id, result):
    # read images
    img1 = Image.open(background_img)
    img2 = Image.open(foreground_img).convert("RGBA")
    # img1.show()

    # filename processing
    basename_without_ext_background_img = os.path.splitext(os.path.basename(background_img))[0]
    basename_without_ext_foreground_img = os.path.splitext(os.path.basename(foreground_img))[0]
    filename = basename_without_ext_background_img + "_" + basename_without_ext_foreground_img

    # foreground img dimension processing
    resized_width = None
    resized_height = None
    foreground_prefix = basename_without_ext_foreground_img.split("_")[0]
    if foreground_prefix in ["like", "star", "tson", "tsoff"]:
        # we will introduce randomization
        resized_width = 64
        resized_height = 64
        size = (resized_width, resized_height)
        img2 = img2.resize(size, Image.ANTIALIAS)

    # anchor position in the background img
    x = img1.size[0] // 2
    y = img1.size[1] // 2
    # print(x,y)

    # generate superimposed UI
    img1.paste(img2, (x,y), img2)
    img1.save("output/images/" + filename + ".png","PNG")

    # populating result["images"]
    image = {}
    image["width"] = resized_width
    image["height"] = resized_height
    image["id"] = image_id
    image["file_name"] = "images/" + filename + ".png"
    result["images"].append(image)

    # # populating result["annotations"]
        {
      "id": 0,
      "image_id": 0,
      "category_id": 0,
      "segmentation": [],
      "bbox": [
        162,
        171,
        771,
        921
      ],
      "ignore": 0,
      "iscrowd": 0,
      "area": 710091
    },

    annotation = {}
    annotation["id"] = image_id
    annotation["image_id"] = image_id


def generate_synthetic_dataset():
    object_files = [file for file in glob.glob("input/objects/" + "*.*")]
    object_files.sort()
    print("object_files: ", object_files)
    ui_files = [file for file in glob.glob("input/UIs/" + "*.*")]
    ui_files.sort()
    print("ui_files: ", ui_files)

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
    categories = ["like", "star"]
    for i in range(len(categories)):
        result["categories"].append({"id": i, "name": categories[i]})

    # generate superimposed UIs and annotations
    image_id = 0
    for i in range(len(object_files)):
        for j in range(len(ui_files)):
            foreground_img = object_files[i]
            background_img = ui_files[j]
            generate_image_and_annotation(background_img, foreground_img, image_id, result)
            image_id += 1

    pp.pprint(result)

generate_synthetic_dataset()

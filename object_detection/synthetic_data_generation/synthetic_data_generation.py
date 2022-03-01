from PIL import Image
import glob
import os

def overlay_object_on_ui(background_img, foreground_img):
    # read images
    img1 = Image.open(background_img)
    img2 = Image.open(foreground_img).convert("RGBA")
    # img1.show()

    # filename processing
    basename_without_ext_background_img = os.path.splitext(os.path.basename(background_img))[0]
    basename_without_ext_foreground_img = os.path.splitext(os.path.basename(foreground_img))[0]
    filename = basename_without_ext_background_img + "_" + basename_without_ext_foreground_img

    # foreground img dimension processing
    foreground_prefix = basename_without_ext_foreground_img.split("_")[0]
    if foreground_prefix in ["like", "star", "tson", "tsoff"]:
        size = (64,64)
        img2 = img2.resize(size, Image.ANTIALIAS)

    # anchor position in the background img
    x = img1.size[0] // 2
    y = img1.size[1] // 2
    # print(x,y)

    # overlay foreground img on the background img
    img1.paste(img2, (x,y), img2)
    img1.save("output/" + filename + ".png","PNG")

def generate_synthetic_dataset():
    object_files = [file for file in glob.glob("input/objects/" + "*.*")]
    object_files.sort()
    print("object_files: ", object_files)
    ui_files = [file for file in glob.glob("input/UIs/" + "*.*")]
    ui_files.sort()
    print("ui_files: ", ui_files)

    for foreground_img in object_files:
        for background_img in ui_files:
            overlay_object_on_ui(background_img, foreground_img)

if __name__ == "__main__":
    generate_synthetic_dataset()

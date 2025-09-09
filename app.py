from PIL import Image
import os

def to_thumbnail(dir_path, img_name):
    file_path = os.path.join(dir_path,img_name)
    img = Image.open(file_path)
    width, height = img.size

    if width > height:
        new_w = 320
        new_h = int(height * (new_w/width))

    else:
        new_h = 320
        new_w = int(width * (new_h/height))

    img.thumbnail((new_w,new_h))
    img.save(f"thumbnails/thumbnail_{img_name}")

    return img_name ,new_w , new_h
 

def create_thumbnails(dir_path):
    with open("raport.txt", "w") as raport:
        for file_name in os.listdir(dir_path):
            if file_name.endswith(".jpg"):
                imgf_name, w, h = to_thumbnail(dir_path, file_name)
                raport.write(f"file name: {imgf_name} size: {w}px {h}px \n")


# Joey Hinson
# I tried to make a web app
# that searchers for your images on your PC but displays them randomly

import os
import glob
import random
from PIL import Image

def is_image_file(file_path):
    try:
        img = Image.open(file_path)
        img.close()
        return True
    except (IOError, OSError):
        return False

def search_for_images(root_folder, image_extensions=('jpg', 'jpeg', 'png', 'gif', 'bmp')):
    image_files = []
    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            file_extension = filename.split('.')[-1].lower()
            if file_extension in image_extensions:
                file_path = os.path.join(foldername, filename)
                if is_image_file(file_path):
                    image_files.append(file_path)
    return image_files

if __name__ == "__main__":
    # Replace "C:/Path/To/Your/Folder" with the root folder where you want to search for images
    # Be careful it does not filter nsfw images
    root_folder = "C:/Path/To/Your/Folder"

    image_files = search_for_images(root_folder)
    if image_files:
        print("Found images:")
        # randomly shuffle the images in the file list
        random.shuffle(image_files)
        for image_file in image_files:
            print("Displaying:", image_file)
            img = Image.open(image_file)
            img.show()
            #print(image_file)I comented this out since its a little redundant but to each theire own
    else:
        print("No images found in the specified folder.")

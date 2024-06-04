import os

def find_png_images(directory = "assets/images/") -> list:
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                images.append(os.path.join(root, file)) # replace \ with /
    return images


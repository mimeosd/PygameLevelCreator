import os

def find_png_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                images.append(os.path.join(root, file))
    return images

path = "assets/images/"
png_images = find_png_images(path)
for image in png_images:
    print(image)

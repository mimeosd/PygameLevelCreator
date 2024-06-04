import os

def find_png_images(directory="assets/images/") -> list:
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                full_path = os.path.join(root, file)
                normalized_path = full_path.replace("\\", "/")  # Normalize to forward slashes
                images.append(normalized_path)
    return images

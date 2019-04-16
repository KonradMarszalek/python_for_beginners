from pathlib import Path
from random import choice

image_directory = "/Users/kmarszalek/code/python_for_beginners/paintings/static/polls"

pattern = "*.jpg"

image_path = Path(image_directory)

images = image_path.glob(pattern)

images_names = []
for image in images:
    images_names.append(image.name)

random_image = choice(images_names)

print(random_image)










import os
from pathlib import Path
import random

from django.conf import settings
from django.shortcuts import render


def hello(request):
    relative_static_dir = os.path.join(settings.STATIC_URL.strip("/"), "polls")
    image_directory = Path(settings.BASE_DIR).joinpath(relative_static_dir)

    pattern = "*.jpg"

    image_path = Path(image_directory)

    images = image_path.glob(pattern)

    images_names = []
    for image in images:
        images_names.append("polls/" + image.name)

    random_image = random.choice(images_names)
    return render(request, 'polls/index.html', context={"dowolne": random_image})















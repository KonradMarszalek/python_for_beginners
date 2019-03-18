import os
from pathlib import Path
import random

from django.conf import settings
from django.shortcuts import render


def hello(request):
    images = []
    relative_static_dir = os.path.join(settings.STATIC_URL.strip("/"), "polls")
    absolute_static_dir = Path(settings.BASE_DIR).joinpath(relative_static_dir)
    pattern = "*.jpg"

    for image in absolute_static_dir.glob(pattern):
        images.append(image.name)

    random_image = random.choice(images)

    return render(request, 'polls/index.html', context={'random_image': os.path.join("polls", random_image)})







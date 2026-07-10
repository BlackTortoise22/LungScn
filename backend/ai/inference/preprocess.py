from PIL import Image

from torchvision import transforms

from backend.ai.config import (
    IMAGE_SIZE,
    MEAN,
    STD
)


transform = transforms.Compose([

    transforms.Resize(
        (
            IMAGE_SIZE,
            IMAGE_SIZE
        )
    ),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=MEAN,
        std=STD
    )

])


def preprocess_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    return image
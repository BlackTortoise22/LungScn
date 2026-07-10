import torch

from backend.ai.classes import (
    CLASS_NAMES,
    DISPLAY_NAMES
)

from backend.ai.inference.loader import load_model
from backend.ai.inference.preprocess import preprocess_image


def predict(image_path):

    model = load_model()

    image = preprocess_image(image_path)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )[0]

        confidence, predicted = torch.max(
            probabilities,
            dim=0
        )

    raw_class = CLASS_NAMES[
        predicted.item()
    ]

    prediction = DISPLAY_NAMES[
        raw_class
    ]

    return {

        "prediction": prediction,

        "confidence": round(
            confidence.item() * 100,
            2
        ),

        "probabilities": {

            DISPLAY_NAMES[CLASS_NAMES[i]]:
            round(probabilities[i].item() * 100, 2)

            for i in range(
                len(CLASS_NAMES)
            )

        }

    }
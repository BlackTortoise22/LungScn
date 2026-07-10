import torch

from backend.ai.models.lungnn import LungNN
from backend.ai.config import (
    MODEL_PATH,
    DEVICE
)

_model = None


def load_model():

    global _model

    if _model is None:

        _model = LungNN()

        try:
            state_dict = torch.load(
                MODEL_PATH,
                map_location=DEVICE,
                weights_only=True
            )
        except TypeError:
            # Compatibility with older PyTorch versions
            state_dict = torch.load(
                MODEL_PATH,
                map_location=DEVICE
            )

        _model.load_state_dict(state_dict)

        _model.to(DEVICE)

        _model.eval()

    return _model
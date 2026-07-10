from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR /
    "weights" /
    "LungNN2.pth"
)

IMAGE_SIZE = 224

DEVICE = "cpu"

MEAN = [
    0.485,
    0.456,
    0.406
]

STD = [
    0.229,
    0.224,
    0.225
]
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.ai.inference.predictor import predict


def main():

    image = (
        PROJECT_ROOT /
        "backend" /
        "static" /
        "uploads" /
        "sample_xray.jpg"
    )

    if not image.exists():

        print(f"❌ Image not found:\n{image}")

        return

    print("=" * 60)
    print("           LungScan AI Test")
    print("=" * 60)

    print(f"\nTesting Image:\n{image}\n")

    result = predict(image)

    print("Prediction")
    print("-" * 60)

    print(f"Disease    : {result['prediction']}")
    print(f"Confidence : {result['confidence']:.2f}%")

    print("\nClass Probabilities")
    print("-" * 60)

    for disease, probability in result["probabilities"].items():

        print(f"{disease:<25}{probability:>7.2f}%")

    print("\n✓ AI inference completed successfully.")


if __name__ == "__main__":
    main()
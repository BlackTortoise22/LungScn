import torch.nn as nn


class LungNN(nn.Module):

    def __init__(self, input_features=3):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(input_features, 32, kernel_size=3, padding="same"),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(32, 64, kernel_size=3, padding="same"),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(64, 128, kernel_size=3, padding="same"),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(128, 256, kernel_size=3, padding="same"),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(256, 512, kernel_size=3, padding="same"),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)

        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(512 * 7 * 7, 256),
            nn.ReLU(),
            nn.Dropout(0.4),

            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Dropout(0.4),

            nn.Linear(64, 5)

        )

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x
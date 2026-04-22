"""A tiny perceptron demo for an introductory AI practice project.

The program trains a perceptron to learn the AND logic gate. It uses only the
Python standard library so the repository can be cloned and run directly.
"""

from dataclasses import dataclass


@dataclass
class Perceptron:
    weights: list[float]
    bias: float
    learning_rate: float = 0.1

    def predict(self, features: list[float]) -> int:
        score = sum(weight * value for weight, value in zip(self.weights, features))
        score += self.bias
        return 1 if score >= 0 else 0

    def train(self, samples: list[tuple[list[float], int]], epochs: int = 10) -> None:
        for _ in range(epochs):
            for features, expected in samples:
                prediction = self.predict(features)
                error = expected - prediction

                for index, value in enumerate(features):
                    self.weights[index] += self.learning_rate * error * value
                self.bias += self.learning_rate * error


def main() -> None:
    training_data = [
        ([0.0, 0.0], 0),
        ([0.0, 1.0], 0),
        ([1.0, 0.0], 0),
        ([1.0, 1.0], 1),
    ]

    model = Perceptron(weights=[0.0, 0.0], bias=0.0)
    model.train(training_data, epochs=20)

    print("AND gate prediction results")
    print("-" * 28)
    for features, expected in training_data:
        prediction = model.predict(features)
        print(f"input={features}, expected={expected}, prediction={prediction}")

    print("-" * 28)
    print(f"learned weights={model.weights}, bias={model.bias:.2f}")


if __name__ == "__main__":
    main()

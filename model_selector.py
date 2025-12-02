import random

class ModelSelector:
    def __init__(self):
        self.models = {
            "naive_bayes": 0.98,
            "logistic_regression": 0.97,
            "svc": 0.96,
            "random_forest": 0.95,
            "gradient_boost": 0.94,
        }

    def choose_best(self, predictions):
        """
        predictions: dict = {model_name: predicted_disease}
        """
        scored = [
            (model, pred, self.models.get(model, 0))
            for model, pred in predictions.items()
        ]
        scored.sort(key=lambda x: x[2], reverse=True)
        best = scored[0]
        print(f"[SELECTOR] Choosing model '{best[0]}' with accuracy {best[2]}")
        return best[1]

    def random_demo(self):
        """For testing purposes only."""
        fake_preds = {m: f"Disease_{random.randint(1,5)}" for m in self.models}
        return self.choose_best(fake_preds)

if __name__ == "__main__":
    selector = ModelSelector()
    print(selector.random_demo())

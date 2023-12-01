from model_strategy import ModelStrategy

class ModelContext:
    def __init__(self, strategy: ModelStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: ModelStrategy) -> None:
        self.strategy = strategy

    def evaluate(self, frame):
        return self.strategy.evaluate(frame)


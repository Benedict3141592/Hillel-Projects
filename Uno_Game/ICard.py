class ICard:
    def __init__(self, color: str, value: int or str):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

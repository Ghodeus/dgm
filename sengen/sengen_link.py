# simple parametric “Link” class
class Link:
    def __init__(self, length: float, width: float):
        assert length > 0 and width > 0, "Dimensions must be positive"
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

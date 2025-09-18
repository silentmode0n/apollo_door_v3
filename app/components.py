class Tube():
    def __init__(self, a: int, b: int, c: int|None=None):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        if self.c:
            return f'{self.a}x{self.b}x{self.c}'
        else:
            return f'{self.a}x{self.b}'

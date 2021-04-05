class CountNum:
    def __init__(self, v=0, i=1) -> None:
        self.v = v
        self.i = i

    def count(self):
        self.v += self.i

    def __repr__(self) -> str:
        return str(self.v)

h = CountNum()
print(h.i)
print(h.v)
print(h.count)
# print(h.count())
print(h.v)

class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / 0.3048


everest = Mountain("everest", 8848)
aconcagua = Mountain("aconcagua", 6960.8)

print(Mountain.convert_height(everest), Mountain.convert_height(aconcagua))

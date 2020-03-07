class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


print(f'"{input()}" by {input()} ({input()}) hangs in the {Painting.museum}.')

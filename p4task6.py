class Furniture:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self.string = string = ''.join(str(list(self.kwargs)).strip('[').strip(']'))

    def getFurniture(self):
       
       
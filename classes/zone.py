# clase parent para crear zonas

class zone():
    name = ""
    text = ""
    image = ""
    options = {}

    def __init__(self, name, text, image, options):
        self.name = name
        self.text = text
        self.image = image
        self.options = options
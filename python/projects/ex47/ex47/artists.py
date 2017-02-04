class Art(object):

    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.colors = {}


    def paint(self, main_color):
        return self.colors.get(main_color, None)

    def add_colors(self, colors):
            self.colors.update(colors)

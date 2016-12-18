class Cell:
    def __init__(self):
        self.marker = None

    def set_marker(self, marker):
        self.marker = marker

    def __repr__(self):
        if self.marker == None:
            marker = 'None'
        else:
            marker = self.marker

        return marker


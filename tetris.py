
# interface for tetris piece 
class Tetris_piece:
    def __init__(self, shape, color):
        # shape is a list of 5 tuples
        self.shape = shape
        self.rotation = 0

    def rotate(self):
        pass

    def print(self):
        print(self.shape)
        pass
        
class L_piece:
    def __init__(self, color):
        self.color = color
        self.shape = [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 1, 1, 1, 0), (0, 1, 0, 0, 0), (0, 0, 0, 0, 0)]

    def rotate(self):
        self.rotation += 1 % 4
        # rotate shape

        pass


class I_piece:
    def __init__(self, color):
        self.color = color
        self.shape = [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 1, 1, 1, 1), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)]

    def rotate(self):
        self.rotation += 1 % 2
        # rotate shape
        
        pass

class O_piece:
    def __init__(self, color):
        self.color = color
        self.shape = [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 0), (0, 0, 0, 0, 0)]

    def rotate(self):

        pass

    def print(self):
        print(self.shape)
        pass


class Shape:
    """Docstring: This class represents a shape."""
    __area = 0

    def __init__(self):
        """Constructor: inicializa los atributos de la clase."""
        pass

    def print(self):
        """Method: imprime los atributos de la clase."""
        print(f'Area: {self.__area}')
        pass

    def getArea(self):
        return self.__area
    
    def setArea(self, area):
        self.__area = area
        pass


class Rectangle(Shape):
    """Docstring: This class represents a rectangle."""
    __height = 0
    __width = 0

    def __init__(self, height, width):
        """Constructor: inicializa los atributos de la clase."""
        self.__height = height
        self.__width = width
        self.setArea(height * width)
        pass

    def print(self):
        """Method: imprime los atributos de la clase."""
        print(f'Height: {self.__height} - Width: {self.__width} - Area: {self.getArea()}')
        pass

    def static_method():
        print('This is a static method')
        pass

    def setHeight(self, height):
        if height <= 0:
            print('Height must be greater than 0')
            pass
        self.__height = height
        # set new area
        self.setArea(height * self.__width)
        pass

    def setWidth(self, width):
        if width <= 0:
            print('Width must be greater than 0')
            pass
        self.__width = width
        # set new area
        self.setArea(self.__height * width)
        pass

    def getHeight(self):
        return self.__height
        pass

    def getWidth(self):
        return self.__width
        pass

    def getArea(self):
        return self.__area
        pass




rectangle = Rectangle(10, 20)
rectangle.print()


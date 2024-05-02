from input_validation import validate_input

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = validate_input('alto', width)
        self.height = validate_input('lado', height)

    def set_width(self, width: float):
        """Modifica el valor de ancho de una instancia de la clase Rectángulo

        Args:
            width (float): Ancho del rectángulo
        """
        self.width = validate_input('alto', width)


    def set_height(self, height: float):
        """Modifica el valor de alto de una instancia de la clase Rectángulo

        Args:
            height (float): Alto del rectángulo
        """
        self.height = validate_input('lado', height)

    def get_area(self) -> float:
        """Calcula el área del Rectángulo

        Returns:
            float: Área del Rectángulo
        """
        
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)
    
    def set_width(self, width):
        """Modifica el valor de ancho de una instancia de la clase cuadrado

        Args:
            width (float): Ancho del cuadrado
        """
        self.width = width
        self.height = width

    def set_height(self, height):
        """Modifica el valor de alto de una instancia de la clase cuadrado

        Args:
            height (float): Alto del cuadrado
        """
        self.width = height
        self.height = height


class Triangle(Rectangle):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    def get_area(self):
        """Calcula el área del Triángulo

        Returns:
            float: Área del Triángulo
        """
        return self.height * self.width / 2


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def set_radius(self, radius):
        """Modifica el valor de radio de una instancia de la clase círculo

        Args:
            width (float): Radio del círculo
        """
        pass

    def get_area(self):
        """Calcula el área del Círculo

        Returns:
            float: Área del Círculo
        """
        return 3.14 * self.radius ** 2


class Sphere(Circle):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    def get_area(self):
        """Calcula el área de la esfera

        Returns:
            float: Área de la esfera
        """
        return 4 * 3.14 * self.radius ** 2

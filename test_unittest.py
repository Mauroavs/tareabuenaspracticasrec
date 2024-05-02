import logging
import unittest
from figures import Rectangle, Square, Circle, Sphere, Triangle


class TestRectangleSquare(unittest.TestCase):

    def test_rectangle(self):
        self.assertEqual(Rectangle(5, 5).get_area(), 25.0)
        self.assertEqual(Rectangle(1, 1).get_area(), 1.0)
        self.assertEqual(Rectangle(10, 10).get_area(), 100.0)

        # area Rectangle(5,5) == 25.0
        # self.assertEqual(Rectangle(0, 0).get_area(), None)
        # self.assertEqual(Rectangle(-1, -1).get_area(), 'Negativo')

        # with self.assertLogs(level="INFO") as log:
        #     Rectangle(-5, -5).get_area()
        # self.assertEqual(log.level, logging.INFO)
        #     self.assertIn(log.output[0], 'INFO:root:negative number')

        # self.assertRaises(Rectangle("hola", "hola"), ValueError)

    def test_square(self): 
        self.assertEqual(Square(5).get_area(), 25.0) # Square(5).get_area() == 25.0
        self.assertEqual(Square(1).get_area(), 1.0)
        self.assertEqual(Square(10).get_area(), 100.0)

    def test_circle(self):
        self.assertEqual(Circle(5).get_area(), 78.5)
        self.assertEqual(Circle(1).get_area(), 3.14)
        self.assertEqual(Circle(10).get_area(), 314.00)

    def test_sphere(self):
        self.assertEqual(Sphere(5).get_area(), 314.00)
        self.assertEqual(Sphere(1).get_area(), 12.56)
        self.assertEqual(Sphere(10).get_area(), 1256)

    def test_triangle(self):
        self.assertEqual(Triangle(5, 5).get_area(), 12.5)
        self.assertEqual(Triangle(1, 1).get_area(), 0.5)
        self.assertEqual(Triangle(10, 10).get_area(), 50)


# dunder: double underscore -> d.under method
if __name__ == "__main__":
    unittest.main()

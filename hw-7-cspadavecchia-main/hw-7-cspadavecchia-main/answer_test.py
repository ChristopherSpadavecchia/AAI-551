import pytest
import answer

class TestAnswer():
    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_Q1_Rectangel_1_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.area()
        assert (result == 12)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_perimeter(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.perimeter()
        assert (result == 14)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.diagonal()
        assert (round(result,2) == 5.0)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.is_square()
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        x.resize(5,10)
        result = x.area()
        assert (result == 50)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_2_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(10,10)
        result = x.area()
        assert (result == 100)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_2_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(10,10)
        result = x.is_square()
        assert (result == True)
        TestAnswer.__correct__ += 1

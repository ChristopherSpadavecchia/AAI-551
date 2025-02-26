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


        print(f"Score:{(cls.__correct__/cls.__total__)*100}%")
        
    def test_number_x(self):
        TestAnswer.__total__ += 1
        assert(answer.tuple() == (13, 100, 7, 3, 10168, 8679)) 
        TestAnswer.__correct__ += 1


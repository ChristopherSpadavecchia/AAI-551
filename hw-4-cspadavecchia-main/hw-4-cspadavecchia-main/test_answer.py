import math
import copy
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

    def test_object_b_equal_to_a(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (b == a)
        TestAnswer.__correct__ += 1
    
    def test_obejct_b_id(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (id(b) == id(a))
        TestAnswer.__correct__ += 1
        
    def test_obejct_c_value(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (c == [1,2,[3,4,5]])
        TestAnswer.__correct__ += 1

    def test_obejct_c_id(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (id(c) != id(a))
        TestAnswer.__correct__ += 1

    def test_obejct_c_copy(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (c == copy.copy(a))
        TestAnswer.__correct__ += 1
    
    def test_obejct_d_id(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (id(d) != id(a))
        TestAnswer.__correct__ += 1

    def test_obejct_d_copy(self):
        TestAnswer.__total__ += 1
        a = [1,2,[3,4,5]]
        b, c, d, id_a = answer.objects(a)
        assert (d == copy.deepcopy(a))
        TestAnswer.__correct__ += 1
    
    def test_prime_test_1(self):
        TestAnswer.__total__ += 1
        number = 10
        num = answer.prime_number(number)
        assert(num == [2,3,5,7])
        TestAnswer.__correct__ += 1

    def test_prime_test_2(self):
        TestAnswer.__total__ += 1
        number = 100
        num = answer.prime_number(number)
        assert(num == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        TestAnswer.__correct__ += 1
    
    def test_prime_test_3(self):
        TestAnswer.__total__ += 1
        number = 3
        num = answer.prime_number(number)
        assert(num == [2])
        TestAnswer.__correct__ += 1
    
    def test_while_loop_calculation_1(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("3")
        assert(output == 6)
        TestAnswer.__correct__ += 1

    def test_while_loop_calculation_2(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("10")
        assert(output == 55)
        TestAnswer.__correct__ += 1
    
    def test_while_loop_calculation_3(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("100")
        assert(output == 5050)
        TestAnswer.__correct__ += 1

    def test_while_loop_zero(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("0")
        assert(output == 0)
        TestAnswer.__correct__ += 1  

    def test_while_loop_not_number(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("Hello")
        assert(output == "Error")
        TestAnswer.__correct__ += 1 

    def test_while_loop_decimal_number(self):
        TestAnswer.__total__ += 1
        output = answer.while_loop("1.1")
        assert(output == "Error")
        TestAnswer.__correct__ += 1


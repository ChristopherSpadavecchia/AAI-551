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

    def test_Q1_normal_list_1(self):
        TestAnswer.__total__ += 1
        test_list = [1, 2, 3, 4, 5, 6]
        output = answer.filter_even(test_list)
        assert(output == [2, 4, 6])
        TestAnswer.__correct__ += 1

    def test_Q1_normal_list_2(self):
        TestAnswer.__total__ += 1
        test_list = [10, 10, 10, 20, 21, 20]
        output = answer.filter_even(test_list)
        assert(output == [10, 10, 10, 20, 20])
        TestAnswer.__correct__ += 1

    def test_Q1_normal_list_3(self):
        TestAnswer.__total__ += 1
        test_list = [20,21,22,23]
        output = answer.filter_even(test_list)
        assert(output == [20, 22])
        TestAnswer.__correct__ += 1

    def test_Q1_empty_list(self):
        TestAnswer.__total__ += 1
        test_list = []
        output = answer.filter_even(test_list)
        assert(output == [])
        TestAnswer.__correct__ += 1

    def test_Q2_normal_list_1(self):
        TestAnswer.__total__ += 1
        test_list = [1, 2, 3, 4, 5, 6]
        output = answer.reduce_function(test_list)
        assert(output == 720)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_list_2(self):
        TestAnswer.__total__ += 1
        test_list = [7,8,9,10]
        output = answer.reduce_function(test_list)
        assert(output == 5040)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_list_3(self):
        TestAnswer.__total__ += 1
        test_list = [100,200,300]
        output = answer.reduce_function(test_list)
        assert(output == 6000000)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_list_4(self):
        TestAnswer.__total__ += 1
        test_list = [100,200,3,300]
        output = answer.reduce_function(test_list)
        assert(output == 18000000)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_list_5(self):
        TestAnswer.__total__ += 1
        test_list = [1]
        output = answer.reduce_function(test_list)
        assert(output == 1)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_list_1(self):
        TestAnswer.__total__ += 1
        test_list = "8999921111116"
        output = answer.largestGoodInteger(test_list)
        assert(output == '9999')
        TestAnswer.__correct__ += 1

    def test_Q3_normal_list_2(self):
        TestAnswer.__total__ += 1
        test_list = "6498888132"
        output = answer.largestGoodInteger(test_list)
        assert(output == '8888')
        TestAnswer.__correct__ += 1

    def test_Q3_normal_list_3(self):
        TestAnswer.__total__ += 1
        test_list = "89454648126666"
        output = answer.largestGoodInteger(test_list)
        assert(output == '6666')
        TestAnswer.__correct__ += 1

    def test_Q3_empty_output(self):
        TestAnswer.__total__ += 1
        test_list = "89454648126"
        output = answer.largestGoodInteger(test_list)
        assert(output == '')
        TestAnswer.__correct__ += 1

    def test_Q3_empty_list(self):
        TestAnswer.__total__ += 1
        test_list = ""
        output = answer.largestGoodInteger(test_list)
        assert(output == '')
        TestAnswer.__correct__ += 1

    def test_Q4_normal_list_1(self):
        TestAnswer.__total__ += 1
        test_list = [-4,-2,1,4,8]
        output = answer.findClosestNumber(test_list)
        assert(output == 1)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_list_2(self):
        TestAnswer.__total__ += 1
        test_list = [2,-1,1]
        output = answer.findClosestNumber(test_list)
        assert(output == 1)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_list_3(self):
        TestAnswer.__total__ += 1
        test_list = [2,-1,2]
        output = answer.findClosestNumber(test_list)
        assert(output == -1)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_list_4(self):
        TestAnswer.__total__ += 1
        test_list = [0]
        output = answer.findClosestNumber(test_list)
        assert(output == 0)
        TestAnswer.__correct__ += 1

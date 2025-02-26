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

    def test_Q1_normal_list(self):
        TestAnswer.__total__ += 1
        test_list = [10, 5, 20, 15, 25]
        output = answer.find_maximum(test_list)
        assert(output == 25)
        TestAnswer.__correct__ += 1
    
    def test_Q1_same_number_list(self):
        TestAnswer.__total__ += 1
        test_list = [10, 10, 10, 10]
        output = answer.find_maximum(test_list)
        assert(output == 10)
        TestAnswer.__correct__ += 1
                            
    def test_Q1_empty_list(self):
        TestAnswer.__total__ += 1
        test_list = []
        output = answer.find_maximum(test_list)
        assert(output == None)
        TestAnswer.__correct__ += 1

    def test_Q2_Input_0(self):
        TestAnswer.__total__ += 1
        test_num = 0
        output = answer.generateParenthesis(test_num)

        assert(output == [''])
        TestAnswer.__correct__ += 1

    def test_Q2_Input_1(self):
        TestAnswer.__total__ += 1
        test_num = 1
        output = answer.generateParenthesis(test_num)
        assert(output == ['()'])
        TestAnswer.__correct__ += 1
    
    def test_Q2_Input_2(self):
        TestAnswer.__total__ += 1
        test_num = 2
        output = answer.generateParenthesis(test_num)
        assert(output == ['(())', '()()'])
        TestAnswer.__correct__ += 1
    
    def test_Q2_Input_3(self):
        TestAnswer.__total__ += 1
        test_num = 3
        output = answer.generateParenthesis(test_num)
        assert(output == ['((()))', '(()())', '(())()', '()(())', '()()()'])
        TestAnswer.__correct__ += 1
    
    def test_Q2_Input_4(self):
        TestAnswer.__total__ += 1
        test_num = 4
        output = answer.generateParenthesis(test_num)
        assert(output == ['(((())))','((()()))','((())())','((()))()','(()(()))','(()()())',
                          '(()())()','(())(())','(())()()','()((()))','()(()())','()(())()','()()(())','()()()()'])
        TestAnswer.__correct__ += 1  
    
    def test_Q2_Input_3(self):
        TestAnswer.__total__ += 1
        test_num = 3
        output = answer.generateParenthesis(test_num)
        assert(output == ['((()))', '(()())', '(())()', '()(())', '()()()'])
        TestAnswer.__correct__ += 1      
    
    def test_Q3_normal_list(self):
        TestAnswer.__total__ += 1
        test_str= "A man, a plan, a canal: Panama"
        output = answer.isPalindrome(test_str)
        assert(output == True)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_list_2(self):
        TestAnswer.__total__ += 1
        test_str= "Was it a car or a cat I saw?"
        output = answer.isPalindrome(test_str)
        assert(output == True)
        TestAnswer.__correct__ += 1

    def test_Q3_empty_list(self):
        TestAnswer.__total__ += 1
        test_str= ""
        output = answer.isPalindrome(test_str)
        assert(output == True)
        TestAnswer.__correct__ += 1

    def test_Q3_wrong_list(self):
        TestAnswer.__total__ += 1
        test_str= "hello"
        output = answer.isPalindrome(test_str)
        assert(output == False)
        TestAnswer.__correct__ += 1    

    def test_Q3_wrong_list_2(self):
        TestAnswer.__total__ += 1
        test_str= "race a car"
        output = answer.isPalindrome(test_str)
        assert(output == False)
        TestAnswer.__correct__ += 1   

    def test_Q3_str_num_true(self):
        TestAnswer.__total__ += 1
        test_str= "1234321"
        output = answer.isPalindrome(test_str)
        assert(output == True)
        TestAnswer.__correct__ += 1   
    
    def test_Q3_str_num_wrong(self):
        TestAnswer.__total__ += 1
        test_str= "1234321a"
        output = answer.isPalindrome(test_str)
        assert(output == False)
        TestAnswer.__correct__ += 1   
    

"""
QUESTION 1:
========================================================================================================
Given a list of numbers, write a function to find the maximum number in the list.
Do Not Use the built-in Python function max.
Note: For the purpose of this problem, we define that an empty list will return None.

NOTE: DO NOT USE THE PYTHON FUNCTION max. WRITE your program using a loop. 

Example 1:
========================================
Input: [10, 5, 20, 15, 25]
Output: 25

Example 2:
========================================
Input:[10,10,10]
Output: 10

Example 3:
========================================
Input: []
Output: None
"""

def find_maximum(numbers):
    if not numbers:  # Check if the list is empty
        return None
    
    maximum = numbers[0]  # Start with the first number as the maximum
    for number in numbers:
        if number > maximum:
            maximum = number  # Update maximum if a larger number is found

    return maximum

"""
QUESTION 2: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.

Example 1:
========================================
Input: 0
Output: ['']

Example 2:
========================================
Input: 1
Output: ['()']

Example 3:
========================================
Input: 2
Output: ['(())', '()()']

Example 4:
========================================
Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()'])
"""

def generateParenthesis(n):
    parens = []  # Initialize the list of combinations
    generate('', n, n, parens)  # Start the generation process
    return parens  # Return the list of valid parentheses combinations

def generate(p, left, right, parens):
        if left > 0:  # Check if there are left parentheses to add
            generate(p + '(', left - 1, right, parens)
        if right > left:  # Check if there are right parentheses to add
            generate(p + ')', left, right - 1, parens)
        if right == 0:  # If no right parentheses left, a valid combination is formed
            parens.append(p)  # Corrected to append to the list

"""
QUESTION 3: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome. Write a function
named isPalindrome that takes a string as an input and returns a bool as an output.

Hint: refer to the following example on how to reverse a string.

>>> S = "abc"
>>> S[::-1]
'cba'


Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  amanaplanacanalPanama
which reads the same as backward and forward, so it is true.

Example 2:
=========================================
Input: "race a car"
Output: false

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  raceacar
which does not read the same as backward and forward, so it is false.
"""

def isPalindrome(x):
    filtered = ''.join(char.lower() for char in x if char.isalnum())
    
    # Reverse the filtered string
    reversed_filtered = filtered[::-1]
    
    # Check if the filtered string is equal to its reverse
    return filtered == reversed_filtered
    

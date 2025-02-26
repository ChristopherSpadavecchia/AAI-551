import pytest
import answer

def test_number():
    x, y = answer.number()
    assert x == 4 ** 5
    assert y == x / 3

def test_strings():
    stevens, stevens_7, length, great, good = answer.strings()
    assert stevens == "stevens"
    assert stevens_7 == "stevens" * 7
    assert length == len(stevens_7)
    assert great == "stevens is great"
    assert good == "stevens is good"

def test_list_1D():
    hoboken, hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
    assert hoboken == "hoboken,is,awesome,i,like,it"
    assert hoboken_list == ["hoboken", "is", "awesome", "i", "like", "it"]
    assert hoboken_first_item == "hoboken"
    assert l == sorted([2, 3, 4, 1, 5, 6, 9, 10, 15, 12, 13, -2, -6, 0, 0])
    assert new_l == sorted([2, 3, 4, 1, 5, 6, 9, 10, 15, 12, 13, -2, -6, 0, 0])[3:10]

def test_list_2D():
    A, last_column, a, b = answer.list_2D()
    assert A == [
        [1, 4, 5],
        [6, 10, 11],
        [12, 17, 38]
    ]
    assert last_column == [5, 11, 38]
    assert a == 38
    assert b == 6

def test_dictionary():
    fruit_dict, f = answer.dictionary()
    assert fruit_dict == {"fruit": "apple", "quantity": 19, "color": "red"}
    assert f == "apple"

def test_dictionary_nested():
    Grace, last_name, job = answer.dictionary_nested()
    assert Grace == {
        "name": {"first_name": "Grace", "last_name": "Hopper"},
        "jobs": ["scientist", "engineer", "programmer"],
        "age": 85
    }
    assert last_name == "Hopper"
    assert job == "programmer"
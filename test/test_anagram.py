from src.main import group_anagrams
import pytest

@pytest.mark.parametrize("test_keywords, expected", [
    (() , []), (("eat",), [["eat"]]), (("abc", "cab", "bac"),  [["abc", "cab", "bac"]])] )

def test_group_anagrams(test_keywords, expected):
    result = group_anagrams(test_keywords)
    assert result == expected


from src.main import group_anagrams

def test_anagrams():
    test_keywords = ("hi", "hello", "bye", "helol", "abc", "cab", "bac", "silenced", "licensed", "declines")
    result = group_anagrams(test_keywords)
    expected = [['abc', 'bac', 'cab'], ['bye'], ['declines', 'licensed', 'silenced'], ['hello', 'helol'], ['hi']]

    assert sorted([sorted(g) for g in result]) == expected
from collections import Counter, defaultdict


with open("src/wordlist.txt", encoding="iso-8859-1") as f:
    keywords = tuple(f.read().split('\n'))


def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = frozenset(tuple(Counter(word).items()))
        anagrams[histogram].append(word)
    return list(anagrams.values())


#keywords = ("hi", "hello", "bye", "helol", "abc", "cab","bac", "silenced", "licensed", "declines")

print(group_anagrams(keywords))


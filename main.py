def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)

def test_all_vowels():
    s = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    assert count_vowels(s) == len(s)

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0
    assert count_vowels("") == 0
    assert count_vowels("1234567890!@#") == 0

def test_mixed_case():
    assert count_vowels("Hello, мир!") == 3  # e, o, и
    assert count_vowels("PyTest is COOL!") == 4  # e, i, O, O
    assert count_vowels("Привет, как дела?") == 5  # и, е, а, е, а
    assert count_vowels("Мама мыла раму") == 6  # а, а, ы, а, а, у
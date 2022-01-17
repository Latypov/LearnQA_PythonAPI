class TestShortPhrase:

    def test_phrase_size(self):
        phrase = input("Set a phrase: ")
        print(phrase)
        assert len(phrase) < 15, f"Unexpected '{phrase}' phrase length: '{len(phrase)}'"

    # Use: 'python -m pytest -s test_short_phrase.py -k "test_phrase_size"' string to run test it terminal

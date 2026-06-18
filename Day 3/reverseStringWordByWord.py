# Write a Python class to reverse a string word by word.

class ReverseStringWordByWord:
    def reverse_words(self, text):
        words = text.split()
        words.reverse()
        return " ".join(words)


reverser = ReverseStringWordByWord()
print(reverser.reverse_words("Hello I am Vaibhav Kheriwal!"))

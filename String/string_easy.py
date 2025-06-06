

# 1. find the longest word of string ?   TC- O(n), SC- O(n)
def longest_word_of_a_sentence(sentence: str) -> str:
    words = sentence.split(" ")
    longest = " "
    for word in words:
        if len(word) >= len(longest):
            longest = word  
    return longest

# 2. print all the words of a sentence ?
def print_all_words_of_a_sentence(sentence: str) -> str:
    words = sentence.split(" ")
    # for word in words:
    print(words)








if __name__ == "__main__":
    text = "my name is sumit"
    longests = " "
    print(longest_word_of_a_sentence(text))
    print(print_all_words_of_a_sentence(text))
    print(type(longests))
class StringUtils():
    @staticmethod
    def is_char_in_word(char, word):
        return char in word

    @staticmethod
    def get_char_index(char, word):
        return word.index(char)
# Завдання 2.

print('--- Task 2 ---')


class TextProcessor:
    def __init__(self, str):
        self._punctuation = '\' " , / . ? ; !'
        self.__clean_string = None
        self.str = str

    def is_punctuation(self, char):
        return char in self._punctuation

    @property
    def clean_string(self):
        # self.char = self._punctuation
        # self.no_punct = ' '
        # # Цикл для видалення знаків пунктуації з рядка.
        # for char in self.str:
        #     if char not in self._punctuation:
        #         self.no_punct += char
        # print('The current word:', text.str)
        # print('Updated word:', self.no_punct)
        return self.__clean_string

    @clean_string.setter
    def clean_string(self, value):
        self.__clean_string = value
        self.char = self._punctuation
        self.no_punct = ''
        # Цикл для видалення знаків пунктуації з рядка.
        for char in value:
            if char not in self._punctuation:
                self.no_punct += char
        print('Setter\'s word:', text.clean_string)
        print('Updated setter\'s word:', self.no_punct)


text = TextProcessor('Hello, World!!')

# print('List of the punctuation:', text._punctuation)
# print(text.clean_string)

print('Does the punctuation from the list exist in this world?: ', end='')
print(text.is_punctuation(''))
# Значення для сеттера
text.clean_string = 'Hi, other World!'

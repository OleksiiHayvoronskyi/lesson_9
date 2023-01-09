# Завдання 2.

print('--- Task 2 ---')


class TextProcessor:
    def __init__(self, str):
        self._punctuation = (' \' " , / . ? ; ! ')
        self.__clean_string = None
        self.str = str

    def is_punctuation(self, char):
        return char in self._punctuation

    @property
    def clean_string(self):
        self.char = self._punctuation
        self.no_punct = ' '
        for char in self.str:
            if char not in self._punctuation:
                self.no_punct += char
        print('The current word:', mark.str)
        print('Updated word:', self.no_punct)
        return self.__clean_string

    @clean_string.setter
    def clean_string(self, value):
        self.__clean_string = value
        self.char = self._punctuation
        self.no_punct = ' '
        for char in value:
            if char not in self._punctuation:
                self.no_punct += char
        print('Setter\'s word:', mark.clean_string)
        print('Updated setter\'s word:', self.no_punct)
        #print(self.__clean_string)


mark = TextProcessor('Hello, World!!')
print('List of the punctuation:', mark._punctuation)
mark.clean_string = 'Hi, other World!'

print(mark.clean_string)


print('Does the punctuation from the list exist in this world?: ', end='')
print(mark.is_punctuation(''))




# self._punktuation = '.,!?;:*
# Оголошення захищеної зміної, потрібно виконати в методі init

# def is_punktuation(self, char):
#         return char in self._punktuation
# Приватний метод для перевірки на наявність символа в переліку пунктуаційних знаків

#  @property
#     def clean_string(self):
# Створення проперті, для змінної (зміна self.__clean_string = None оголошена в методі __init )

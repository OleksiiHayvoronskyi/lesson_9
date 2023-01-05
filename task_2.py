# Завдання 2.

print('--- Task 2 ---')


class TextProcessor:
    def __init__(self, punctuation, str, clean_string = None):
        self.__punctuation = punctuation
        self.__clean_string = clean_string
        self.str = str

    def is_punctuation(self, char):
        return char in self.__punctuation

    @property
    def clean_string(self):
        return self.__clean_string

    @clean_string.setter
    def clean_string(self, value):
        self.__clean_string = value


mark = TextProcessor('/.,?";!', 'Hello, World!!')
print('The current word:', mark.str)
print('Does the punctuation from the list exist in this world?')
print(mark.is_punctuation(','))





# self._punktuation = '.,!?;:*
# Оголошення захищеної зміної, потрібно виконати в методі init

# def is_punktuation(self, char):
#         return char in self._punktuation
# Приватний метод для перевірки на наявність символа в переліку пунктуаційних знаків

#  @property
#     def clean_string(self):
# Створення проперті, для змінної (зміна self.__clean_string = None оголошена в методі __init )


# class TextProcessor(object):
#     def __init__(self, string):
#         #self.marks = None
#         self.string = string
#
#     def get_clean_string(self, marks):
#         self.marks = marks
#         for i, sign in self.marks:
#             if i in self.string:
#                 self.string = self.string.replace(i, sign)
#         print(self.string)
#
#
#
#     # def __is_punktiatian(self): # Приватний метод.
#     #     pass
#
# class TextLoader:
#     def __init__(self, text_processor, clean_string):
#         self.__text_processor = text_processor
#         self.__clean_string = clean_string
#
#     def set_clean_text(self):
#         pass
#
# class DataInterface:
#     def __init__(self, ):
#         pass
#
#     def process_texts(self):
#         pass


# # Об’єкт класу TextProcessor.
# self._punktuation = '.,!?;:*
# text_processor = TextProcessor()
# my_string = TextProcessor('Hello, world!')
#
# print(my_string.get_clean_string())
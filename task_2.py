# Завдання 2.

print('--- Task 2 ---')


class TextProcessor(object):
    def __init__(self, string):
        #self.marks = None
        self.string = string

    def get_clean_string(self, marks):
        self.marks = marks
        for i, sign in self.marks:
            if i in self.string:
                self.string = self.string.replace(i, sign)
        print(self.string)



    def __is_punktiatian(self): # Приватний метод.
        pass

class TextLoader:
    def __init__(self, text_processor, clean_string):
        self.__text_processor = text_processor
        self.__clean_string = clean_string

    def set_clean_text(self):
        pass

class DataInterface:
    def __init__(self, ):
        pass

    def process_texts(self):
        pass


# Об’єкт класу TextProcessor.
text_processor = TextProcessor()
my_string = TextProcessor('Hello, world!')

print(my_string.get_clean_string())
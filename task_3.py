# Завдання 3. Написати клас Parallelogram з двама аргументами: width та lenght.
# Додати метод get_area, який вираховує площу паралелограму.
# Успадкувати від цього класу підклас Square і перевизначити метод get_area,
# щоб він вираховував площу квадрата.

print('--- Task 3 ---')


class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        print('Calculate the area of the parallelogram:')
        print(f' width = {self.width} cm\n length = {self.length} cm')
        print(f'{self.width} * {self.length} = {self.width * self.length}')
        return f'Area of the parallelogram = {self.width * self.length} cm'


class Square(Parallelogram):
    def get_area(self):
        print('\nCalculate the area of the square:')
        print(f' width = {self.width} cm\n length = {self.length} cm')
        print(f'{self.width} * {self.length} = {self.width * self.length}')
        return f'Area of the square = {self.width * self.length} cm'


# Викликаю метод класу Parallelogram.
area_1 = Parallelogram(5, 6)
print(area_1.get_area())
# Викликаю метод класу підкласу Square.
area_2 = Square(4, 4)
print(area_2.get_area())

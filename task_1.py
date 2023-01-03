# Завдання 1. Написати клас автомобіля:
# атрибути: марка, колір, об’єм двигуна;
# методи: їхати вперед, їхати назад.

# Написати ще один клас автомобіля, який є успадкуваням від першого.
# Додати до нього методи повороту праворуч та ліворуч.

print('--- Task 1 ---')


# Батьківський клас Car.
class Car(object):
    # Атрибути класу.
    def __init__(self, brand, color, engine_volume, direction_of_wheels_1,
                 direction_of_wheels_2):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume
        self.direction_of_wheels_1 = direction_of_wheels_1
        self.direction_of_wheels_2 = direction_of_wheels_2

    # Деталі методу - Їхати вперед.
    def drive_forward(self):
        print('(Main Car\'s class)')

        print('Car was identified as:')
        print(f' brand: {self.brand}\n color: {self.color}\n '
              f'engine: {self.engine_volume}')

        if self.direction_of_wheels_1 == 'straight':
            print(f'{self.brand} is now driving forward.')
        elif self.direction_of_wheels_1 != 'straight':
            print('No movement')

        return 'Car with a good condition.' '\n'

    # Деталі методу - Їхати назад.
    def drive_back(self):
        print('(Main Car\'s class)')

        print('Car was identified as:')
        print(f' brand: {self.brand}\n color: {self.color}\n '
              f'engine: {self.engine_volume}')

        if self.direction_of_wheels_2 == 'backward':
            print(f'{self.brand} is now driving backward.')
        elif self.direction_of_wheels_2 != 'backward':
            print('No movement')

        return 'Car with a good condition.' '\n'


# Новий клас, який успадковується від батьківського класу Car.
class PassengerCar(Car):
    # Атрибути підкласу PassengerCar класу Car.
    def __init__(self, brand, color, engine_volume, direction_of_wheels_1,
                 direction_of_wheels_2, direction_of_wheels_3,
                 direction_of_wheels_4):
        # Успадковую атрибути класу Car.
        super().__init__(brand, color, engine_volume, direction_of_wheels_1,
                         direction_of_wheels_2)
        # Додаю нові атрибути до підкласу PassengerCar.
        self.direction_of_wheels_3 = direction_of_wheels_3
        self.direction_of_wheels_4 = direction_of_wheels_4

    # Методи підкласу PassengerCar.
    def turn_right(self):
        print('(Sub-PassengerCar\'s class)')

        print('Car was identified as:')
        print(f' brand: {self.brand}\n color: {self.color}\n '
              f'engine: {self.engine_volume}')

        if self.direction_of_wheels_3 == 'turn right':
            print(f'{self.brand} is now turning right.')
        elif self.direction_of_wheels_3 != 'turn right':
            print('No movement')

        return 'Car with a good condition.' '\n'

    def turn_left(self):
        print('(Sub-PassengerCar\'s class)')

        print('Car was identified as:')
        print(f' brand: {self.brand}\n color: {self.color}\n '
              f'engine: {self.engine_volume}')

        if self.direction_of_wheels_4 == 'turn left':
            print(f'{self.brand} is now turning right.')
        elif self.direction_of_wheels_4 != 'turn left':
            print('No movement')

        return 'Car with a good condition.'


bmw = Car('BMW', 'black', 3.5, 'straight', 'backward')
tavria = Car('Tavria Nova', 'gold', 1.3, 'straight', 'backward')
toyota = PassengerCar('Toyota', 'white', 2.0, 'straight', 'backward',
                      'turn right', 'turn left')
hummer = PassengerCar('Hummer', 'white', 2.0, 'straight', 'backward',
                      'turn right', 'turn left')


# Надрукує атрибути класу Car.
print(bmw.drive_forward())
print(tavria.drive_back())
# Надрукує атрибути підкласу PassengerCar.
print(toyota.turn_right())
print(hummer.turn_left())

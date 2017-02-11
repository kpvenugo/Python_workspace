class Fruit:
    fruit_count = 0  # class variable available across all instances

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Fruit.fruit_count += 1

    def print_fruit(self):
        return '{} {}'.format(self.name, self.color)

    @classmethod
    def :
        pass

fruit1 = Fruit("apple", "green")
fruit2 = Fruit("orange", "orange")
print(Fruit.print_fruit(fruit1))  # or fruit1.print_fruit()
print(Fruit.print_fruit(fruit2))  # or fruit2.print_fruit()
print(Fruit.__dict__)
print(fruit1.__dict__)

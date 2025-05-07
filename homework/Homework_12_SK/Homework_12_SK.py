class Flowers:
    all_quantity = 45
    leaf = True
    count = 99

    def __init__(self, name, color, price, life, length):
        self.name = name
        self.color = color
        self.price = price
        self.life = life
        self.length = length

    def __str__(self):
        return f"{self.name} {self.color} - ${self.price:.2f}, life: {self.life} days, length: {self.length} cm"


class Rose(Flowers):
    def __init__(self, color, price, life, length):
        super().__init__("Rose", color, price, life, length)


class Tulip(Flowers):
    def __init__(self, color, price, life, length):
        super().__init__("Tulip", color, price, life, length)


class Lily(Flowers):
    def __init__(self, color, price, life, length):
        super().__init__("Lily", color, price, life, length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def all_cost(self):
        return sum(flower.price for flower in self.flowers)

    def avarage_life(self):
        if not self.flowers:
            return 0
        return sum(flower.life for flower in self.flowers) / len(self.flowers)

    def find_fl_life(self, min_life):
        return [flower for flower in self.flowers if flower.life >= min_life]

    def sort_flow(self, key):
        self.flowers.sort(key=key)

    def __str__(self):
        details = "\n".join(str(flower) for flower in self.flowers)
        return f"Bouquet:\n{details}\nTotal cost: ${self.all_cost():.2f}, Avarage life: {self.avarage_life():.2f} days"


red_rose = Rose("Red", 5, 7, 17)
yellow_tulip = Tulip("Yellow", 2, 6, 16)
white_lily = Lily("White", 4, 5, 15)

bouquet = Bouquet()
bouquet.add_flower(white_lily)
bouquet.add_flower(yellow_tulip)
bouquet.add_flower(red_rose)

bouquet.sort_flow(key=lambda flower: flower.price)
print("\nBouquet sorted by price:")
print(bouquet)

long_lived_flowers = bouquet.find_fl_life(6)
print("\nFlowers with lifespan of 6 days or more:")
for flower in long_lived_flowers:
    print(flower)

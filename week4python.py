# Base class
class Character:
    def __init__(self, name, universe):
        self.name = name
        self.universe = universe

    def character_info(self):
        return f"{self.name} from {self.universe} Universe"

# Subclass
class Superhero(Character):
    def __init__(self, name, universe, power, energy_level):
        super().__init__(name, universe)
        self.__power = power               # Encapsulation
        self.__energy_level = energy_level # Encapsulation

    def use_power(self):
        if self.__energy_level > 0:
            self.__energy_level -= 10
            return f"{self.name} uses {self.__power}! 💥 Energy left: {self.__energy_level}%"
        else:
            return f"{self.name} is too tired to use power. 😴"

    def recharge(self):
        self.__energy_level = 100
        return f"{self.name} is fully recharged! ⚡"

    def move(self):
        return f"{self.name} is moving in a mysterious way..."

# Polymorphism: Different types of superheroes with unique move styles
class FlyingHero(Superhero):
    def move(self):
        return f"{self.name} is soaring through the sky! 🕊️"

class TeleportingHero(Superhero):
    def move(self):
        return f"{self.name} teleports instantly! ⚡"

class SwingingHero(Superhero):
    def move(self):
        return f"{self.name} is swinging between buildings! 🕸️"

# Example usage
heroes = [
    FlyingHero("SkyLord", "Marvel", "Wind Blast", 100),
    TeleportingHero("Blink", "DC", "Teleportation", 80),
    SwingingHero("WebSlinger", "Marvel", "Web Shot", 90)
]

# Display superhero actions
for hero in heroes:
    print(hero.character_info())
    print(hero.move())
    print(hero.use_power())
    print(hero.recharge())
    print("-" * 40)

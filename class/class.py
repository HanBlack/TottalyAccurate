from Character import character
from faker import Faker
import random

fake = Faker()


class Warrior(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(50, 70)
        self.mp = 10
        self.strength = random.randint(12, 15)
        self.dexterity = random.randint(7, 11)
        self.intelligence = random.randint(1, 4)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Rogue(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(30, 40)
        self.mp = 30
        self.strength = random.randint(5, 9)
        self.dexterity = random.randint(12, 15)
        self.intelligence = random.randint(3, 6)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Mage(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(25, 40)
        self.mp = 40
        self.strength = random.randint(1, 4)
        self.dexterity = random.randint(8, 11)
        self.intelligence = random.randint(11, 15)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Cleric(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(30, 40)
        self.mp = 40
        self.strength = random.randint(6, 9)
        self.dexterity = random.randint(6, 9)
        self.intelligence = random.randint(8, 12)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Hunter(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(30, 45)
        self.mp = 20
        self.strength = random.randint(5, 10)
        self.dexterity = random.randint(10, 13)
        self.intelligence = random.randint(5, 7)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Necromancer(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(25, 40)
        self.mp = 40
        self.strength = random.randint(5, 10)
        self.dexterity = random.randint(5, 8)
        self.intelligence = random.randint(10, 12)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Monk(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(30, 40)
        self.mp = 10
        self.strength = random.randint(6, 10)
        self.dexterity = random.randint(11, 15)
        self.intelligence = random.randint(3, 5)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Assassin(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(20, 40)
        self.mp = 20
        self.strength = random.randint(6, 7)
        self.dexterity = random.randint(11, 17)
        self.intelligence = random.randint(3, 6)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Paladin(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(40, 60)
        self.mp = 30
        self.strength = random.randint(11, 13)
        self.dexterity = random.randint(4, 8)
        self.intelligence = random.randint(5, 9)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Shaman(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(25, 40)
        self.mp = 30
        self.strength = random.randint(6, 11)
        self.dexterity = random.randint(3, 5)
        self.intelligence = random.randint(12, 14)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


class Druid(character.Character):
    def __init__(self):
        super().__init__()
        self.name = fake.name()
        self.hp = random.randint(25, 40)
        self.mp = 25
        self.strength = random.randint(6, 10)
        self.dexterity = random.randint(8, 10)
        self.intelligence = random.randint(6, 10)
        self.experience = 0
        self.level = 0
        self.statusEffect = None


warrior = Warrior()
rogue = Rogue()
mage = Mage()
cleric = Cleric()
hunter = Hunter()
necromancer = Necromancer()
monk = Monk()
assassin = Assassin()
paladin = Paladin()
shaman = Shaman()
druid = Druid()

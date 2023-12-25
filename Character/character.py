import random
from EnemyCharacter import echaracter
from Equipment import equipment
from faker import Faker

from Equipment.equipment import Equipment

fake = Faker()


class Character:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.experience = 0
        self.level = 0
        self.statusEffect = None
        self.equipment = Equipment()

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        if value < 0:
            self._mp = 0
        else:
            self._mp = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if value < 0:
            self._strength = 0
        elif value > 100:
            self._strength = 100
        else:
            self._strength = value

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
        if value < 0:
            self._dexterity = 0
        elif value > 100:
            self._dexterity = 100
        else:
            self._dexterity = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        if value < 0:
            self._intelligence = 0
        elif value > 100:
            self._intelligence = 100
        else:
            self._intelligence = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            self._experience = 0
        else:
            self._experience = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        else:
            self._level = value

    @staticmethod
    def create_character(character_class):
        character_classes = {
            'warrior': Warrior,
            'rogue': Rogue,
            'mage': Mage,
            'cleric': Cleric,
            'hunter': Hunter,
            'necromancer': Necromancer,
            'monk': Monk,
            'assassin': Assassin,
            'paladin': Paladin,
            'shaman': Shaman,
            'druid': Druid,

        }
        if character_class not in character_classes:
            raise ValueError(f"Invalid character class: {character_class}")

        new_character = character_classes[character_class.lower()]()
        return new_character

    def increase_experience(self, amount):
        self._experience += amount
        while self._experience >= self.calculate_experience_needed_for_next_level():
            self.level_up()

    def calculate_experience_needed_for_next_level(self):
        return (150 * self.level) + self.strength + self.dexterity + self.intelligence + random.randint(1, 5)

    def level_up(self):
        experience_required = self.calculate_experience_needed_for_next_level()
        print(experience_required)
        if self._experience >= experience_required:
            self._experience -= experience_required
            self.level += 1
            return True
        else:
            return False

    def gain_experience_from_enemy(self, enemy):
        experience_gained = echaracter.ECharacter.calculate_total_experience(enemy)
        self.increase_experience(experience_gained)
        print(f"{self.name} gained {experience_gained} experience from defeating {enemy.name}!")

    def calculate_character_damage(self):
        primary_damage_deal_attribute = max(self.strength, self.dexterity, self.intelligence)

        if self.check_if_player_scored_critical_hit():
            primary_damage_deal_attribute = (primary_damage_deal_attribute * 2) - (self.level / 2)
        if self.equipment.weapon:
            return int((primary_damage_deal_attribute / 5) + self.equipment.weapon.damage) + random.randint(-1, 1) + 300
        else:
            return int(primary_damage_deal_attribute)

    def calculate_character_armor_value(self):
        total_armour = 0
        for slot in [self.equipment.head, self.equipment.chest, self.equipment.legs, self.equipment.boots,
                     self.equipment.hands, self.equipment.offhand]:
            if slot and slot.armour:
                total_armour += slot.armour
        return total_armour

    def calculate_character_damage_reduction(self):
        armor = self.calculate_character_armor_value()
        return int(armor * 0.1)

    def calculate_player_critical_chance(self):
        base_chance = self.dexterity * 0.1
        level_modifier = 1 + (self.level * 0.05)
        chance_to_crit = base_chance * level_modifier
        chance_to_crit = min(chance_to_crit, 100)
        return chance_to_crit

    def check_if_player_scored_critical_hit(self):
        crit_chance = self.calculate_player_critical_chance()
        compare_number = random.randint(0, 100)
        return compare_number <= crit_chance


character = Character()


class Warrior(Character):
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


warrior = Warrior()


class Rogue(Character):
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


rogue = Rogue()


class Mage(Character):
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


mage = Mage()


class Cleric(Character):
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


cleric = Cleric()


class Hunter(Character):
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


hunter = Hunter()


class Necromancer(Character):
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


necromancer = Necromancer()


class Monk(Character):
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


monk = Monk()


class Assassin(Character):
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


assassin = Assassin()


class Paladin(Character):
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


paladin = Paladin()


class Shaman(Character):
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


shaman = Shaman()


class Druid(Character):
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


druid = Druid()


class Party:
    def __init__(self):
        self.characters = []

    def recruit_character(self, new_character):
        self.characters.append(new_character)


party = Party()

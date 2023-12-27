import random
from EnemyCharacter import echaracter
from Equipment import equipment
from faker import Faker

from Equipment.equipment import Equipment

fake = Faker()


class Character:
    def __init__(self, character_class=None, **kwargs):
        self.character_class = character_class
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
        self.level_up_points = {'strength': 10, 'dexterity': 10, 'intelligence': 10}

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

    def increase_strength(self):
        self.strength += 1

    def increase_dexterity(self):
        self.dexterity += 1

    def increase_intelligence(self):
        self.intelligence += 1

    def increase_experience(self, amount):
        self._experience += amount
        while self._experience >= self.calculate_experience_needed_for_next_level():
            self.level_up()

    def calculate_experience_needed_for_next_level(self):
        return (150 * self.level) + self.strength + self.dexterity + self.intelligence + random.randint(1, 5)

    def level_up(self, stat_to_increase):
        experience_required = self.calculate_experience_needed_for_next_level()
        if self._experience >= experience_required:
            self._experience -= experience_required
            self.level += 1
            if stat_to_increase.lower() == 'strength':
                self.level_up_points['strength'] += 1
            elif stat_to_increase.lower() == 'dexterity':
                self.level_up_points['dexterity'] += 1
            elif stat_to_increase.lower() == 'intelligence':
                self.level_up_points['intelligence'] += 1
            print(f"{self.name} leveled up to level {self.level} and increased {stat_to_increase}!")
            return True
        else:
            return False

    def gain_experience_from_enemy(self, enemy):
        experience_gained = echaracter.ECharacter.calculate_total_experience(enemy)
        self.increase_experience(experience_gained)

    def calculate_character_damage(self):
        primary_damage_deal_attribute = max(self.strength, self.dexterity, self.intelligence)

        if self.check_if_player_scored_critical_hit():
            primary_damage_deal_attribute = (primary_damage_deal_attribute * 2) - (self.level / 2)

        if self.equipment.weapon and "damage" in self.equipment.weapon:
            weapon_damage = self.equipment.weapon["damage"]
            if weapon_damage is not None:
                return int((primary_damage_deal_attribute * 0.8) + weapon_damage) + random.randint(-3, 3)
            else:
                return int(primary_damage_deal_attribute) / 2
        else:
            return int(primary_damage_deal_attribute) / 2

    def calculate_character_armor_value(self):
        total_armour = 0

        equipment_slots = ["head", "chest", "legs", "boots", "hands", "weapon", "offhand", "neck", "ring"]

        for slot in equipment_slots:
            item_data = getattr(self.equipment, slot)
            if item_data and "armour" in item_data:
                armour_value = item_data["armour"]
                if armour_value is not None:
                    total_armour += armour_value

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

    def set_from_friendly_character(self, friendly_character):
        self.name = friendly_character.name
        self.hp = friendly_character.hp
        self.mp = friendly_character.mp
        self.strength = friendly_character.strength
        self.dexterity = friendly_character.dexterity
        self.intelligence = friendly_character.intelligence
        self.experience = friendly_character.experience
        self.level = friendly_character.level
        self.statusEffect = friendly_character.statusEffect
        self.equipment = friendly_character.equipment
        self.character_class = friendly_character.character_class


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

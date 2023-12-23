from Equipment import equipment
from Equipment.EquipmentList import equipment_list
import random


class Legs(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.reset_values()
        self.name = None
        self.damage = None
        self.armor = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def reset_values(self):
        self.name = None
        self.damage = None
        self.armor = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_legs_lvl_1_to_15(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(5, 15)
        return self

    def rare_legs_lvl_1_to_15(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)
        return self

    def common_legs_lvl_15_to_30(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        return self

    def rare_legs_lvl_15_to_30(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)
        return self

    def common_legs_lvl_30_and_more(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        return self

    def rare_legs_lvl_30_and_more(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)
        return self


legs = Legs()


def rare_generate_legs_name():
    prefix = random.choice(equipment_list.rare_fantasy_prefixes)
    suffix = random.choice(equipment_list.rare_fantasy_word_list)
    return f"{prefix} Legs {suffix}"


def normal_generate_legs_name():
    prefix = random.choice(equipment_list.normal_quality_prefixes)
    suffix = random.choice(equipment_list.normal_fantasy_suffixes)
    return f"{prefix} Legs {suffix}"

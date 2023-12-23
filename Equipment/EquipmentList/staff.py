from Equipment import equipment
from Equipment.EquipmentList import equipment_list
import random


class Staff(equipment.EquipmentStats):
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

    def common_staff_lvl_1_to_15(self):
        self.name = normal_generate_staff_name()
        self.damage = random.randint(1, 3)
        return self

    def rare_staff_lvl_1_to_15(self):
        self.name = rare_generate_staff_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        return self

    def common_staff_lvl_15_to_30(self):
        self.name = normal_generate_staff_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        return self

    def rare_staff_lvl_15_to_30(self):
        self.name = rare_generate_staff_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)
        return self

    def common_staff_lvl_30_and_more(self):
        self.name = normal_generate_staff_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        return self

    def rare_staff_lvl_30_and_more(self):
        self.name = rare_generate_staff_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(0, 10)
        return self


staff = Staff()


def rare_generate_staff_name():
    prefix = random.choice(equipment_list.rare_fantasy_prefixes)
    suffix = random.choice(equipment_list.rare_fantasy_word_list)
    return f"{prefix} Staff {suffix}"


def normal_generate_staff_name():
    prefix = random.choice(equipment_list.normal_quality_prefixes)
    suffix = random.choice(equipment_list.normal_fantasy_suffixes)
    return f"{prefix} Staff {suffix}"

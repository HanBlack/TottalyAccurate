from Equipment import equipment
from Equipment.EquipmentList import equipment_list
import random


class Neck(equipment.EquipmentStats):
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

    def common_neck_lvl_1_to_15(self):
        self.reset_values()
        self.name = normal_generate_neck_name()
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 2)
        return self

    def rare_neck_lvl_1_to_15(self):
        self.reset_values()
        self.name = rare_generate_neck_name()
        self.intelligence_bonus = random.randint(1, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)
        return self

    def common_neck_lvl_15_to_30(self):
        self.reset_values()
        self.name = normal_generate_neck_name()
        self.intelligence_bonus = random.randint(0, 3)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)
        return self

    def rare_neck_lvl_15_to_30(self):
        self.reset_values()
        self.name = rare_generate_neck_name()
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(1, 10)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 10)
        return self

    def common_neck_lvl_30_and_more(self):
        self.reset_values()
        self.name = normal_generate_neck_name()
        self.strength_bonus = random.randint(1, 2)
        self.dexterity_bonus = random.randint(1, 2)
        self.intelligence_bonus = random.randint(1, 8)
        self.hp_bonus = random.randint(0, 15)
        self.mp_bonus = random.randint(0, 10)
        return self

    def rare_neck_lvl_30_and_more(self):
        self.reset_values()
        self.name = rare_generate_neck_name()
        self.armour = random.randint(0, 10)
        self.strength_bonus = random.randint(2, 4)
        self.dexterity_bonus = random.randint(2, 4)
        self.intelligence_bonus = random.randint(5, 16)
        self.hp_bonus = random.randint(0, 30)
        self.mp_bonus = random.randint(0, 20)
        return self


neck = Neck()


def rare_generate_neck_name():
    prefix = random.choice(equipment_list.rare_fantasy_prefixes)
    suffix = random.choice(equipment_list.rare_fantasy_word_list)
    return f"{prefix} Neck {suffix}"


def normal_generate_neck_name():
    prefix = random.choice(equipment_list.normal_quality_prefixes)
    suffix = random.choice(equipment_list.normal_fantasy_suffixes)
    return f"{prefix} Neck {suffix}"

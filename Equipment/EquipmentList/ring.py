from Equipment import equipment
from Equipment.EquipmentList import equipment_list
import random


class Ring(equipment.EquipmentStats):
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

    def common_ring_lvl_1_to_15(self):
        self.name = normal_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 2)
        return self

    def rare_ring_lvl_1_to_15(self):
        self.name = rare_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)
        return self

    def common_ring_lvl_15_to_30(self):
        self.name = normal_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 3)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)
        return self

    def rare_ring_lvl_15_to_30(self):
        self.name = rare_generate_ring_name()
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 5)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 10)
        return self

    def common_ring_lvl_30_and_more(self):
        self.name = normal_generate_ring_name()
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 8)
        self.hp_bonus = random.randint(0, 15)
        self.mp_bonus = random.randint(0, 10)
        return self

    def rare_ring_lvl_30_and_more(self):
        self.name = rare_generate_ring_name()
        self.armour = random.randint(0, 10)
        self.strength_bonus = random.randint(2, 4)
        self.dexterity_bonus = random.randint(2, 4)
        self.intelligence_bonus = random.randint(5, 10)
        self.hp_bonus = random.randint(0, 30)
        self.mp_bonus = random.randint(0, 20)
        return self


ring = Ring()


def rare_generate_ring_name():
    prefix = random.choice(equipment_list.rare_fantasy_prefixes)
    suffix = random.choice(equipment_list.rare_fantasy_word_list)
    return f"{prefix} Ring {suffix}"


def normal_generate_ring_name():
    prefix = random.choice(equipment_list.normal_quality_prefixes)
    suffix = random.choice(equipment_list.normal_fantasy_suffixes)
    return f"{prefix} Ring {suffix}"

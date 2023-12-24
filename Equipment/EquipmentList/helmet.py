from Equipment import equipment
from Equipment.EquipmentList import equipment_list
import random


class Helmet(equipment.EquipmentStats):
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

    def common_helmets_lvl_1_to_15(self):
        self.reset_values()
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(5, 15)
        return self

    def rare_helmets_lvl_1_to_15(self):
        self.reset_values()
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(1, 2)
        self.intelligence_bonus = random.randint(1, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)
        return self

    def common_helmets_lvl_15_to_30(self):
        self.reset_values()
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        return self

    def rare_helmets_lvl_15_to_30(self):
        self.reset_values()
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(1, 4)
        self.intelligence_bonus = random.randint(1, 4)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)
        return self

    def common_helmets_lvl_30_and_more(self):
        self.reset_values()
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        return self

    def rare_helmets_lvl_30_and_more(self):
        self.reset_values()
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(1, 8)
        self.intelligence_bonus = random.randint(1, 8)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)
        return self


helmet = Helmet()


def rare_generate_helmet_name():
    prefix = random.choice(equipment_list.rare_fantasy_prefixes)
    suffix = random.choice(equipment_list.rare_fantasy_word_list)
    return f"{prefix} Helmet {suffix}"


def normal_generate_helmet_name():
    prefix = random.choice(equipment_list.normal_quality_prefixes)
    suffix = random.choice(equipment_list.normal_fantasy_suffixes)
    return f"{prefix} Helmet {suffix}"


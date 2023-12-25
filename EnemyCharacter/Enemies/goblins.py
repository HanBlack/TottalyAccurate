import json
import os

from EnemyCharacter import echaracter
from random import choice
from Equipment.EquipmentList import helmet, chest, legs, boots, hands, neck, ring, shield, axe, bow, buckler, crossbow, \
    dagger, hammer, mana_orb, staff, sword, wand
from Equipment.inventory import inventory
import program


def drop_item_goblin_boss_loottable():
    items = [helmet.helmet.rare_helmets_lvl_1_to_15(), chest.chest.rare_chest_lvl_1_to_15(),
             legs.legs.rare_legs_lvl_1_to_15(), boots.boots.rare_boots_lvl_1_to_15(),
             ring.ring.rare_ring_lvl_1_to_15(), neck.neck.rare_neck_lvl_1_to_15(),
             sword.sword.rare_sword_lvl_1_to_15(), axe.axe.rare_axe_lvl_1_to_15(),
             dagger.dagger.rare_dagger_lvl_1_to_15(), bow.bow.rare_bow_lvl_1_to_15(),
             staff.staff.rare_staff_lvl_15_to_30(), crossbow.crossbow.rare_crossbow_lvl_1_to_15(),
             hammer.hammer.rare_hammer_lvl_1_to_15(), wand.wand.rare_wand_lvl_1_to_15(),
             buckler.buckler.rare_buckler_lvl_1_to_15(), shield.shield.rare_shield_lvl_1_to_15(),
             mana_orb.mana_orb.rare_mana_orb_lvl_1_to_15(), hands.hands.rare_hands_lvl_1_to_15()]
    return choice(items)


def drop_item_goblin_lower_evolution_loottable():
    items = [helmet.helmet.common_helmets_lvl_1_to_15(), chest.chest.common_chest_lvl_1_to_15(),
             legs.legs.common_legs_lvl_1_to_15(), boots.boots.common_boots_lvl_1_to_15(),
             ring.ring.common_ring_lvl_1_to_15(), neck.neck.common_neck_lvl_1_to_15(),
             sword.sword.common_sword_lvl_1_to_15(), axe.axe.common_axe_lvl_1_to_15(),
             dagger.dagger.common_dagger_lvl_1_to_15(), bow.bow.common_bow_lvl_1_to_15(),
             staff.staff.common_staff_lvl_15_to_30(), crossbow.crossbow.common_crossbow_lvl_1_to_15(),
             hammer.hammer.common_hammer_lvl_1_to_15(), wand.wand.common_wand_lvl_1_to_15(),
             buckler.buckler.common_buckler_lvl_1_to_15(), shield.shield.common_shield_lvl_1_to_15(),
             mana_orb.mana_orb.common_mana_orb_lvl_1_to_15(), hands.hands.common_hands_lvl_1_to_15()]
    return choice(items)


path_variable = program.current_directory()


def defeat_enemy_goblin_boss(boss):
    path = path_variable

    if boss.hp == 0:
        dropped_item = drop_item_goblin_boss_loottable()
        inventory.add_item(dropped_item)
        class_name = type(dropped_item).__name__
        file_path = os.path.join(path, 'Character', 'CharacterSave', 'CharacterInventory')
        file_name = f'{dropped_item.name}.json'
        file_path = os.path.join(file_path, file_name)
        with open(file_path, "a") as file:
            dropped_item_data = {
                "Class": class_name,
                "Name": dropped_item.name,
                "Damage": dropped_item.damage,
                "Armour": dropped_item.armour,
                "Strength Bonus": dropped_item.strength_bonus,
                "Dexterity Bonus": dropped_item.dexterity_bonus,
                "Intelligence Bonus": dropped_item.intelligence_bonus,
                "HP Bonus": dropped_item.hp_bonus,
                "MP Bonus": dropped_item.mp_bonus
            }
            json.dump(dropped_item_data, file)
            file.write('\n')


class LowerEvolutionGoblin(echaracter.ECharacter):
    def __init__(self):
        super().__init__()

    def snik_stat_set(self):
        self.name = "Snik Goblin"
        self.hp = 10
        self.mp = 5
        self.strength = 2
        self.dexterity = 3
        self.intelligence = 1
        self.level = 1
        return self

    def dribblet_stat_set(self):
        self.name = "Dribblet Goblin"
        self.hp = 12
        self.mp = 6
        self.strength = 3
        self.dexterity = 2
        self.intelligence = 1
        self.level = 1
        return self

    def goblet_stat_set(self):
        self.name = "Goblet Goblin"
        self.hp = 11
        self.mp = 4
        self.strength = 2
        self.dexterity = 2
        self.intelligence = 2
        self.level = 1
        return self

    def snaggletooth_stat_set(self):
        self.name = "Snaggletooth Goblin"
        self.hp = 14
        self.mp = 3
        self.strength = 3
        self.dexterity = 2
        self.intelligence = 1
        self.level = 1
        return self

    def snikwort_stat_set(self):
        self.name = "Snikwort Goblin"
        self.hp = 13
        self.mp = 5
        self.strength = 2
        self.dexterity = 3
        self.intelligence = 1
        self.level = 1
        return self

    def wizzletoe_stat_set(self):
        self.name = "Wizzletoe Goblin"
        self.hp = 10
        self.mp = 4
        self.strength = 2
        self.dexterity = 3
        self.intelligence = 2
        self.level = 1
        return self

    def goblinkin_stat_set(self):
        self.name = "Goblinkin Goblin"
        self.hp = 12
        self.mp = 5
        self.strength = 2
        self.dexterity = 2
        self.intelligence = 2
        self.level = 1
        return self

    def snaglet_stat_set(self):
        self.name = "Snaglet Goblin"
        self.hp = 11
        self.mp = 4
        self.strength = 3
        self.dexterity = 1
        self.intelligence = 1
        self.level = 1
        return self

    def glimmerkin_stat_set(self):
        self.name = "Glimmerkin Goblin"
        self.hp = 9
        self.mp = 6
        self.strength = 1
        self.dexterity = 3
        self.intelligence = 2
        self.level = 1
        return self

    def sniknose_stat_set(self):
        self.name = "Sniknose Goblin"
        self.hp = 10
        self.mp = 3
        self.strength = 1
        self.dexterity = 2
        self.intelligence = 3
        self.level = 1
        return self


class MiddleEvolutionGoblin(echaracter.ECharacter):
    def __init__(self):
        super().__init__()

    def snikkle_stat_set(self):
        self.name = "Snikkle Goblin"
        self.hp = 15
        self.mp = 8
        self.strength = 4
        self.dexterity = 4
        self.intelligence = 2
        self.level = 3
        return self

    def grobok_stat_set(self):
        self.name = "Grobok Goblin"
        self.hp = 16
        self.mp = 7
        self.strength = 3
        self.dexterity = 5
        self.intelligence = 2
        self.level = 3
        return self

    def snaggle_stat_set(self):
        self.name = "Snaggle Goblin"
        self.hp = 14
        self.mp = 6
        self.strength = 5
        self.dexterity = 3
        self.intelligence = 3
        self.level = 3
        return self

    def zoglink_stat_set(self):
        self.name = "Zoglink Goblin"
        self.hp = 15
        self.mp = 5
        self.strength = 4
        self.dexterity = 4
        self.intelligence = 3
        self.level = 3
        return self

    def gnarble_stat_set(self):
        self.name = "Gnarble Goblin"
        self.hp = 13
        self.mp = 8
        self.strength = 3
        self.dexterity = 3
        self.intelligence = 4
        self.level = 3
        return self

    def snigwort_stat_set(self):
        self.name = "Snigwort Goblin"
        self.hp = 16
        self.mp = 6
        self.strength = 4
        self.dexterity = 5
        self.intelligence = 2
        self.level = 3
        return self

    def wizzle_stat_set(self):
        self.name = "Wizzle Goblin"
        self.hp = 14
        self.mp = 7
        self.strength = 3
        self.dexterity = 4
        self.intelligence = 3
        self.level = 2
        return self

    def goblimp_stat_set(self):
        self.name = "Goblimp Goblin"
        self.hp = 15
        self.mp = 6
        self.strength = 4
        self.dexterity = 4
        self.intelligence = 3
        self.level = 3
        return self

    def grunk_stat_set(self):
        self.name = "Grunk Goblin"
        self.hp = 14
        self.mp = 7
        self.strength = 3
        self.dexterity = 3
        self.intelligence = 3
        self.level = 2
        return self


class HigherEvolutionGoblin(echaracter.ECharacter):
    def __init__(self):
        super().__init__()

    def snarltooth_stat_set(self):
        self.name = "Snarltooth Goblin"
        self.hp = 25
        self.mp = 15
        self.strength = 8
        self.dexterity = 7
        self.intelligence = 5
        self.level = 5
        return self

    def rumblefist_stat_set(self):
        self.name = "Rumblefist Goblin"
        self.hp = 23
        self.mp = 12
        self.strength = 7
        self.dexterity = 8
        self.intelligence = 6
        self.level = 5
        return self

    def gorknash_stat_set(self):
        self.name = "Gorknash Goblin"
        self.hp = 24
        self.mp = 14
        self.strength = 9
        self.dexterity = 6
        self.intelligence = 6
        self.level = 5
        return self

    def kragnash_stat_set(self):
        self.name = "Kragnash Goblin"
        self.hp = 22
        self.mp = 13
        self.strength = 8
        self.dexterity = 7
        self.intelligence = 7
        self.level = 5
        return self

    def grimsnarl_stat_set(self):
        self.name = "Grimsnarl Goblin"
        self.hp = 21
        self.mp = 16
        self.strength = 7
        self.dexterity = 6
        self.intelligence = 8
        self.level = 5
        return self

    def grobthar_stat_set(self):
        self.name = "Grobthar Goblin"
        self.hp = 26
        self.mp = 11
        self.strength = 9
        self.dexterity = 8
        self.intelligence = 5
        self.level = 5
        return self

    def thraggle_stat_set(self):
        self.name = "Thraggle Goblin"
        self.hp = 20
        self.mp = 17
        self.strength = 6
        self.dexterity = 9
        self.intelligence = 7
        self.level = 5
        return self

    def zilgok_stat_set(self):
        self.name = "Zilgok Goblin"
        self.hp = 19
        self.mp = 18
        self.strength = 5
        self.dexterity = 10
        self.intelligence = 8
        self.level = 5
        return self

    def sniklash_stat_set(self):
        self.name = "Sniklash Goblin"
        self.hp = 18
        self.mp = 20
        self.strength = 4
        self.dexterity = 11
        self.intelligence = 9
        self.level = 5
        return self

    def vargnash_stat_set(self):
        self.name = "Vargnash Goblin"
        self.hp = 20
        self.mp = 19
        self.strength = 6
        self.dexterity = 9
        self.intelligence = 7
        self.level = 5
        return self


class BossEvolutionGoblin(echaracter.ECharacter):
    def __init__(self):
        super().__init__()

    def grommok_the_tyrant_stat_set(self):
        self.name = "Grommok The Tyrant"
        self.hp = 50
        self.mp = 30
        self.strength = 15
        self.dexterity = 12
        self.intelligence = 10
        self.level = 10
        self.statusEffect = "Fury Swipe"  # Deals a massive cleave damage
        return self

    def zargoth_the_unbreakable_stat_set(self):
        self.name = "Zargoth The Unbreakable"
        self.hp = 55
        self.mp = 25
        self.strength = 14
        self.dexterity = 10
        self.intelligence = 12
        self.level = 11
        self.statusEffect = "Unyielding Resiliance "  # Reduce incoming damage for one turn by 50%
        return self

    def morgul_the_devourer_stat_set(self):
        self.name = "Morgul The Devourer"
        self.hp = 60
        self.mp = 35
        self.strength = 16
        self.dexterity = 13
        self.intelligence = 11
        self.level = 12
        self.statusEffect = "Fury Swipe"  # life steal by damage deal
        return self

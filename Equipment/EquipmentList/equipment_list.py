from Equipment import equipment
from faker import Faker
import random

fake = Faker()
rare_fantasy_prefixes = [
    'Dread', 'Radiant', 'Savage', 'Mystic', 'Shadow', 'Doom', 'Divine', 'Frost', 'Blazing',
    'Ancient', 'Spectral', 'Eternal', 'Infernal', 'Thundering', 'Twilight', 'Celestial', 'Silent',
    'Ghostly', 'Fiery', 'Storm', 'Arcane', 'Soul', 'Furious', 'Nightmare', 'Death', 'Corrupted',
    'Golden', 'Frozen', 'Venomous', 'Enchanted', 'Silver', 'Holy', 'Cursed', 'Piercing', 'Iron',
    'Hellfire', 'Void', 'Bloodied', 'Platinum', 'Demonic', 'Molten', 'Crystal', 'Thunderous', 'Jade',
    'Spirit', 'Onyx', 'Burning', 'Glacial', 'Draconic', 'Radiant', 'Shattered', 'Oblivion', 'Fanged',
    'Ember', 'Darkened', 'Renegade', 'Stormforged', 'Hallowed', 'Whispering', 'Vengeful', 'Resplendent',
    'Shadowed', 'Runic', 'Resolute', 'Abyssal', 'Royal', 'Virtuous', 'Venom', 'Dreadnaught', 'Enigma',
    'Gilded', 'Ashen', 'Glimmering', 'Stalwart', 'Raging', 'Pristine', 'Bladeworn', 'Ashen', 'Crystalline',
    'Haunted', 'Crimson', 'Azure', 'Ebon', 'Verdant', 'Glowing', 'Slayer', 'Moonlit', 'Crested', 'Ravager'
    # Add more fantasy-inspired prefixes for helmets here
]
rare_fantasy_word_list = [
    'of Excalibur', 'of Eldritch', 'of Dragonfire', 'of Arcane', 'of Sorcery', 'of Mystic', 'of Shadowblade',
    'of Celestial', 'of Frostfang', 'of Wyvern', 'of Runesong', 'of Stormbringer', 'of Moonshadow', 'of Abyssal',
    'of Emberstorm', 'of Starfall', 'of Doomhammer', 'of Thornstrike', 'of Soulreaper', 'of Blightcaster',
    'of Phoenix', 'of Thunderbolt', 'of Eclipse', 'of Baneblade', 'of Crimsonbane', 'of Necroblade', 'of Duskblade',
    'of Frostbite', 'of Voidwalker', 'of Shadowstep', 'of Nightfall', 'of Stardust', 'of Vortex', 'of Firesoul',
    'of Deathwhisper', 'of Bloodmoon', 'of Venomspite', 'of Ashbringer', 'of Frostheart', 'of Ironfury',
    'of Skyshatter',
    'of Hellfire', 'of Gravecaller', 'of Runeblade', 'of Thunderstrike', 'of Sunflare', 'of Darkmatter',
    'of Eternalflame',
    'of Frostfire', 'of Skullcrusher', 'of Vorpalblade', 'of Wyrmslayer', 'of Arcanite', 'of Gorehowl', 'of Netherbane',
    'of Silentshadow', 'of Shattersong', 'of Aurora', 'of Dragonheart', 'of Stormfury', 'of Ghostwalker', 'of Twilight',
    'of Bladestorm', 'of Stormbreaker', 'of Stargazer', 'of Warbringer', 'of Dreamweaver', 'of Dreadfang',
    'of Nightmare',
    'of Soulrender', 'of Doombringer', 'of Frostshard', 'of Voidblade', 'of Sunflare', 'of Grimoire', 'of Nightstalker',
    'of Twilightshroud', 'of Eclipse', 'of Lunarfall', 'of Celestialwrath', 'of Thunderfury', 'of Darkbane',
    'of Bloodthirst'
]
normal_quality_prefixes = [
    'Iron', 'Steel', 'Bronze', 'Copper', 'Leather', 'Wooden', 'Cloth', 'Tin', 'Bone', 'Brass',
    'Rusty', 'Padded', 'Chain', 'Scale', 'Battered', 'Worn', 'Tarnished', 'Frayed', 'Weathered',
    'Chipped', 'Cracked', 'Dented', 'Rugged', 'Patchwork', 'Plain', 'Simple', 'Sturdy', 'Aged',
    'Primitive', 'Old', 'Rustic', 'Basic', 'Common', 'Ordinary', 'Unremarkable', 'Rudimentary',
    'Inferior', 'Modest', 'Faulty', 'Flawed', 'Shabby', 'Tattered', 'Used', 'Blemished', 'Dingy',
    'Dull', 'Junk', 'Worn-out', 'Tired', 'Rough', 'Jagged', 'Humble', 'Scratched', 'Tinged',
    'Marked', 'Discolored', 'Misfit', 'Mended', 'Amateur', 'Homely', 'Slight', 'Subpar', 'Decayed',
    'Aged', 'Weathered', 'Fractured', 'Weak', 'Shoddy', 'Patched', 'Ragged', 'Battered', 'Faded',
    'Raggedy', 'Ragged', 'Frayed', 'Dingy', 'Worn', 'Shabby', 'Tattered', 'Cracked', 'Faded',
    'Ancient', 'Broken', 'Dirty', 'Ailing', 'Crude', 'Damaged', 'Defective', 'Wretched', 'Wearied',
    'Tarnished', 'Dishonored', 'Dishonorable', 'Doomed', 'Worn-down', 'Wasteful', 'Wearisome',
    'Wretched', 'Decrepit', 'Discredited', 'Dilapidated', 'Deplorable', 'Ragged', 'Rough', 'Ruined',
    'Sloppy', 'Underprivileged', 'Unsightly', 'Unsuitable', 'Unworthy', 'Vile', 'Weariful', 'Yawning'
]
normal_fantasy_suffixes = [
    'of Protection', 'of Guarding', 'of the Sentinel', 'of Fortitude', 'of the Guardian', 'of Warding',
    'of the Ward', 'of Defense', 'of the Defender', 'of the Bulwark', 'of the Protector', 'of the Shield',
    'of Safeguarding', 'of Shelter', 'of the Screen', 'of the Rampart', 'of Covering', 'of the Barrier',
    'of Safety', 'of Security', 'of Safety', 'of the Aegis', 'of Safeguard', 'of the Shelter', 'of the Haven',
    'of the Citadel', 'of the Stronghold', 'of the Sanctuary', 'of the Refuge', 'of the Fend', 'of the Screen',
    'of the Protection', 'of the Shelter', 'of the Shield', 'of the Rampart', 'of the Bastion', 'of the Keep',
    'of the Bulwark', 'of the Blockade', 'of the Ward', 'of the Barricade', 'of the Hedge', 'of the Cover',
    'of the Guard', 'of the Shielding', 'of the Shelter', 'of the Rampart', 'of the Guard', 'of the Protection',
    'of the Bulwark', 'of the Refuge', 'of the Safehold', 'of the Screen', 'of the Shelter', 'of the Haven',
    'of the Barricade', 'of the Rampart', 'of the Wall', 'of the Fend', 'of the Guard', 'of the Safeguard',
    'of the Ward', 'of the Keep', 'of the Aegis', 'of the Citadel', 'of the Sanctuary', 'of the Protection',
    'of the Shelter', 'of the Shield', 'of the Rampart', 'of the Bastion', 'of the Keep', 'of the Bulwark',
    'of the Blockade', 'of the Ward', 'of the Barricade', 'of the Hedge', 'of the Cover', 'of the Guard',
    'of the Shielding', 'of the Shelter', 'of the Rampart', 'of the Guard', 'of the Protection', 'of the Bulwark',
    'of the Refuge', 'of the Safehold', 'of the Screen', 'of the Shelter', 'of the Haven', 'of the Barricade',
    'of the Rampart', 'of the Wall', 'of the Fend', 'of the Guard', 'of the Safeguard', 'of the Ward', 'of the Keep'
]


def rare_generate_helmet_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Helmet {suffix}"


def normal_generate_helmet_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Helmet {suffix}"


def rare_generate_chest_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} chest {suffix}"


def normal_generate_chest_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} chest {suffix}"


def rare_generate_legs_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} legs {suffix}"


def normal_generate_legs_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} legs {suffix}"


def rare_generate_boots_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} boots {suffix}"


def normal_generate_boots_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} boots {suffix}"


def rare_generate_hands_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} hands {suffix}"


def normal_generate_hands_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} hands {suffix}"


def rare_generate_sword_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Sword {suffix}"


def normal_generate_sword_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Sword {suffix}"


def rare_generate_axe_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Axe {suffix}"


def normal_generate_axe_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Axe {suffix}"


def rare_generate_dagger_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Dagger {suffix}"


def normal_generate_dagger_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Dagger {suffix}"


def rare_generate_bow_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Bow {suffix}"


def normal_generate_bow_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Bow {suffix}"


def rare_generate_crossbow_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Crossbow {suffix}"


def normal_generate_crossbow_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Crossbow {suffix}"


def rare_generate_stave_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Stave {suffix}"


def normal_generate_stave_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Stave {suffix}"


def rare_generate_wand_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Wand {suffix}"


def normal_generate_wand_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Wand {suffix}"


def rare_generate_hammer_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Hammer {suffix}"


def normal_generate_hammer_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Hammer {suffix}"


def rare_generate_shield_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Shield {suffix}"


def normal_generate_shield_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Shield {suffix}"


def rare_generate_buckler_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Buckler {suffix}"


def normal_generate_buckler_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Buckler {suffix}"


def rare_generate_mana_orb_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} Mana Orb {suffix}"


def normal_generate_mana_orb_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} Mana Orb {suffix}"


def rare_generate_neck_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} neck {suffix}"


def normal_generate_neck_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} neck {suffix}"


def rare_generate_ring_name():
    prefix = random.choice(rare_fantasy_prefixes)
    suffix = random.choice(rare_fantasy_word_list)
    return f"{prefix} ring {suffix}"


def normal_generate_ring_name():
    prefix = random.choice(normal_quality_prefixes)
    suffix = random.choice(normal_fantasy_suffixes)
    return f"{prefix} ring {suffix}"


class Helmet(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_helmets_lvl_1_to_15(self):
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(5, 15)

    def rare_helmets_lvl_1_to_15(self):
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_helmets_lvl_15_to_30(self):
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_helmets_lvl_15_to_30(self):
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_helmets_lvl_30_and_more(self):
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_helmets_lvl_30_and_more(self):
        self.name = rare_generate_helmet_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


class Chest(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_chest_lvl_1_to_15(self):
        self.name = normal_generate_chest_name()
        self.armour = random.randint(5, 15)

    def rare_chest_lvl_1_to_15(self):
        self.name = rare_generate_chest_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_chest_lvl_15_to_30(self):
        self.name = normal_generate_chest_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_chest_lvl_15_to_30(self):
        self.name = rare_generate_chest_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_chest_lvl_30_and_more(self):
        self.name = normal_generate_chest_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)

    def rare_chest_lvl_30_and_more(self):
        self.name = rare_generate_chest_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


class Legs(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_legs_lvl_1_to_15(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(5, 15)

    def rare_legs_lvl_1_to_15(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_legs_lvl_15_to_30(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_legs_lvl_15_to_30(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_legs_lvl_30_and_more(self):
        self.name = normal_generate_legs_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_legs_lvl_30_and_more(self):
        self.name = rare_generate_legs_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


class Boots(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_boots_lvl_1_to_15(self):
        self.name = normal_generate_boots_name()
        self.armour = random.randint(5, 15)

    def rare_boots_lvl_1_to_15(self):
        self.name = rare_generate_boots_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_boots_lvl_15_to_30(self):
        self.name = normal_generate_boots_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_boots_lvl_15_to_30(self):
        self.name = rare_generate_boots_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_boots_lvl_30_and_more(self):
        self.name = normal_generate_boots_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_boots_lvl_30_and_more(self):
        self.name = rare_generate_boots_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


class Hands(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_hands_lvl_1_to_15(self):
        self.name = normal_generate_hands_name()
        self.armour = random.randint(5, 15)

    def rare_hands_lvl_1_to_15(self):
        self.name = rare_generate_hands_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_hands_lvl_15_to_30(self):
        self.name = normal_generate_hands_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_hands_lvl_15_to_30(self):
        self.name = rare_generate_hands_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_hands_lvl_30_and_more(self):
        self.name = normal_generate_hands_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_hands_lvl_30_and_more(self):
        self.name = rare_generate_hands_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


class Neck(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_neck_lvl_1_to_15(self):
        self.name = normal_generate_neck_name()
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 2)

    def rare_neck_lvl_1_to_15(self):
        self.name = rare_generate_neck_name()
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)

    def common_neck_lvl_15_to_30(self):
        self.name = normal_generate_neck_name()
        self.intelligence_bonus = random.randint(0, 3)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def rare_neck_lvl_15_to_30(self):
        self.name = rare_generate_neck_name()
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 5)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 10)

    def common_neck_lvl_30_and_more(self):
        self.name = normal_generate_neck_name()
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 8)
        self.hp_bonus = random.randint(0, 15)
        self.mp_bonus = random.randint(0, 10)

    def rare_neck_lvl_30_and_more(self):
        self.name = rare_generate_neck_name()
        self.armour = random.randint(0, 10)
        self.strength_bonus = random.randint(2, 4)
        self.dexterity_bonus = random.randint(2, 4)
        self.intelligence_bonus = random.randint(5, 10)
        self.hp_bonus = random.randint(0, 30)
        self.mp_bonus = random.randint(0, 20)


class Ring(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_ring_lvl_1_to_15(self):
        self.name = normal_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 2)

    def rare_ring_lvl_1_to_15(self):
        self.name = rare_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)

    def common_ring_lvl_15_to_30(self):
        self.name = normal_generate_ring_name()
        self.intelligence_bonus = random.randint(0, 3)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def rare_ring_lvl_15_to_30(self):
        self.name = rare_generate_ring_name()
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 5)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 10)

    def common_ring_lvl_30_and_more(self):
        self.name = normal_generate_ring_name()
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 8)
        self.hp_bonus = random.randint(0, 15)
        self.mp_bonus = random.randint(0, 10)

    def rare_ring_lvl_30_and_more(self):
        self.name = rare_generate_ring_name()
        self.armour = random.randint(0, 10)
        self.strength_bonus = random.randint(2, 4)
        self.dexterity_bonus = random.randint(2, 4)
        self.intelligence_bonus = random.randint(5, 10)
        self.hp_bonus = random.randint(0, 30)
        self.mp_bonus = random.randint(0, 20)


class Weapon(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.damage = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.mp_bonus = None

    def common_sword_lvl_1_to_15(self):
        self.name = normal_generate_sword_name()
        self.damage = random.randint(1, 3)

    def rare_sword_lvl_1_to_15(self):
        self.name = rare_generate_sword_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def common_sword_lvl_15_to_30(self):
        self.name = normal_generate_sword_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_sword_lvl_15_to_30(self):
        self.name = rare_generate_sword_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)

    def common_sword_lvl_30_and_more(self):
        self.name = normal_generate_sword_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_sword_lvl_30_and_more(self):
        self.name = rare_generate_sword_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_axe_lvl_1_to_15(self):
        self.name = normal_generate_axe_name()
        self.damage = random.randint(1, 3)

    def rare_axe_lvl_1_to_15(self):
        self.name = rare_generate_axe_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 2)

    def common_axe_lvl_15_to_30(self):
        self.name = normal_generate_axe_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 2)

    def rare_axe_lvl_15_to_30(self):
        self.name = rare_generate_axe_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(1, 3)
        self.hp_bonus = random.randint(0, 5)

    def common_axe_lvl_30_and_more(self):
        self.name = normal_generate_axe_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 3)

    def rare_axe_lvl_30_and_more(self):
        self.name = rare_generate_axe_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(3, 6)
        self.hp_bonus = random.randint(2, 10)

    def common_dagger_lvl_1_to_15(self):
        self.name = normal_generate_dagger_name()
        self.damage = random.randint(1, 3)

    def rare_dagger_lvl_1_to_15(self):
        self.name = rare_generate_dagger_name()
        self.damage = random.randint(3, 5)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def common_dagger_lvl_15_to_30(self):
        self.name = normal_generate_dagger_name()
        self.damage = random.randint(3, 6)
        self.dexterity_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_dagger_lvl_15_to_30(self):
        self.name = rare_generate_dagger_name()
        self.damage = random.randint(5, 8)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)

    def common_dagger_lvl_30_and_more(self):
        self.name = normal_generate_dagger_name()
        self.damage = random.randint(6, 10)
        self.dexterity_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)

    def rare_dagger_lvl_30_and_more(self):
        self.name = rare_generate_dagger_name()
        self.damage = random.randint(10, 15)
        self.dexterity_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(3, 5)

    def common_bow_lvl_1_to_15(self):
        self.name = normal_generate_bow_name()
        self.damage = random.randint(1, 3)

    def rare_bow_lvl_1_to_15(self):
        self.name = rare_generate_bow_name()
        self.damage = random.randint(3, 5)
        self.dexterity_bonus = random.randint(0, 2)

    def common_bow_lvl_15_to_30(self):
        self.name = normal_generate_bow_name()
        self.damage = random.randint(3, 6)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_bow_lvl_15_to_30(self):
        self.name = rare_generate_bow_name()
        self.damage = random.randint(5, 8)
        self.dexterity_bonus = random.randint(0, 3)
        self.hp_bonus = random.randint(0, 5)

    def common_bow_lvl_30_and_more(self):
        self.name = normal_generate_bow_name()
        self.damage = random.randint(6, 10)
        self.dexterity_bonus = random.randint(0, 3)

    def rare_bow_lvl_30_and_more(self):
        self.name = rare_generate_bow_name()
        self.damage = random.randint(10, 15)
        self.dexterity_bonus = random.randint(3, 6)
        self.hp_bonus = random.randint(2, 10)

    def common_crossbow_lvl_1_to_15(self):
        self.name = normal_generate_crossbow_name()
        self.damage = random.randint(1, 3)

    def rare_crossbow_lvl_1_to_15(self):
        self.name = rare_generate_crossbow_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def common_crossbow_lvl_15_to_30(self):
        self.name = normal_generate_crossbow_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 1)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_crossbow_lvl_15_to_30(self):
        self.name = rare_generate_crossbow_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)

    def common_crossbow_lvl_30_and_more(self):
        self.name = normal_generate_crossbow_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 2)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_crossbow_lvl_30_and_more(self):
        self.name = rare_generate_crossbow_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(0, 4)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_stave_lvl_1_to_15(self):
        self.name = normal_generate_stave_name()
        self.damage = random.randint(1, 3)

    def rare_stave_lvl_1_to_15(self):
        self.name = rare_generate_stave_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def common_stave_lvl_15_to_30(self):
        self.name = normal_generate_stave_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_stave_lvl_15_to_30(self):
        self.name = rare_generate_stave_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 5)

    def common_stave_lvl_30_and_more(self):
        self.name = normal_generate_stave_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)

    def rare_stave_lvl_30_and_more(self):
        self.name = rare_generate_stave_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(0, 10)

    def common_wand_lvl_1_to_15(self):
        self.name = normal_generate_wand_name()
        self.damage = random.randint(1, 3)

    def rare_wand_lvl_1_to_15(self):
        self.name = rare_generate_wand_name()
        self.damage = random.randint(3, 5)
        self.intelligence_bonus = random.randint(0, 2)

    def common_wand_lvl_15_to_30(self):
        self.name = normal_generate_wand_name()
        self.damage = random.randint(3, 6)
        self.intelligence_bonus = random.randint(0, 2)

    def rare_wand_lvl_15_to_30(self):
        self.name = rare_generate_wand_name()
        self.damage = random.randint(5, 8)
        self.intelligence_bonus = random.randint(0, 4)
        self.mp_bonus = random.randint(0, 5)

    def common_wand_lvl_30_and_more(self):
        self.name = normal_generate_wand_name()
        self.damage = random.randint(6, 10)
        self.intelligence_bonus = random.randint(0, 4)

    def rare_wand_lvl_30_and_more(self):
        self.name = rare_generate_wand_name()
        self.damage = random.randint(10, 15)
        self.intelligence_bonus = random.randint(3, 6)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(2, 10)

    def common_hammer_lvl_1_to_15(self):
        self.name = normal_generate_hammer_name()
        self.damage = random.randint(1, 3)

    def rare_hammer_lvl_1_to_15(self):
        self.name = rare_generate_hammer_name()
        self.damage = random.randint(3, 5)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 3)

    def common_hammer_lvl_15_to_30(self):
        self.name = normal_generate_hammer_name()
        self.damage = random.randint(3, 6)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_hammer_lvl_15_to_30(self):
        self.name = rare_generate_hammer_name()
        self.damage = random.randint(5, 8)
        self.strength_bonus = random.randint(0, 3)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 5)
        self.max_hp_bonus = random.randint(0, 5)

    def common_hammer_lvl_30_and_more(self):
        self.name = normal_generate_hammer_name()
        self.damage = random.randint(6, 10)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)

    def rare_hammer_lvl_30_and_more(self):
        self.name = rare_generate_hammer_name()
        self.damage = random.randint(10, 15)
        self.strength_bonus = random.randint(2, 5)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(2, 10)
        self.mp_bonus = random.randint(2, 10)


class Offhand(equipment.EquipmentStats):
    def __init__(self):
        super().__init__()
        self.name = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None

    def common_shield_lvl_1_to_15(self):
        self.name = normal_generate_shield_name()
        self.armour = random.randint(5, 15)

    def rare_shield_lvl_1_to_15(self):
        self.name = rare_generate_shield_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)

    def common_shield_lvl_15_to_30(self):
        self.name = normal_generate_shield_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)

    def rare_shield_lvl_15_to_30(self):
        self.name = rare_generate_shield_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)

    def common_shield_lvl_30_and_more(self):
        self.name = normal_generate_shield_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 2)

    def rare_shield_lvl_30_and_more(self):
        self.name = rare_generate_shield_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)

    def common_buckler_lvl_1_to_15(self):
        self.name = normal_generate_buckler_name()
        self.armour = random.randint(5, 15)

    def rare_buckler_lvl_1_to_15(self):
        self.name = rare_generate_buckler_name()
        self.armour = random.randint(2, 30)
        self.dexterity_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)

    def common_buckler_lvl_15_to_30(self):
        self.name = normal_generate_buckler_name()
        self.armour = random.randint(15, 30)
        self.dexterity_bonus = random.randint(0, 1)

    def rare_buckler_lvl_15_to_30(self):
        self.name = rare_generate_buckler_name()
        self.armour = random.randint(30, 60)
        self.dexterity_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)

    def common_buckler_lvl_30_and_more(self):
        self.name = normal_generate_buckler_name()
        self.armour = random.randint(30, 50)
        self.dexterity_bonus = random.randint(0, 2)

    def rare_buckler_lvl_30_and_more(self):
        self.name = rare_generate_buckler_name()
        self.armour = random.randint(60, 80)
        self.dexterity_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)

    def common_mana_orb_lvl_1_to_15(self):
        self.name = normal_generate_helmet_name()
        self.armour = random.randint(5, 15)

    def rare_mana_orb_lvl_1_to_15(self):
        self.name = rare_generate_mana_orb_name()
        self.armour = random.randint(2, 30)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)
        self.hp_bonus = random.randint(0, 5)
        self.mp_bonus = random.randint(0, 2)

    def common_mana_orb_lvl_15_to_30(self):
        self.name = normal_generate_mana_orb_name()
        self.armour = random.randint(15, 30)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_mana_orb_lvl_15_to_30(self):
        self.name = rare_generate_mana_orb_name()
        self.armour = random.randint(30, 60)
        self.strength_bonus = random.randint(0, 2)
        self.intelligence_bonus = random.randint(0, 2)
        self.hp_bonus = random.randint(0, 10)
        self.mp_bonus = random.randint(0, 5)

    def common_mana_orb_lvl_30_and_more(self):
        self.name = normal_generate_mana_orb_name()
        self.armour = random.randint(30, 50)
        self.strength_bonus = random.randint(0, 1)
        self.intelligence_bonus = random.randint(0, 1)

    def rare_mana_orb_lvl_30_and_more(self):
        self.name = rare_generate_mana_orb_name()
        self.armour = random.randint(60, 80)
        self.strength_bonus = random.randint(0, 4)
        self.intelligence_bonus = random.randint(0, 4)
        self.hp_bonus = random.randint(0, 20)
        self.mp_bonus = random.randint(0, 10)


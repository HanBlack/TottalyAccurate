class Equipment:
    def __init__(self):
        self.head = None
        self.chest = None
        self.legs = None
        self.boots = None
        self.hands = None
        self.weapon = None
        self.offhand = None
        self.neck = None
        self.ring = None

    def save_equipped_gear_to_file(self, file_path):
        equipped_slots = {
            "head": equipment.head,
            "chest": equipment.chest,
            "legs": equipment.legs,
            "boots": equipment.boots,
            "hands": equipment.hands,
            "weapon": equipment.weapon,
            "offhand": equipment.offhand,
            "neck": equipment.neck,
            "ring": equipment.ring
        }

        with open(file_path, "w") as file:
            for slot, item in equipped_slots.items():
                if item:
                    file.write(f"{slot}: {item.name}\n")

    def get_equipped_items(self):
        equipped_slots = {
            "head": self.head,
            "chest": self.chest,
            "legs": self.legs,
            "boots": self.boots,
            "hands": self.hands,
            "weapon": self.weapon,
            "offhand": self.offhand,
            "neck": self.neck,
            "ring": self.ring
        }
        equipped_items_dict = {}
        for slot, item in equipped_slots.items():
            if item:
                equipped_items_dict[slot] = item
        return equipped_items_dict

    def dictionary_for_items(self):
        equipped_slots = {
            "head": self.head,
            "chest": self.chest,
            "legs": self.legs,
            "boots": self.boots,
            "hands": self.hands,
            "weapon": self.weapon,
            "offhand": self.offhand,
            "neck": self.neck,
            "ring": self.ring
        }

        equipped_items_dict = {}
        for slot, item in equipped_slots.items():
            if item:
                equipped_items_dict[slot] = item.to_dict() if isinstance(item, EquipmentStats) else item

        return equipped_items_dict

    def equip_item(self, item):
        if item.item_class == 'Helmet':
            self.head = item
        elif item.item_class == 'Chest':
            self.chest = item
        elif item.item_class == 'Boots':
            self.boots = item
        elif item.item_class == 'Hands':
            self.hands = item
        elif item.item_class == 'Neck':
            self.neck = item
        elif item.item_class == 'Ring':
            self.ring = item
        elif item.item_class in ['Shield', 'Buckler', 'ManaOrb']:
            self.offhand = item
        elif item.item_class in ['Sword', 'Axe', 'Dagger', 'Bow', 'Crossbow', 'Staff', 'Wand', 'Hammer']:
            self.weapon = item

    def unequip_item(self, slot_name):
        if slot_name == 'helmet':
            self.head = None
        elif slot_name == 'chest':
            self.chest = None
        elif slot_name == 'boots':
            self.boots = None
        elif slot_name == 'hands':
            self.hands = None
        elif slot_name == 'neck':
            self.neck = None
        elif slot_name == 'ring':
            self.ring = None
        elif slot_name == 'offhand':
            self.offhand = None
        elif slot_name == 'weapon':
            self.weapon = None

    def print_equipped_items(self):
        equipped_slots = {
            "head": self.head,
            "chest": self.chest,
            "legs": self.legs,
            "boots": self.boots,
            "hands": self.hands,
            "weapon": self.weapon,
            "offhand": self.offhand,
            "neck": self.neck,
            "ring": self.ring
        }

        print("Equipped Items:")
        for slot, item in equipped_slots.items():
            if item:
                print(f"{slot}: {item.name}")


equipment = Equipment()


class EquipmentStats:
    def __init__(self, item_class="", name=None, damage=None, armour=None, strength_bonus=None, dexterity_bonus=None,
                 intelligence_bonus=None, hp_bonus=None, mp_bonus=None):
        self.item_class = item_class
        self.name = name
        self.damage = damage
        self.armour = armour
        self.strength_bonus = strength_bonus
        self.dexterity_bonus = dexterity_bonus
        self.intelligence_bonus = intelligence_bonus
        self.hp_bonus = hp_bonus
        self.mp_bonus = mp_bonus

    def to_dict(self):
        return {
            "item_class": self.item_class,
            "name": self.name,
            "damage": self.damage,
            "armour": self.armour,
            "strength_bonus": self.strength_bonus,
            "dexterity_bonus": self.dexterity_bonus,
            "intelligence_bonus": self.intelligence_bonus,
            "hp_bonus": self.hp_bonus,
            "mp_bonus": self.mp_bonus
        }


equipmentStats = EquipmentStats()

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

    def dictionary_for_items(self):
        return {
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


equipment = Equipment()


class EquipmentStats:
    def __init__(self):
        self.name = None
        self.damage = None
        self.armour = None
        self.strength_bonus = None
        self.dexterity_bonus = None
        self.intelligence_bonus = None
        self.hp_bonus = None
        self.mp_bonus = None


equipmentStats = EquipmentStats()

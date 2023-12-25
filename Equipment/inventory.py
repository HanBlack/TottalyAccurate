class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        item_already_exists = any(existing_item.name == item.name for existing_item in self.items)

        if not item_already_exists:
            item_data = {
                f"Name: {item.name}\n"
                f"Damage: {item.damage}\n"
                f"Armour: {item.armour}\n"
                f"Strength Bonus: {item.strength_bonus}\n"
                f"Dexterity Bonus: {item.dexterity_bonus}\n"
                f"Intelligence Bonus: {item.intelligence_bonus}\n"
                f"HP Bonus: {item.hp_bonus}\n"
                f"MP Bonus: {item.mp_bonus}\n\n"
            }
            self.items.append(item_data)
        else:
            item_data = {
                f"Name: {item.name}\n"
                f"Damage: {item.damage}\n"
                f"Armour: {item.armour}\n"
                f"Strength Bonus: {item.strength_bonus}\n"
                f"Dexterity Bonus: {item.dexterity_bonus}\n"
                f"Intelligence Bonus: {item.intelligence_bonus}\n"
                f"HP Bonus: {item.hp_bonus}\n"
                f"MP Bonus: {item.mp_bonus}\n\n"
            }
            self.items.append(item_data)

    def load_equipment_from_file(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                slot, item_name = line.strip().split(": ")
                setattr(self, slot, item_name)


inventory = Inventory()

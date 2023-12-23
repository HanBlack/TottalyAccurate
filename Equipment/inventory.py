from Character import character


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Check if the item is already in the inventory
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
                # You need to create instances of equipment based on the loaded item_name
                # For instance, if you have classes like Helmet, Sword, etc., create instances based on the item_name
                # Example: self.head = Helmet() or self.weapon = Sword()
                # This is just a placeholder and might vary based on your implementation

                # Assign the loaded items to respective equipment slots
                setattr(self, slot, item_name)  # For demonstration, this assumes item_name is the name of the equipment


inventory = Inventory()

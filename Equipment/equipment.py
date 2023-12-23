import tkinter as tk


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

    # def load_equipped_gear_from_file(self, file_path):

    # Code to load the character's currently equipped gear from a file
    # Similar logic to the previously shown loading method can be used

    # def save_inventory_to_file(self, file_path):

    # Code to save the character's inventory to a file
    # This can follow a similar structure as the save_equipped_gear_to_file method

    # def load_inventory_from_file(self, file_path):


# Code to load the character's inventory from a file
# This method would resemble the previous methods for loading data from a file


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


def create_save_equipped_gear_gui():
    # Create an instance of Equipment
    player_equipment = Equipment()

    # Function to save equipped gear to a file
    def save_equipped_gear():
        file_path = "equipped_gear.txt"  # Change the file path as needed
        player_equipment.save_equipped_gear_to_file(file_path)
        status_label.config(text="Equipped gear saved successfully!")

    # Create the GUI window
    root = tk.Tk()
    root.title("Save Equipped Gear")

    # Button to trigger saving equipped gear
    save_button = tk.Button(root, text="Save Equipped Gear", command=save_equipped_gear)
    save_button.pack()

    # Label to display the status of the save operation
    status_label = tk.Label(root, text="")
    status_label.pack()

    root.mainloop()

# Call the function to create and display the GUI

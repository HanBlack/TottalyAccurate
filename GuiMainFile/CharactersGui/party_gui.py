import json
import tkinter as tk
from tkinter import ttk
from Character.character import Character
from Character.character import warrior, rogue, mage, cleric, druid, shaman, paladin, assassin, monk, necromancer, \
    hunter
from Character.character_load_inventory import open_file_to_get_characters, open_file_to_get_items
import program
import os
from Equipment.equipment import Equipment, EquipmentStats

character = Character()
warrior_instance = warrior
rogue = rogue
mage = mage
cleric = cleric
druid = druid
shaman = shaman
paladin = paladin
assassin = assassin
monk = monk
hunter = hunter
necromancer = necromancer
equipment = Equipment()


def party_gui(root):
    valid_path = program.current_directory()
    characters_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave')
    items_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave', 'CharacterInventory')

    loaded_items = open_file_to_get_items(items_directory_path)
    loaded_characters = open_file_to_get_characters(characters_directory_path)

    def on_character_selected(event):
        selected_character_name = character_combobox.get()
        display_character_stats(selected_character_name)

    def display_character_stats(selected_character_name):
        for character in loaded_characters:
            if character.name == selected_character_name:
                character_class = type(character).__name__
                character_stats_label.config(text=f"Character Stats:\n"
                                                  f"Class: {character_class}\n"
                                                  f"Name: {character.name}\n"
                                                  f"HP: {character.hp}\n"
                                                  f"MP: {character.mp}\n"
                                                  f"Strength: {character.strength}\n"
                                                  f"Dexterity: {character.dexterity}\n"
                                                  f"Intelligence: {character.intelligence}\n"
                                                  f"Experience: {character.experience}\n"
                                                  f"Level: {character.level}\n"
                                                  f"Status Effect: {character.statusEffect}")
                display_equipped_item_stats(selected_character_name)  # Update equipped item stats
                break

    def display_equipped_item_stats(selected_character_name):
        equipped_items_text = "Equipped Items:\n"
        for character in loaded_characters:
            if character.name == selected_character_name:
                equipped_items = character.equipment.dictionary_for_items()
                for slot, item in equipped_items.items():
                    if item:
                        if isinstance(item, dict):
                            equipped_items_text += f"Slot: {slot}, Name: {item['name']}\n"
                        else:
                            equipped_items_text += f"Slot: {slot}, Name: {item.name}\n"
                equipped_item_stats_label.config(text=equipped_items_text)
                break

    def equip_item(event=None):
        selected_character_name = character_combobox.get()
        selected_item_name = selected_item.get()

        for character in loaded_characters:
            if character.name == selected_character_name:
                for item in loaded_items:
                    if item.name == selected_item_name:
                        character.equipment.equip_item(item)
                        print(f"Equipped item '{item.name}' to '{character.name}'")

                        # Add a print statement specifically for legs
                        if item.item_class == "Legs":
                            print(f"This is a Legs item: {item.name}")

                        break
                break

        display_character_stats(selected_character_name)
        display_equipped_item_stats(selected_character_name)

    def unequip_item(event=None):
        selected_character_name = character_combobox.get()
        selected_slot = equipped_slot_combobox.get()

        for character in loaded_characters:
            if character.name == selected_character_name:
                character.equipment.unequip_item(selected_slot.lower())
                break

        display_character_stats(selected_character_name)
        display_equipped_item_stats(selected_character_name)
        update_item_stats()

    def update_item_stats(event=None):
        selected_item_name = selected_item.get()

        for item in loaded_items:
            if item.name == selected_item_name:
                if isinstance(item, EquipmentStats):  # Check if it's an EquipmentStats object
                    print(f"Legs Item - Name: {item.name}, Armour: {item.armour}")  # Print legs item details
                item_stats_label.config(text=f"Selected Item Stats:\n"
                                             f"Name: {item.name}\n"
                                             f"Damage: {item.damage}\n"
                                             f"Armour: {item.armour}\n"
                                             f"Strength Bonus: {item.strength_bonus}\n"
                                             f"Dexterity Bonus: {item.dexterity_bonus}\n"
                                             f"Intelligence Bonus: {item.intelligence_bonus}\n"
                                             f"HP Bonus: {item.hp_bonus}\n"
                                             f"MP Bonus: {item.mp_bonus}")
                break

    def save_equipped_items():
        selected_character_name = character_combobox.get()
        for character in loaded_characters:
            if character.name == selected_character_name:
                character_class = type(character).__name__
                character_file_path = os.path.join(characters_directory_path, f"{character.name}.json")
                character_data = {
                    "class": character_class,
                    "name": character.name,
                    "hp": character.hp,
                    "mp": character.mp,
                    "strength": character.strength,
                    "dexterity": character.dexterity,
                    "intelligence": character.intelligence,
                    "experience": character.experience,
                    "level": character.level,
                    "statusEffect": character.statusEffect,
                    "equipment": character.equipment.dictionary_for_items(),
                    "character_class": character_class
                }
                with open(character_file_path, 'w') as file:
                    json.dump(character_data, file, indent=4)
                    print(f"Saved character '{character.name}' along with equipped items to '{character_file_path}'")
                break

    def on_closing():
        window.destroy()  # Destroy the Toplevel window
        root.deiconify()  # Show the main window again

    window = tk.Toplevel(root)
    window.title("Character Inventory GUI")
    window.columnconfigure(0, weight=1)

    main_frame = ttk.Frame(window)
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    character_frame = ttk.Frame(main_frame)
    character_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky="nsew")

    if loaded_characters:
        character_label = ttk.Label(character_frame, text="Select Character", font=("Arial", 12, "bold"))
        character_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        character_combobox = ttk.Combobox(character_frame, values=[character.name for character in loaded_characters])
        character_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        character_combobox.bind("<<ComboboxSelected>>", on_character_selected)
        character_combobox.bind("<<ComboboxSelected>>",
                                lambda event: display_equipped_item_stats(character_combobox.get()))
        character_combobox.bind("<<ComboboxSelected>>",
                                lambda event: display_character_stats(character_combobox.get()))

    inventory_frame = ttk.Frame(main_frame)
    inventory_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    selected_item = tk.StringVar()
    if loaded_items:
        inventory_label = ttk.Label(inventory_frame, text="Select Item", font=("Arial", 12, "bold"))
        inventory_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        item_combobox = ttk.Combobox(inventory_frame, textvariable=selected_item,
                                     values=[item.name for item in loaded_items])
        item_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        item_combobox.bind("<<ComboboxSelected>>", update_item_stats)

    equipment_frame = ttk.Frame(main_frame)
    equipment_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    equipped_slot_combobox = ttk.Combobox(equipment_frame,
                                          values=["weapon", "offhand", "head", "chest", "hands", "boots", "legs",
                                                  "neck", "ring"])
    equipped_slot_combobox.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    equip_button = ttk.Button(equipment_frame, text="Equip Item", command=equip_item)
    equip_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    unequip_button = ttk.Button(equipment_frame, text="Unequip Item", command=unequip_item)
    unequip_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    stats_frame = ttk.Frame(main_frame)
    stats_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    character_stats_label = ttk.Label(stats_frame, text="Character Stats:", font=("Arial", 12, "bold"))
    character_stats_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    equipped_item_stats_label = ttk.Label(stats_frame, text="Equipped Item Stats:", font=("Arial", 12, "bold"))
    equipped_item_stats_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    item_stats_label = ttk.Label(stats_frame, text="Selected Item Stats:", font=("Arial", 12, "bold"))
    item_stats_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    save_button = ttk.Button(stats_frame, text="Save Equipped Items", command=save_equipped_items)
    save_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

    window.protocol("WM_DELETE_WINDOW", on_closing)

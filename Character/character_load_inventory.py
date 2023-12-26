import os
import json
from Equipment.equipment import EquipmentStats
from Character.character import Character
from Character.character_load import open_file_to_get_characters
import program

character = Character()


def open_file_to_get_items(directory_path):
    items = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    item_data = json.load(file)
                    item_instance = EquipmentStats(
                        item_class=item_data.get('class', None),
                        name=item_data.get('name', None),
                        damage=item_data.get('damage', None),
                        armour=item_data.get('armour', None),
                        strength_bonus=item_data.get('strength_bonus', None),
                        dexterity_bonus=item_data.get('dexterity_bonus', None),
                        intelligence_bonus=item_data.get('intelligence_bonus', None),
                        hp_bonus=item_data.get('hp_bonus', None),
                        mp_bonus=item_data.get('mp_bonus', None)
                    )
                    items.append(item_instance)
            except FileNotFoundError as e:
                print(f"File '{file_path}' not found: {e}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file '{file_path}': {e}")
    return items


valid_path = program.current_directory()
characters_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave')
items_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave', 'CharacterInventory')

loaded_items = open_file_to_get_items(items_directory_path)
loaded_characters = open_file_to_get_characters(characters_directory_path)

if loaded_characters:
    for character in loaded_characters:
        if loaded_items:
            for item in loaded_items:
                character.equipment.equip_item(item)

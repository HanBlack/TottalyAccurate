import Character.character_load_inventory
import program
import os
from Equipment.equipment import EquipmentStats, Equipment
from Character.character_load import open_file_to_get_characters
from Character.character_load_inventory import open_file_to_get_items
from Character.character import Character

character = Character()

equipment = Equipment()
valid_path = program.current_directory()
characters_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave')
loaded_characters = open_file_to_get_characters(characters_directory_path)
items_directory_path = os.path.join(valid_path, 'Character', 'CharacterSave', 'CharacterInventory')
loaded_items = open_file_to_get_items(items_directory_path)
equipment_stats_list = []

for item in loaded_items:
    equipment_stat = EquipmentStats(
        item_class=item.item_class,
        name=item.name,
        damage=item.damage,
        armour=item.armour,
        strength_bonus=item.strength_bonus,
        dexterity_bonus=item.dexterity_bonus,
        intelligence_bonus=item.intelligence_bonus,
        hp_bonus=item.hp_bonus,
        mp_bonus=item.mp_bonus
    )

    equipment_stats_list.append(equipment_stat)

    equipment.equip_item(item)

if loaded_characters:
    character_to_equip = loaded_characters[0]
    for item in loaded_items:
        character_to_equip.equipment.equip_item(item)
        break

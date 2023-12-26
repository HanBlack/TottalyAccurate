import tkinter as tk
import json
import os
import program
from Character.character import Character
from Equipment.equipment import Equipment
from Character.character import Warrior, Rogue, Mage, Cleric, Druid, Shaman, Paladin, Assassin, Monk, Necromancer, \
    Hunter

valid_path = program.current_directory()
directory_path = os.path.join(valid_path, 'Character', 'CharacterSave')


def open_file_to_get_characters(directory_path):
    characters = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    character_data = json.load(file)

                    character_class_name = character_data.get('class')  # Get the character class from JSON
                    if character_class_name == 'Warrior':
                        character_instance = Warrior()
                    elif character_class_name == 'Mage':
                        character_instance = Mage()
                    elif character_class_name == 'Cleric':
                        character_instance = Cleric()
                    elif character_class_name == 'Hunter':
                        character_instance = Hunter()
                    elif character_class_name == 'Shaman':
                        character_instance = Shaman()
                    elif character_class_name == 'Paladin':
                        character_instance = Paladin()
                    elif character_class_name == 'Assassin':
                        character_instance = Assassin()
                    elif character_class_name == 'Necromaner':
                        character_instance = Necromancer()
                    elif character_class_name == 'Druid':
                        character_instance = Druid()
                    elif character_class_name == 'Monk':
                        character_instance = Monk()
                    elif character_class_name == 'Rogue':
                        character_instance = Rogue()
                    else:
                        character_instance = Character()

                    character_instance.name = character_data.get('name', character_instance.name)
                    character_instance.hp = character_data.get('hp', character_instance.hp)
                    character_instance.mp = character_data.get('mp', character_instance.mp)
                    character_instance.strength = character_data.get('strength', character_instance.strength)
                    character_instance.dexterity = character_data.get('dexterity', character_instance.dexterity)
                    character_instance.intelligence = character_data.get('intelligence',
                                                                         character_instance.intelligence)
                    character_instance.experience = character_data.get('experience', character_instance.experience)
                    character_instance.level = character_data.get('level', character_instance.level)
                    character_instance.statusEffect = character_data.get('statusEffect',
                                                                         character_instance.statusEffect)

                    equipment_data = character_data.get('equipment', {})
                    character_instance.equipment = Equipment()
                    character_instance.equipment.__dict__.update(equipment_data)

                    characters.append(character_instance)
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except Exception as e:
                print(f"Error: {e}")

    return characters

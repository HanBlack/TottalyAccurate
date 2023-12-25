import json
import tkinter as tk
from Character import character
import random
import os
import program

character_instances = {
    'warrior': character.character.create_character('warrior'),
    'rogue': character.character.create_character('rogue'),
    'mage': character.character.create_character('mage'),
    'cleric': character.character.create_character('cleric'),
    'hunter': character.character.create_character('hunter'),
    'necromancer': character.character.create_character('necromancer'),
    'monk': character.character.create_character('monk'),
    'assassin': character.character.create_character('assassin'),
    'paladin': character.character.create_character('paladin'),
    'shaman': character.character.create_character('shaman'),
    'druid': character.character.create_character('druid')
}


def make_recruitment_random():
    character_classes_lowercase = list(character_instances.keys())
    population_to_recruit = random.randint(3, 6)

    selected_classes_lowercase = random.sample(character_classes_lowercase, k=population_to_recruit)

    recruited_characters = []
    for class_name in selected_classes_lowercase:
        recruited_characters.append(class_name)

    return recruited_characters


def display_character_info(player, frame, class_name):
    header_label = tk.Label(frame, text=class_name.capitalize(), font=("Arial", 12, "bold"))
    header_label.grid(row=0, column=0, columnspan=2, pady=5)

    info_labels = [
        f"Name: {player.name}",
        f"HP: {player.hp}",
        f"MP: {player.mp}",
        f"Strength: {player.strength}",
        f"Dexterity: {player.dexterity}",
        f"Intelligence: {player.intelligence}",
        f"Experience: {player.experience}",
        f"Level: {player.level}",
        f"Status Effect: {player.statusEffect}" if player.statusEffect else "Status Effect: None"
    ]

    for i, info in enumerate(info_labels):
        label = tk.Label(frame, text=info)
        label.grid(row=i + 1, column=0, sticky="w")


variable_for_path = program.current_directory()


def recruit_character(character_class, recruit_button):
    new_character = character_instances[character_class.lower()]
    class_name = type(new_character).__name__
    path = variable_for_path
    directory = os.path.join(path, 'Character', 'CharacterSave')
    file_name = f"{class_name}_{new_character.name}.json"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'a') as file:
        character_data = {
            "class": class_name,
            "name": new_character.name,
            "hp": new_character.hp,
            "mp": new_character.mp,
            "strength": new_character.strength,
            "dexterity": new_character.dexterity,
            "intelligence": new_character.intelligence,
            "experience": new_character.experience,
            "level": new_character.level,
            "statusEffect": new_character.statusEffect,
            "equipment": new_character.equipment.dictionary_for_items()
        }
        json.dump(character_data, file)
        file.write('\n')

    recruit_button.config(state=tk.DISABLED)


def create_character_spreed_sheet_for_recruit(frame, class_name, row_position, column_position):
    class_frame = tk.Frame(frame)
    class_frame.grid(row=row_position, column=column_position, padx=5, pady=5)

    player = character_instances[class_name.lower()]

    stats_frame = tk.Frame(class_frame, padx=10, pady=15)
    stats_frame.grid(row=0, column=0, pady=5, sticky="w")

    display_character_info(player, stats_frame, class_name)

    recruit_button = tk.Button(
        class_frame,
        text=f"Recruit {class_name}",
        command=lambda cn=class_name.lower(), button=None: recruit_character(cn, button)
    )
    recruit_button.grid(row=1, column=0, pady=5, sticky="w")

    recruit_button.configure(command=lambda cn=class_name.lower(), btn=recruit_button: recruit_character(cn, btn))

    return row_position + 1 if (column_position + 1) % 4 == 0 else row_position, (column_position + 1) % 4


def character_recruit_gui_run():
    root = tk.Tk()
    root.title("Game")

    character_classes = make_recruitment_random()

    row_pos = 0
    col_pos = 0
    for char_class in character_classes:
        row_pos, col_pos = create_character_spreed_sheet_for_recruit(root, char_class, row_pos, col_pos)
    root.mainloop()

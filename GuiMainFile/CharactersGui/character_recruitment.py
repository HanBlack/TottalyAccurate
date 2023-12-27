import json
import tkinter as tk
from Character.character import Character
import random
import os
import program

character_instances = {
    'warrior': Character.create_character('warrior'),
    'rogue': Character.create_character('rogue'),
    'mage': Character.create_character('mage'),
    'cleric': Character.create_character('cleric'),
    'hunter': Character.create_character('hunter'),
    'necromancer': Character.create_character('necromancer'),
    'monk': Character.create_character('monk'),
    'assassin': Character.create_character('assassin'),
    'paladin': Character.create_character('paladin'),
    'shaman': Character.create_character('shaman'),
    'druid': Character.create_character('druid')
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

character = Character()


def recruit_character(character_class, recruit_button):
    new_character = character_instances[character_class.lower()]
    class_name = type(new_character).__name__
    path = variable_for_path
    directory = os.path.join(path, 'Character', 'CharacterSave')
    file_name = f"{new_character.name}.json"
    file_path = os.path.join(directory, file_name)
    print(class_name)
    character = Character(character_class=class_name)
    character.name = new_character.name
    character.hp = new_character.hp
    character.mp = new_character.mp
    character.strength = new_character.strength
    character.dexterity = new_character.dexterity
    character.intelligence = new_character.intelligence
    character.experience = new_character.experience
    character.level = new_character.level
    character.statusEffect = new_character.statusEffect
    character.equipment = new_character.equipment

    with open(file_path, 'a') as file:
        character_data = {
            "class": class_name,
            "name": character.name,
            "hp": character.hp,
            "mp": character.mp,
            "strength": character.strength,
            "dexterity": character.dexterity,
            "intelligence": character.intelligence,
            "experience": character.experience,
            "level": character.level,
            "statusEffect": character.statusEffect,
            "equipment": character.equipment.get_equipped_items()
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

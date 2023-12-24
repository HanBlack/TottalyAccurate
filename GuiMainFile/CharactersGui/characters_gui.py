import tkinter as tk
from Character import character
import random



def generate_default_characters():
    character_classes = [
        'Warrior', 'Rogue', 'Mage', 'Cleric', 'Hunter', 'Necromancer',
        'Monk', 'Assassin', 'Paladin', 'Shaman', 'Druid'
    ]
    default_characters = [character.character.create_character(class_name.lower()) for class_name in character_classes]
    return default_characters


def make_recruitment_random():
    character_classes_lowercase = [
        'warrior', 'rogue', 'mage', 'cleric', 'hunter', 'necromancer',
        'monk', 'assassin', 'paladin', 'shaman', 'druid'
    ]
    population_to_recruit = random.randint(1, 5)

    # Make sure the recruitment is unique
    selected_classes_lowercase = random.sample(character_classes_lowercase, k=population_to_recruit)

    recruited_characters = []
    for class_name in selected_classes_lowercase:
        new_character = character.character.create_character(class_name)
        recruited_characters.append(type(new_character).__name__)

    return recruited_characters

def display_character_info(player, frame):
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
        label.grid(row=i, column=0, sticky="w")


def recruit_character(players_list, character_class, recruit_window):
    new_character = character.character.create_character(character_class)
    players_list.append(new_character)
    class_name = type(new_character).__name__


def create_character_spreed_sheet_for_recruit(frame, players_list, class_name, row_position, column_position):
    class_frame = tk.Frame(frame)
    class_frame.grid(row=row_position, column=column_position, padx=5, pady=5)  # Use grid manager instead of pack

    players_of_class = [player for player in players_list if type(player).__name__ == class_name]

    for idx, player in enumerate(players_of_class):
        stats_frame = tk.Frame(class_frame, padx=10, pady=15)
        stats_frame.grid(row=idx, column=0, pady=5, sticky="w")  # Use grid manager

        display_character_info(player, stats_frame)

        recruit_button = tk.Button(class_frame, text=f"Recruit {class_name}",
                                   command=lambda p=player, cn=class_name.lower(): recruit_character(players_list, cn,
                                                                                                     frame))
        recruit_button.grid(row=idx + 1, column=0, pady=5, sticky="w")  # Use grid manager for buttons

    return row_position + 1 if (column_position + 1) % 4 == 0 else row_position, (
                                                                                         column_position + 1) % 4


def character_recruit_gui_run():
    root = tk.Tk()
    root.title("Game")

    players = generate_default_characters()

    character_classes = make_recruitment_random()

    row_pos = 0
    col_pos = 0
    for char_class in character_classes:
        row_pos, col_pos = create_character_spreed_sheet_for_recruit(root, players, char_class, row_pos, col_pos)
    root.mainloop()

import tkinter as tk
from Character import character
from Equipment import equipment


def display_character_info(player):
    def show_info():
        character_info_window = tk.Toplevel()
        character_info_window.title("Character Information")

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

        for info in info_labels:
            label = tk.Label(character_info_window, text=info)
            label.pack()

    return show_info


def recruit_character(players_list, character_class):
    new_character = character.character.create_character(character_class)
    players_list.append(new_character)
    class_name = type(new_character).__name__
    info_button = tk.Button(root, text=f"{class_name} {len(players_list)} Info",
                            command=display_character_info(new_character))
    info_button.pack(padx=20, pady=5)


def character_gui_run():
    global root

    root = tk.Tk()
    root.title("Game")

    players = []

    # Buttons to recruit each class
    recruit_warrior_button = tk.Button(root, text="Recruit Warrior",
                                       command=lambda: recruit_character(players, 'warrior'))
    recruit_warrior_button.pack(padx=20, pady=10)

    recruit_rogue_button = tk.Button(root, text="Recruit Rogue",
                                     command=lambda: recruit_character(players, 'rogue'))
    recruit_rogue_button.pack(padx=20, pady=10)

    recruit_mage_button = tk.Button(root, text="Recruit Mage",
                                    command=lambda: recruit_character(players, 'mage'))
    recruit_mage_button.pack(padx=20, pady=10)

    recruit_cleric_button = tk.Button(root, text="Recruit Cleric",
                                      command=lambda: recruit_character(players, 'cleric'))
    recruit_cleric_button.pack(padx=20, pady=10)

    recruit_hunter_button = tk.Button(root, text="Recruit Hunter",
                                      command=lambda: recruit_character(players, 'hunter'))
    recruit_hunter_button.pack(padx=20, pady=10)

    recruit_necromancer_button = tk.Button(root, text="Recruit Necromancer",
                                           command=lambda: recruit_character(players, 'necromancer'))
    recruit_necromancer_button.pack(padx=20, pady=10)

    recruit_monk_button = tk.Button(root, text="Recruit Monk",
                                    command=lambda: recruit_character(players, 'monk'))
    recruit_monk_button.pack(padx=20, pady=10)

    recruit_assassin_button = tk.Button(root, text="Recruit Assassin",
                                        command=lambda: recruit_character(players, 'assassin'))
    recruit_assassin_button.pack(padx=20, pady=10)

    recruit_paladin_button = tk.Button(root, text="Recruit Paladin",
                                       command=lambda: recruit_character(players, 'paladin'))
    recruit_paladin_button.pack(padx=20, pady=10)

    recruit_shaman_button = tk.Button(root, text="Recruit Shaman",
                                      command=lambda: recruit_character(players, 'shaman'))
    recruit_shaman_button.pack(padx=20, pady=10)

    recruit_druid_button = tk.Button(root, text="Recruit Druid",
                                     command=lambda: recruit_character(players, 'druid'))
    recruit_druid_button.pack(padx=20, pady=10)

    root.mainloop()


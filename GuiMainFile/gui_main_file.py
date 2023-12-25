import tkinter as tk
from GuiMainFile.CharactersGui import character_recruitment, party_gui, party_inventory_gui


def open_characters_window():
    character_recruitment.character_recruit_gui_run()


def open_recruit_characters(main_window):
    main_window.withdraw()
    open_characters_window()


def open_display_characters_window():
    party_gui.display_character_gui()


def open_display_characters(main_window):
    main_window.withdraw()
    open_display_characters_window()


def open_display_items_window():
    party_inventory_gui.display_items_gui()


def open_display_items(main_window):
    main_window.withdraw()
    open_display_items_window()


def game_run():
    root = tk.Tk()
    root.title("Main Page")

    recruit_characters_button = tk.Button(root, text="Recruit Characters",
                                          command=lambda: open_recruit_characters(root))
    recruit_characters_button.pack(padx=20, pady=10)

    display_characters_button = tk.Button(root, text="Characters",
                                          command=lambda: open_display_characters(root))
    display_characters_button.pack(padx=20, pady=10)

    items_characters_button = tk.Button(root, text="Open inventory",
                                        command=lambda: open_display_items(root))
    items_characters_button.pack(padx=20, pady=10)

    root.mainloop()


game_run()

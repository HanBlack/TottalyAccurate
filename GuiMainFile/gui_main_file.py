import tkinter as tk
from GuiMainFile.CharactersGui import characters_gui


def open_characters_window():
    characters_gui.character_recruit_gui_run()


def open_recruit_characters(main_window):
    main_window.withdraw()
    open_characters_window()


def game_run():
    root = tk.Tk()
    root.title("Main Page")

    recruit_characters_button = tk.Button(root, text="Recruit Characters",
                                          command=lambda: open_recruit_characters(root))
    recruit_characters_button.pack(padx=20, pady=10)

    root.mainloop()


game_run()

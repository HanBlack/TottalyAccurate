from tkinter import font

from Character.character_load import open_file_to_get_characters
from EnemyCharacter.Enemies.goblins import (
    drop_item_goblin_boss_loottable,
    drop_item_goblin_higher_evolution_loottable,
    drop_item_goblin_middle_evolution_loottable,
    drop_item_goblin_lower_evolution_loottable,
    LowerEvolutionGoblin,
    MiddleEvolutionGoblin,
    HigherEvolutionGoblin,
    BossEvolutionGoblin,
)
from Character.character import Character
import program
import os
import json
import time
import tkinter as tk

valid_path = program.current_directory()
directory_path = os.path.join(valid_path, "Character", "CharacterSave")


class CombatHandler:
    def __init__(self):
        self.characters = []
        self.enemy = None

    def load_characters(self, directory_path):
        loaded_characters = open_file_to_get_characters(directory_path)

        for friendly_character in loaded_characters:
            character = Character()
            character.set_from_friendly_character(friendly_character)
            self.characters.append(character)

    def load_enemy(self):
        self.enemy = LowerEvolutionGoblin.entrance_cave()

    def prepare_character_for_fight(self, friendly_character):
        equipped_items = friendly_character.equipment.get_equipped_items()

        total_armour = 0
        for slot, item_data in equipped_items.items():
            if "armour" in item_data:
                armour_value = item_data["armour"]
                if armour_value is not None:
                    total_armour += armour_value

        damage_reduction = int(total_armour * 0.1)
        damage_dealt_by_player = friendly_character.calculate_character_damage()
        player_critical_chance = friendly_character.calculate_player_critical_chance()
        scored_critical_hit = friendly_character.check_if_player_scored_critical_hit()

        return {
            "name": friendly_character.name,
            "total_armour": total_armour,
            "damage_reduction": damage_reduction,
            "damage_dealt_by_player": damage_dealt_by_player,
            "player_critical_chance": player_critical_chance,
            "scored_critical_hit": scored_critical_hit,
        }

    def prepare_enemy_for_fight(self, enemy):
        if isinstance(enemy, LowerEvolutionGoblin):
            damage_dealt_by_enemy = enemy.calculate_damage_done_by_enemy()
            enemy_critical_chance = enemy.calculate_enemy_critical_chance()
            scored_critical_hit = enemy.check_if_enemy_scored_critical_hit()

            enemy_prepared = {
                "damage_dealt_by_enemy": damage_dealt_by_enemy,
                "enemy_critical_chance": enemy_critical_chance,
                "scored_critical_hit": scored_critical_hit,
                # Add more attributes as needed for the fight preparation
            }

            return enemy_prepared
        elif isinstance(enemy, MiddleEvolutionGoblin):
            damage_dealt_by_enemy = enemy.calculate_damage_done_by_enemy()
            enemy_critical_chance = enemy.calculate_enemy_critical_chance()
            scored_critical_hit = enemy.check_if_enemy_scored_critical_hit()

            enemy_prepared = {
                "damage_dealt_by_enemy": damage_dealt_by_enemy,
                "enemy_critical_chance": enemy_critical_chance,
                "scored_critical_hit": scored_critical_hit,
            }
            return enemy_prepared
        elif isinstance(enemy, HigherEvolutionGoblin):
            damage_dealt_by_enemy = enemy.calculate_damage_done_by_enemy()
            enemy_critical_chance = enemy.calculate_enemy_critical_chance()
            scored_critical_hit = enemy.check_if_enemy_scored_critical_hit()

            enemy_prepared = {
                "damage_dealt_by_enemy": damage_dealt_by_enemy,
                "enemy_critical_chance": enemy_critical_chance,
                "scored_critical_hit": scored_critical_hit,
            }
            return enemy_prepared
        elif isinstance(enemy, BossEvolutionGoblin):
            damage_dealt_by_enemy = enemy.calculate_damage_done_by_enemy()
            enemy_critical_chance = enemy.calculate_enemy_critical_chance()
            scored_critical_hit = enemy.check_if_enemy_scored_critical_hit()

            enemy_prepared = {
                "damage_dealt_by_enemy": damage_dealt_by_enemy,
                "enemy_critical_chance": enemy_critical_chance,
                "scored_critical_hit": scored_critical_hit,
            }
            return enemy_prepared

    def drop_loot(self, defeated_enemy):
        path_variable = program.current_directory()
        path = path_variable

        print("Inside drop_loot method")
        print(f"Defeated enemy name: {defeated_enemy.name}")  # Display the name of the defeated enemy

        if isinstance(defeated_enemy, LowerEvolutionGoblin):
            dropped_item = drop_item_goblin_lower_evolution_loottable()
            print("Dropping item for Lower Evolution Goblin")
        elif isinstance(defeated_enemy, MiddleEvolutionGoblin):
            dropped_item = drop_item_goblin_middle_evolution_loottable()
            print("Dropping item for Middle Evolution Goblin")
        elif isinstance(defeated_enemy, HigherEvolutionGoblin):
            dropped_item = drop_item_goblin_higher_evolution_loottable()
            print("Dropping item for Higher Evolution Goblin")
        elif isinstance(defeated_enemy, BossEvolutionGoblin):
            dropped_item = drop_item_goblin_boss_loottable()
            print("Dropping item for Boss Evolution Goblin")
        else:
            dropped_item = None

        if dropped_item:
            class_name = type(dropped_item).__name__
            file_path = os.path.join(path, "Character", "CharacterSave", "CharacterInventory")
            file_name = f"{dropped_item.name}.json"
            file_path = os.path.join(file_path, file_name)
            with open(file_path, "a") as file:
                dropped_item_data = {
                    "class": class_name,
                    "name": dropped_item.name,
                    "damage": dropped_item.damage,
                    "armour": dropped_item.armour,
                    "strength_bonus": dropped_item.strength_bonus,
                    "dexterity_bonus": dropped_item.dexterity_bonus,
                    "intelligence_bonus": dropped_item.intelligence_bonus,
                    "hp_bonus": dropped_item.hp_bonus,
                    "mp_bonus": dropped_item.mp_bonus,
                }
                json.dump(dropped_item_data, file)
                file.write("\n")
            print(f"Item dropped: {dropped_item.name}")
        else:
            print("No item dropped.")
        return dropped_item.name

    def perform_combat(self):
        while self.enemy.hp > 0 and any(character.hp > 0 for character in self.characters):
            for friendly_character in self.characters:
                if self.enemy.hp <= 0:
                    break

                damage_dealt_by_player = friendly_character.calculate_character_damage()
                self.enemy.hp -= damage_dealt_by_player
                print(f"{friendly_character.name} deals {damage_dealt_by_player} damage to {self.enemy.name}")
                print(f"Enemy HP: {self.enemy.hp}")  # Print enemy HP after player attack

                if self.enemy.hp <= 0:
                    print(f"{self.enemy.name} has been defeated!")
                    self.drop_loot(self.enemy)
                    break

                for character in self.characters:
                    if character.hp > 0:
                        damage_dealt_by_enemy = self.enemy.calculate_damage_done_by_enemy()
                        character.hp -= damage_dealt_by_enemy
                        print(f"{self.enemy.name} deals {damage_dealt_by_enemy} damage to {character.name}")
                        print(f"{character.name} HP: {character.hp}")  # Print character HP after enemy attack

                        if character.hp <= 0:
                            print(f"{character.name} has been defeated!")
                            break

        print("Combat loop ended")

    def delete_defeated_character_file(self, defeated_character_name):
        valid_path = program.current_directory()
        directory_path = os.path.join(valid_path, "Character", "CharacterSave")
        characters_directory = directory_path
        all_files = os.listdir(characters_directory)
        for filename in all_files:
            if filename.startswith(defeated_character_name) and filename.endswith(".json"):
                character_file_path = os.path.join(characters_directory, filename)
                if os.path.exists(character_file_path):
                    os.remove(character_file_path)
                    print(f"{filename} has been permanently deleted.")
                    break
                else:
                    print(f"File for {filename} not found.")
        else:
            print(f"No file found for {defeated_character_name}.")


class CombatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Combat Simulator")
        self.combat_handler = CombatHandler()

        self.combat_frame = tk.Frame(self.root)
        self.combat_frame.pack()

        self.character_frame = tk.Frame(self.combat_frame, relief=tk.GROOVE, borderwidth=2)
        self.character_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N)

        self.text_box_frame = tk.Frame(self.combat_frame)
        self.text_box_frame.grid(row=0, column=1, padx=5, pady=5)

        self.text_box = tk.Text(self.text_box_frame, height=20, width=60, wrap='word')
        self.text_box.pack()

        self.enemy_frame = tk.Frame(self.combat_frame, relief=tk.GROOVE, borderwidth=2)
        self.enemy_frame.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)

        self.start_combat_button = tk.Button(self.root, text="Start Combat",
                                             command=self.perform_combat_with_gui_updates)
        self.start_combat_button.pack()

        self.load_stats()

    def load_stats(self):
        valid_path = program.current_directory()
        directory_path = os.path.join(valid_path, "Character", "CharacterSave")
        self.combat_handler.load_characters(directory_path)
        self.combat_handler.load_enemy()
        self.display_character_stats()
        self.display_enemy_stats()

    def display_character_stats(self):
        for widget in self.character_frame.winfo_children():
            widget.destroy()

        for idx, friendly_character in enumerate(self.combat_handler.characters):
            label_name = tk.Label(self.character_frame, text=f"{friendly_character.name}")
            label_name.grid(row=idx * 4, column=0, sticky=tk.W)
            label_name.config(font=("Arial", 12))  # Change font size here

            label_hp = tk.Label(self.character_frame, text=f"HP: {friendly_character.hp}")
            label_hp.grid(row=idx * 4 + 1, column=0, sticky=tk.W)
            label_hp.config(font=("Arial", 12))  # Change font size here

            label_strength = tk.Label(self.character_frame, text=f"Strength: {friendly_character.strength}")
            label_strength.grid(row=idx * 4 + 2, column=0, sticky=tk.W)
            label_strength.config(font=("Arial", 12))  # Change font size here

            label_dexterity = tk.Label(self.character_frame, text=f"Dexterity: {friendly_character.dexterity}")
            label_dexterity.grid(row=idx * 4 + 3, column=0, sticky=tk.W)
            label_dexterity.config(font=("Arial", 12))  # Change font size here

            label_intelligence = tk.Label(self.character_frame, text=f"Intelligence: {friendly_character.intelligence}")
            label_intelligence.grid(row=idx * 4 + 4, column=0, sticky=tk.W)
            label_intelligence.config(font=("Arial", 12))  # Change font size here

            label_damage = tk.Label(self.character_frame,
                                    text=f"Damage: {friendly_character.calculate_character_damage()}")
            label_damage.grid(row=idx * 4 + 5, column=0, sticky=tk.W)
            label_damage.config(font=("Arial", 12))  # Change font size here

            total_armor = self.combat_handler.prepare_character_for_fight(friendly_character)['total_armour']
            label_armor = tk.Label(self.character_frame, text=f"Armor: {total_armor}")
            label_armor.grid(row=idx * 4 + 6, column=0, sticky=tk.W)
            label_armor.config(font=("Arial", 12))

    def display_enemy_stats(self):
        for widget in self.enemy_frame.winfo_children():
            widget.destroy()  # Clear existing labels before updating

        if self.combat_handler.enemy:
            label_name = tk.Label(self.enemy_frame, text=f"{self.combat_handler.enemy.name}")
            label_name.grid(row=0, column=0, sticky=tk.W)
            label_name.config(font=("Arial", 12))  # Change font size here

            label_hp = tk.Label(self.enemy_frame, text=f"HP: {self.combat_handler.enemy.hp}")
            label_hp.grid(row=1, column=0, sticky=tk.W)
            label_hp.config(font=("Arial", 12))  # Change font size here

            label_strength = tk.Label(self.enemy_frame, text=f"Strength: {self.combat_handler.enemy.strength}")
            label_strength.grid(row=2, column=0, sticky=tk.W)
            label_strength.config(font=("Arial", 12))  # Change font size here

            label_dexterity = tk.Label(self.enemy_frame, text=f"Dexterity: {self.combat_handler.enemy.dexterity}")
            label_dexterity.grid(row=3, column=0, sticky=tk.W)
            label_dexterity.config(font=("Arial", 12))  # Change font size here

            label_intelligence = tk.Label(self.enemy_frame,
                                          text=f"Intelligence: {self.combat_handler.enemy.intelligence}")
            label_intelligence.grid(row=4, column=0, sticky=tk.W)
            label_intelligence.config(font=("Arial", 12))  # Change font size here

            label_damage = tk.Label(self.enemy_frame,
                                    text=f"Damage: {self.combat_handler.enemy.calculate_damage_done_by_enemy()}")
            label_damage.grid(row=5, column=0, sticky=tk.W)
            label_damage.config(font=("Arial", 12))  # Change font size here

    def update_character_stats(self):
        for idx, friendly_character in enumerate(self.combat_handler.characters):
            hp_label = tk.Label(self.character_frame, text=f"HP: {friendly_character.hp}")
            hp_label.grid(row=idx * 2 + 1, column=0, sticky=tk.W)
            hp_label.config(font=("Arial", 12))  # Change font size here

    def perform_combat_with_gui_updates(self):
        self.text_box.delete('1.0', tk.END)  # Clear the text box before starting combat

        # Define the bold Arial font
        bold_font = font.Font(family="Arial", size=12, weight="bold")

        while self.combat_handler.enemy and self.combat_handler.enemy.hp > 0 and any(
                character.hp > 0 for character in self.combat_handler.characters):
            for friendly_character in self.combat_handler.characters:
                if self.combat_handler.enemy.hp <= 0:
                    defeated_enemy = self.combat_handler.enemy  # Store the defeated enemy
                    self.combat_handler.drop_loot(defeated_enemy)  # Drop loot when enemy is defeated
                    break  # Exit the loop when the enemy is defeated

                damage_dealt_by_player = friendly_character.calculate_character_damage()
                self.combat_handler.enemy.hp -= damage_dealt_by_player
                self.text_box.insert(tk.END,
                                     f"{friendly_character.name} deals {damage_dealt_by_player} damage to {self.combat_handler.enemy.name}\n")
                # Apply the bold Arial font to the inserted text
                self.text_box.tag_configure("bold_12", font=bold_font)
                self.text_box.tag_add("bold_12", "1.0", "end")
                self.update_character_stats()  # Update character HP in GUI
                self.display_enemy_stats()  # Update displayed enemy HP
                self.text_box.update()
                time.sleep(1)  # Pause for 1 second between attacks

                if self.combat_handler.enemy.hp <= 0:
                    defeated_enemy = self.combat_handler.enemy  # Store the defeated enemy
                    dropped_item = self.combat_handler.drop_loot(defeated_enemy)  # Drop loot when enemy is defeated
                    self.text_box.insert(tk.END, f"The enemy dropped {dropped_item}!\n")  # Display dropped item

                    break  # Exit the loop when the enemy is defeated

                for character in self.combat_handler.characters:
                    if character.hp > 0:
                        damage_dealt_by_enemy = self.combat_handler.enemy.calculate_damage_done_by_enemy()
                        character.hp -= damage_dealt_by_enemy
                        self.text_box.insert(tk.END,
                                             f"{self.combat_handler.enemy.name} deals {damage_dealt_by_enemy} damage to {character.name}\n")
                        # Apply the bold Arial font to the inserted text
                        self.text_box.tag_configure("bold_12", font=bold_font)
                        self.text_box.tag_add("bold_12", "1.0", "end")
                        self.text_box.update()
                        time.sleep(1)  # Pause for 1 second between attacks

                        if character.hp <= 0:
                            self.text_box.insert(tk.END, f"{character.name} has been defeated!\n")
                            self.text_box.tag_configure("bold_12", font=bold_font)
                            self.text_box.tag_add("bold_12", "1.0", "end")
                            break

        self.text_box.insert(tk.END, "Battle is finished!\n")
        self.text_box.tag_configure("bold_12", font=bold_font)
        self.text_box.tag_add("bold_12", "1.0", "end")


def delete_character_file(character_name):
    characters_directory_path = "path_to_characters_directory"  # Replace with the actual directory path

    # List all files in the characters directory
    all_files = os.listdir(characters_directory_path)

    # Iterate through all files to find and delete the character's file by name
    for filename in all_files:
        if filename.startswith(character_name) and filename.endswith(".json"):
            character_file_path = os.path.join(characters_directory_path, filename)

            # Check if the character's file exists, and delete it if found
            if os.path.exists(character_file_path):
                os.remove(character_file_path)
                print(f"File for {character_name} has been permanently deleted.")
                break  # Stop searching after deleting the character file
            else:
                print(f"File for {character_name} not found.")
    else:
        print(f"No file found for {character_name}.")


if __name__ == "__main__":
    root = tk.Tk()
    combat_gui = CombatGUI(root)
    root.mainloop()

from Battle import character_vs_enemy_backhand

combat_handler = character_vs_enemy_backhand.CombatHandler()
combat_handler.load_characters()
combat_handler.load_enemy()


def perform_combat(self):
    for friendly_character in self.characters:
        prepared_character = self.prepare_character_for_fight(friendly_character)
        print(f"Prepared character for fight: {prepared_character}")

        enemy_prepared = self.prepare_enemy_for_fight(self.enemy)
        print(f"Prepared enemy for fight: {enemy_prepared}")

        while friendly_character.hp > 0 and self.enemy.hp > 0:
            print(f"Current HP - Character: {friendly_character.hp}, Enemy: {self.enemy.hp}")

            damage_dealt_by_player = friendly_character.calculate_character_damage()
            print(f"{friendly_character.name} deals {damage_dealt_by_player} damage to {self.enemy.name}")
            self.enemy.hp -= damage_dealt_by_player

            if self.enemy.hp <= 0:
                print(f"{self.enemy.name} has been defeated!")
                self.drop_loot(self.enemy)
                break

            damage_dealt_by_enemy = self.enemy.calculate_damage_done_by_enemy()
            print(f"{self.enemy.name} deals {damage_dealt_by_enemy} damage to {friendly_character.name}")
            friendly_character.hp -= damage_dealt_by_enemy

            if friendly_character.hp <= 0:
                print(f"{friendly_character.name} has been defeated!")
                break

        print("Combat loop ended")


combat_handler = character_vs_enemy_backhand.CombatHandler()
combat_handler.load_characters()
combat_handler.load_enemy()
combat_handler.perform_combat()

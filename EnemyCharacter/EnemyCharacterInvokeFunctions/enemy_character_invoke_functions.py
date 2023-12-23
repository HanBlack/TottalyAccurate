from EnemyCharacter.Enemies.goblins import LowerEvolutionGoblin, MiddleEvolutionGoblin, HigherEvolutionGoblin, \
    BossEvolutionGoblin
from Character import character
from Equipment.EquipmentList import equipment_list

lower_goblin = LowerEvolutionGoblin().dribblet_stat_set()
middle_goblin = MiddleEvolutionGoblin().gnarble_stat_set()
higher_goblin = HigherEvolutionGoblin().zilgok_stat_set()
boss_goblin = BossEvolutionGoblin().morgul_the_devourer_stat_set()

player = character.warrior
player.equipment.weapon = equipment_list.Weapon().common_sword_lvl_1_to_15()
enemy_player = boss_goblin
damage_dealt_by_player = player.calculate_character_damage()
damage_dealt_by_enemy_player = enemy_player.calculate_damage_done_by_enemy()
enemy_player.hp -= damage_dealt_by_player
player.hp -= damage_dealt_by_enemy_player

player.gain_experience_from_enemy(enemy_player)
print(f"{player.name}'s Level: {player.level} equipment: {player.equipment.weapon.damage}")

print(f"Player dealt {damage_dealt_by_player} damage to the boss.")
print(f"Boss's remaining HP: {boss_goblin.hp}")
print(f"{boss_goblin.name} dealt {damage_dealt_by_enemy_player} damage to {player.name}")
print(f"player's remaining HP: {player.hp}")

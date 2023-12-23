from EnemyCharacter.Enemies.goblins import LowerEvolutionGoblin, MiddleEvolutionGoblin, HigherEvolutionGoblin, \
    BossEvolutionGoblin
from Character import character
from Equipment.EquipmentList import helmet, chest, legs, boots, hands, neck, ring, shield, axe, bow, buckler, crossbow, \
    dagger, equipment_list, hammer, mana_orb, staff, sword, wand

from EnemyCharacter.Enemies import goblins
from Equipment import inventory

lower_goblin = LowerEvolutionGoblin().dribblet_stat_set()
middle_goblin = MiddleEvolutionGoblin().gnarble_stat_set()
higher_goblin = HigherEvolutionGoblin().zilgok_stat_set()
boss_goblin = BossEvolutionGoblin().morgul_the_devourer_stat_set()

player = character.warrior
player.equipment.weapon = sword.sword.common_sword_lvl_1_to_15()
player.equipment.head = helmet.helmet.common_helmets_lvl_1_to_15()
player_head_armor_value = player.calculate_character_armor_value()
player_damage_reduction = player.calculate_character_damage_reduction()
enemy_player = boss_goblin
damage_dealt_by_player = player.calculate_character_damage()
damage_dealt_by_enemy_player = enemy_player.calculate_damage_done_by_enemy()
enemy_player.hp -= damage_dealt_by_player
player.hp -= damage_dealt_by_enemy_player - player.calculate_character_damage_reduction()
if enemy_player.hp == 0:
    goblins.defeat_enemy_goblin_boss(enemy_player)

player.gain_experience_from_enemy(enemy_player)
print(f"{player.name}'s Level: {player.level} equipment: {player.equipment.weapon.damage}")

print(f"Player dealt {damage_dealt_by_player} damage to the boss.")
print(f"Boss's remaining HP: {boss_goblin.hp}")
print(f"{boss_goblin.name} dealt {damage_dealt_by_enemy_player} damage to {player.name}")
print(f"player's remaining HP: {player.hp}")

print(f"{player.name} has {player_damage_reduction} armor value")

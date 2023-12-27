import random


class ECharacter:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.level = 0
        self.statusEffect = {}

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        if value < 0:
            self._mp = 0
        else:
            self._mp = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if value < 0:
            self._strength = 0
        elif value > 100:
            self._strength = 100
        else:
            self._strength = value

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
        if value < 0:
            self._dexterity = 0
        elif value > 100:
            self._dexterity = 100
        else:
            self._dexterity = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        if value < 0:
            self._intelligence = 0
        elif value > 100:
            self._intelligence = 100
        else:
            self._intelligence = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        else:
            self._level = value

    def calculate_total_experience(self, defeated_enemy):
        base_exp = self.level * 90
        hp_multiplier = (self.hp / 10) + (defeated_enemy.hp / 20)
        strength_multiplier = (self.strength / 2) + (defeated_enemy.strength / 4)
        dexterity_multiplier = (self.dexterity / 2) + (
                defeated_enemy.dexterity / 4)
        intelligence_multiplier = (self.intelligence / 2) + (
                defeated_enemy.intelligence / 4)

        total_experience = base_exp + hp_multiplier + strength_multiplier + dexterity_multiplier + intelligence_multiplier
        return int(total_experience)

    def calculate_damage_done_by_enemy(self):
        primary_damage_deal_attribute = max(self.strength, self.dexterity, self.intelligence)

        if self.check_if_enemy_scored_critical_hit():
            primary_damage_deal_attribute = (primary_damage_deal_attribute * 2) - (self.level / 2)

        if primary_damage_deal_attribute <= 5:
            minimal_damage_done = int(primary_damage_deal_attribute) - 2
            maximal_damage_done = int(primary_damage_deal_attribute) + 2
        elif 5 <= primary_damage_deal_attribute <= 15:
            minimal_damage_done = int(primary_damage_deal_attribute) - 4
            maximal_damage_done = int(primary_damage_deal_attribute) + 4
        elif 15 <= primary_damage_deal_attribute <= 30:
            minimal_damage_done = int(primary_damage_deal_attribute) - 8
            maximal_damage_done = int(primary_damage_deal_attribute) + 8
        else:
            return int(primary_damage_deal_attribute)

        return random.randint(minimal_damage_done, maximal_damage_done)

    def calculate_enemy_critical_chance(self):
        base_chance = self.dexterity * 0.1
        level_modifier = 1 + (self.level * 0.05)
        chance_to_crit = base_chance * level_modifier
        chance_to_crit = min(chance_to_crit, 100)
        return chance_to_crit

    def check_if_enemy_scored_critical_hit(self):
        crit_chance = self.calculate_enemy_critical_chance()
        compare_number = random.randint(0, 100)
        return compare_number <= crit_chance

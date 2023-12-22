import random
import EnemyCharacter.echaracter


class Character:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.experience = 0
        self.level = 0
        self.statusEffect = None

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
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            self._experience = 0
        else:
            self._experience = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        else:
            self._level = value

    def increase_experience(self, amount):
        self._experience += amount
        while self._experience >= self.calculate_experience_needed_for_next_level():
            self.level_up()

    def calculate_experience_needed_for_next_level(self):
        return (150 * self.level) + self.strength + self.dexterity + self.intelligence + random.randint(1, 5)

    def level_up(self):
        experience_required = self.calculate_experience_needed_for_next_level()
        print(experience_required)
        if self._experience >= experience_required:
            self._experience -= experience_required
            self.level += 1
            return True
        else:
            return False

    def gain_experience_from_enemy(self, enemy):
        experience_gained = EnemyCharacter.echaracter.enemy_character.calculate_total_experience()
        self.increase_experience(experience_gained)
        print(f"{self.name} gained {experience_gained} experience from defeating {enemy.name}!")


character = Character()

player = Character()
player.name = "John"
player.level = 0
player.strength = 10
player.dexterity = 5
player.intelligence = 6
enemy_player = EnemyCharacter.echaracter.enemy_character

player.gain_experience_from_enemy(enemy_player)

print(f"{player.name}'s Level: {player.level}")

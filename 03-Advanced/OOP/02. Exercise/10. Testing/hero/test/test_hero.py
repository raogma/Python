from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('raogma', 10, 100, 4)
        self.enemy_hero = Hero('ograma', 20, 200, 5)

    def test_proper_construction(self):
        self.assertEqual(self.hero.username, 'raogma')
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 4)

    def test_battle_method_same_username(self):
        self.enemy_hero.username = 'raogma'
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(exc.exception), "You cannot fight yourself")

    def test_battle_method_without_enough_health(self):
        data = (0, -42)
        for health in data:
            self.hero.health = health
            with self.assertRaises(ValueError) as exc:
                self.hero.battle(self.enemy_hero)
            self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_method_without_enough_health_enemy(self):
        data = (0, -42)
        for health in data:
            self.enemy_hero.health = health
            with self.assertRaises(ValueError) as exc:
                self.hero.battle(self.enemy_hero)
            self.assertEqual(str(exc.exception), f'You cannot fight {self.enemy_hero.username}. He needs to rest')

    def test_battle_method_hero_wins(self):
        self.hero = Hero('raogma', level=1, health=5, damage=3)
        self.enemy_hero = Hero('ograma', level=1, health=1, damage=2)
        old_level = self.hero.level
        old_health = self.hero.health
        old_damage = self.hero.damage
        self.assertEqual(self.hero.battle(self.enemy_hero), 'You win')
        self.assertEqual(self.hero.level, old_level + 1)
        self.assertEqual(self.hero.health, old_health + 5 - self.enemy_hero.damage * self.enemy_hero.level)
        self.assertEqual(self.hero.damage, old_damage + 5)

    def test_battle_method_enemy_wins(self):
        self.hero = Hero('ograma', level=1, health=1, damage=2)
        self.enemy_hero = Hero('raogma', level=1, health=5, damage=3)
        old_level = self.enemy_hero.level
        old_health = self.enemy_hero.health
        old_damage = self.enemy_hero.damage
        self.assertEqual(self.hero.battle(self.enemy_hero), 'You lose')
        self.assertEqual(self.enemy_hero.level, old_level + 1)
        self.assertEqual(self.enemy_hero.health, old_health + 5 - self.hero.damage * self.hero.level)
        self.assertEqual(self.enemy_hero.damage, old_damage + 5)

    def test_battle_method_draw(self):
        self.hero = Hero('ograma', level=1, health=1, damage=2)
        self.enemy_hero = Hero('raogma', level=1, health=1, damage=2)
        self.assertEqual(self.hero.battle(self.enemy_hero), 'Draw')

    def test_class_representation(self):
        self.assertEqual(self.hero.__str__(), f"Hero {self.hero.username}: {self.hero.level} lvl\n" 
                                              f"Health: {self.hero.health}\n" 
                                              f"Damage: {self.hero.damage}\n")


if __name__ == '__main__':
    main()

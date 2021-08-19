class Player:

    def __init__(self, name, health, strength, speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed

    def __str__(self):
        print(f'{self.name}')

    def damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def buff(self, sp_inc, str_inc):
        self.speed += sp_inc
        self.strength += str_inc

    def nerf(self, sp_dec, str_dec):
        self.speed -= sp_dec
        self.strength -= str_dec


class Monster:

    def __init__(self, health, strength, speed):
        self.health = health
        self.strength = strength
        self.speed = speed

    def damage(self, amount):
        self.health -= amount


class Object:

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __str__(self):
        print(f'{self.name}')



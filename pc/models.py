from django.db import models


class PC(models.Model):
    RACE_CHOICES = [
        ("dragonborn", "Dragonborn"),
        ("dwarf", "Dwarf"),
        ("elf", "Elf"),
        ("gnome", "Gnome"),
        ("half-elf", "Half-Elf"),
        ("half-orc", "Half-Orc"),
        ("halfling", "Halfling"),
        ("human", "Human"),
        ("tiefling", "Tiefling"),
    ]

    CLASS_CHOICES = [
        ("barbarian", "Barbarian"),
        ("bard", "Bard"),
        ("cleric", "Cleric"),
        ("druid", "Druid"),
        ("fighter", "Fighter"),
        ("monk", "Monk"),
        ("paladin", "Paladin"),
        ("ranger", "Ranger"),
        ("rogue", "Rogue"),
        ("sorcerer", "Sorcerer"),
        ("warlock", "Warlock"),
        ("wizard", "Wizard"),
    ]

    age = models.PositiveIntegerField()
    actions = models.TextField()
    charisma = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    description = models.CharField(max_length=256)
    dexterity = models.PositiveIntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    intelligence = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    occupation = models.CharField(max_length=100)
    pc_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    race = models.CharField(max_length=20, choices=RACE_CHOICES)
    strength = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()

    def __str__(self):
        return self.name

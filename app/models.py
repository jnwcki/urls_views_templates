from django.db import models

# Create your models here.

PLAYER_POSITIONS = [
    ('RD', 'Right Defense'),
    ('LD', 'Left Defense'),
    ('C', 'Center'),
    ('RW', 'Right Wing'),
    ('LW', 'Left Wing'),
    ('G', 'Goaltender')
]

class Stat(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    player_position = models.CharField(max_length=20, choices=PLAYER_POSITIONS, default='G')
    weight = models.IntegerField(default=0)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.number, self.player_position,
                                    self.weight)

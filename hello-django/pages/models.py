from django.db import models

# Create your models here.
class Hero(models.Model):
    hero_id = models.IntegerField(primary_key=True)
    hero_name = models.CharField(max_length=60)
    pro_win = models.IntegerField()
    pro_pick = models.IntegerField()

    # specify table name
    class Meta:
        db_table = "hero"


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    rank_tier = models.FloatField()
    win = models.FloatField()
    lose = models.FloatField()
    mmr_estimate = models.FloatField()

    # specify table name
    class Meta:
        db_table = "player"

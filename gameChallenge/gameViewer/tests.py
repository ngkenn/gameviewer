from gameViewer.models import Game
from django.test import TestCase

# Very basic test to check if object saved and slugified properly
class GameModelTest(TestCase):
    def setUp(self):
        Game.objects.create(name="GOD OF WAR", platform="PS4",
         genre="FIGHTING", release_date="2018-01-07", 
         n_players=4, publisher="SONY INTERACTIVE ENTERTAINMENT")

    def test_game_slug(self):
        god_of_war = Game.objects.get(name="GOD OF WAR")
        god_of_war.save()
        self.assertEqual(god_of_war.slug, "god-of-war")




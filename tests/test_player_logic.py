import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entities.player import Player



class TestPlayerLogic(unittest.TestCase):
    def test_heal_overflow(self):
        """Test critique : Le soin ne doit jamais dépasser la vie max"""

        player = Player(0, 0)
        player.max_hp = 100
        player.current_hp = 90


        player.heal(50)


        self.assertEqual(player.current_hp, 100, "Erreur logique : Les PV dépassent le maximum autorisé !")


if __name__ == '__main__':
    unittest.main()
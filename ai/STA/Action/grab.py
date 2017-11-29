# Under MIT license, see LICENSE.txt
import numpy as np

from RULEngine.GameDomainObjects.Player import Player
from RULEngine.Util.Pose import Pose
from ai.STA.Action.Action import Action
from ai.Util.ai_command import AICommand, AICommandType
from ai.states.game_state import GameState

__author__ = 'Robocup ULaval'


class Grab(Action):
    def __init__(self, game_state: GameState, player: Player):
        """
            :param game_state: L'etat courant du jeu.
            :param player: Instance du joueur qui se deplace
        """
        Action.__init__(self, game_state, player)

    def exec(self):
        ball = self.game_state.get_ball_position()
        return AICommand(self.player, AICommandType.MOVE, pose_goal=Pose(ball, self.player.pose.orientation), pathfinder_on=True)

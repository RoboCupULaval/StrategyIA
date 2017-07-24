# Under MIT license, see LICENSE.txt

from RULEngine.Game.OurPlayer import OurPlayer
from RULEngine.Util.Pose import Pose

from ai.states.game_state import GameState
from ai.STA.Action.Action import Action
from ai.Util.ai_command import AICommand, AICommandType


class Kick(Action):

    def __init__(self, game_state: GameState, player: OurPlayer, p_force: [int, float], target: Pose=Pose(), end_speed=0,
                 cruise_speed=0.1):
        """
            :param game_state: Current state of the game
            :param player: Instance of the player
            :param p_force: Kick force [0, 10]
        """
        # TODO check the force not used by the new interface! MGL 2017/05/23
        Action.__init__(self, game_state, player)
        assert(isinstance(p_force, (int, float)))
        self.force = p_force
        self.target = target
        self.end_speed = end_speed
        self.cruise_speed = cruise_speed

    def exec(self):
        """
        Execute the kick command
        :return: Un AIcommand
        """
        target = self.target.position
        player = self.player.pose.position
        player_to_target = target - player
        #if player_to_target.norm() > 0:
        player_to_target = self.target.position
        ball_position = self.game_state.get_ball_position()
        orientation = (self.target.position - ball_position).angle()

        # else:
        #     player_to_target = SpeedPose()

        cmd_params = {"pose_goal": Pose(ball_position, orientation),
                      "kick": True,
                      "pathfinder_on": True,
                      "kick_strength": self.force,
                      "cruise_speed": 0.1,
                      "end_speed": self.end_speed}
        # print("command kick")
        return AICommand(self.player, AICommandType.MOVE, **cmd_params)

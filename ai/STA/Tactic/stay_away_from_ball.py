# Under MIT license, see LICENSE.txt
from typing import List

from Util import Pose
from Util.ai_command import MoveTo
from Util.area import stayOutsideCircle
from ai.GameDomainObjects import Player
from ai.STA.Tactic.go_to_position_pathfinder import GoToPositionPathfinder
from ai.STA.Tactic.tactic import Tactic
from ai.states.game_state import GameState


class StayAwayFromBall(Tactic):
    def __init__(self, game_state: GameState, player: Player, target: Pose = Pose(),
                 keepout_radius: int = 500, args: List[str]=None):
        super().__init__(game_state, player, target, args)
        self.current_state = self.stay_out_of_circle
        self.next_state = self.stay_out_of_circle
        self.keepout_radius = keepout_radius

    def stay_out_of_circle(self):
        position = stayOutsideCircle(self.player.pose.position,
                                     self.game_state.ball_position,
                                     self.keepout_radius)
        return MoveTo(position)

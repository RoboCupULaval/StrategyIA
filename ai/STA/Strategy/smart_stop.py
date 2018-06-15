# Under MIT License, see LICENSE.txt

from functools import partial

from Util.constant import KEEPOUT_DISTANCE_FROM_BALL
from Util.pose import Position, Pose
from Util.role import Role

from ai.Algorithm.evaluation_module import closest_player_to_point, closest_players_to_point
from ai.Algorithm.path_partitionner import Obstacle
from ai.STA.Strategy.strategy import Strategy
from ai.STA.Tactic.align_around_the_ball import AlignAroundTheBall
from ai.STA.Tactic.align_to_defense_wall import AlignToDefenseWall
from ai.STA.Tactic.go_kick import GoKick
from ai.STA.Tactic.goalkeeper import GoalKeeper
from ai.STA.Tactic.position_for_pass import PositionForPass
from ai.STA.Tactic.rotate_around_ball import RotateAroundBall
from ai.STA.Tactic.tactic_constants import Flags
from ai.states.game_state import GameState


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic
class SmartStop(Strategy):
    DEFENDERS = [Role.FIRST_DEFENCE, Role.SECOND_DEFENCE]
    def __init__(self, p_game_state):
        super().__init__(p_game_state)

        formation_defender = [p for r, p in self.assigned_roles.items() if r in self.DEFENDERS]
        formation_around_ball = [p for r, p in self.assigned_roles.items() if r not in self.DEFENDERS and r != Role.GOALKEEPER]
        for role, player in self.assigned_roles.items():
            if role == Role.GOALKEEPER:
                self.create_node(Role.GOALKEEPER, GoalKeeper(self.game_state, player))
            elif role in self.DEFENDERS:
                self.create_node(role, AlignToDefenseWall(self.game_state,
                                                          player,
                                                          robots_in_formation=formation_defender,
                                                          object_to_block=self.game_state.ball,
                                                          stay_away_from_ball=True))
            else:
                self.create_node(role, AlignAroundTheBall(self.game_state,
                                                          player,
                                                          robots_in_formation=formation_around_ball))

    def obstacles(self):
        return [Obstacle(self.game_state.ball_position.array, avoid_distance=KEEPOUT_DISTANCE_FROM_BALL)]

    @classmethod
    def required_roles(cls):
        return [Role.GOALKEEPER,
                Role.FIRST_ATTACK,
                Role.FIRST_DEFENCE]

    @classmethod
    def optional_roles(cls):
        return [Role.SECOND_ATTACK,
                Role.MIDDLE,
                Role.SECOND_DEFENCE]



# Under MIT License, see LICENSE.txt
import numpy as np
from functools import partial

from Util.pose import Pose
from Util.role import Role
from Util.role_mapping_rule import keep_prev_mapping_otherwise_random
from ai.STA.Strategy.strategy import Strategy
from ai.STA.Strategy.team_go_to_position import TeamGoToPosition
from ai.STA.Tactic.go_to_position_pathfinder import GoToPositionPathfinder
from ai.STA.Tactic.goalkeeper import GoalKeeper
from ai.STA.Tactic.stop import Stop
from ai.STA.Tactic.tactic_constants import Flags
from ai.states.game_state import GameState


class PrepareKickOffOffense(TeamGoToPosition):

    def __init__(self, p_game_state):
        super().__init__(p_game_state)

        # Positions objectifs des joueurs
        attack_top_position = Pose.from_values(self.game_state.field.our_goal_x / 15,
                                               self.game_state.field.bottom * 3 / 5, 0)
        attack_bottom_position = Pose.from_values(self.game_state.field.our_goal_x / 15,
                                                  self.game_state.field.top * 3 / 5, 0)
        middle_position = Pose.from_values(self.game_state.field.our_goal_x / 15, 0, 0)
        defense_top_position = Pose.from_values(self.game_state.field.our_goal_x / 2,
                                                self.game_state.field.top / 3, 0)
        defense_bottom_position = Pose.from_values(self.game_state.field.our_goal_x / 2,
                                                   self.game_state.field.bottom / 3, 0)

        goalkeeper = self.assigned_roles[Role.GOALKEEPER]
        self.create_node(Role.GOALKEEPER, GoalKeeper(self.game_state, goalkeeper))

        role_to_positions = {Role.FIRST_ATTACK: attack_top_position,
                             Role.SECOND_ATTACK: attack_bottom_position,
                             Role.MIDDLE: middle_position,
                             Role.FIRST_DEFENCE: defense_top_position,
                             Role.SECOND_DEFENCE: defense_bottom_position}

        self.assign_tactics(role_to_positions)

    @classmethod
    def required_roles(cls):
        return {r: keep_prev_mapping_otherwise_random for r in [Role.GOALKEEPER,
                                                                Role.MIDDLE]
                }

    @classmethod
    def optional_roles(cls):
        return {r: keep_prev_mapping_otherwise_random for r in [Role.FIRST_ATTACK,
                                                                Role.SECOND_ATTACK,
                                                                Role.FIRST_DEFENCE,
                                                                Role.SECOND_DEFENCE]
                }


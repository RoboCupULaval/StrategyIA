# Under MIT license, see LICENSE.txt
from Util.constant import ROBOT_RADIUS
from Util.pose import Pose
from Util.role import Role

from ai.STA.Strategy.team_go_to_position import TeamGoToPosition
from ai.STA.Tactic.goalkeeper import GoalKeeper
from ai.states.game_state import GameState


class PreparePenaltyOffense(TeamGoToPosition):
    def __init__(self, p_game_state):
        super().__init__(p_game_state)
        field = self.game_state.field
        our_goal = field.our_goal_pose

        role_to_positions = {Role.FIRST_ATTACK:   Pose.from_values(our_goal.position.x / 8, field.top * 2 / 3),
                             Role.SECOND_ATTACK:  Pose.from_values(our_goal.position.x / 8, field.top / 3),
                             Role.MIDDLE:         Pose.from_values(field.their_goal_area.right + 3 * ROBOT_RADIUS, 0),
                             Role.FIRST_DEFENCE:  Pose.from_values(our_goal.position.x / 8, field.bottom / 3),
                             Role.SECOND_DEFENCE: Pose.from_values(our_goal.position.x / 8, field.bottom * 2 / 3)}

        goalkeeper = self.game_state.get_player_by_role(Role.GOALKEEPER)
        self.create_node(Role.GOALKEEPER, GoalKeeper(self.game_state, goalkeeper, penalty_kick=True))

        self.assign_tactics(role_to_positions)

    @classmethod
    def required_roles(cls):
        return [Role.GOALKEEPER,
                Role.MIDDLE]

    @classmethod
    def optional_roles(cls):
        return [Role.FIRST_ATTACK,
                Role.SECOND_ATTACK,
                Role.FIRST_DEFENCE,
                Role.SECOND_DEFENCE]

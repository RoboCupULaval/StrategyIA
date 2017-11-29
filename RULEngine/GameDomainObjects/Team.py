# Under MIT License, see LICENSE.txt
from typing import Dict

from RULEngine.services.team_color_service import TeamColor


class Team:
    def __init__(self, team_color: TeamColor):
        assert isinstance(team_color, TeamColor)

        self._team_color = team_color
        self._players = {}
        self._onplay_players = {}

    @property
    def team_color(self) -> TeamColor:
        return self._team_color

    @property
    def players(self) -> Dict:
        return self._players

    @property
    def onplay_player(self):
        return self._onplay_players

    @property
    def team_color(self):
        return self._team_color

    def has_player(self, player):
        for this_team_player in self.players.values():
            if this_team_player is player:
                return True
        return False

    def is_team_yellow(self):
        return self.team_color == TeamColor.YELLOW

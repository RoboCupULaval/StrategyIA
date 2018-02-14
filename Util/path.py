import numpy as np

from Util import Position


class Path:
    # FIXME remove speed from pathfinder, it shouldn't be its concern
    def __init__(self, start=Position(),  end=Position(), start_speed=0, end_speed=0):

        self.start = start
        self.goal = end
        self.points = [start, end]
        self.speeds = [start_speed, end_speed]
        self.turns = self.points

    def join_segments(self, other):
        new_path = Path()
        new_path.points = self.points+other.points[1:]
        new_path.start = self.start
        new_path.goal = other.points[-1]
        return new_path

    def split_path(self, idx):
        if idx < 1:
            path_1 = Path()
            path_2 = self
        else:
            path_1 = Path()
            path_1.start = self.start
            path_1.goal = self.points[idx]
            path_1.points = self.points[:idx+1]
            path_2 = Path()
            path_2.start = self.points[idx]
            path_2.goal = self.goal
            path_2.points = self.points[idx:]
        return path_1, path_2

    @staticmethod
    def generate_path_from_points(points_list, speed_list=None, threshold=None, turns_list=None):
        if speed_list is None or len(speed_list) < 2:
            speed_list = [0, 0]
        if len(points_list) < 2:
            points_list = [points_list[0], points_list[0]]
        if len(points_list) < 3:
            pass
        else:
            for i in range(0, len(points_list)-1):
                if threshold is not None:
                    if np.linalg.norm(points_list[i] - points_list[i+1]) < threshold:
                        del points_list[i+1]
                    # print(position_list)
                    # print(new_speed_list)
        # points étant une liste de positions
        new_path = Path()
        new_path.start = points_list[0]
        new_path.goal = points_list[-1]
        if turns_list is None or len(turns_list) < 2:
            turns_list = [new_path.start, new_path.goal]
        new_path.points = points_list
        new_path.speeds = speed_list
        new_path.turns = turns_list

        return new_path

    @classmethod
    def from_dict(cls, dict):
        points = [Position.from_dict(p) for p in dict]
        path = Path.generate_path_from_points(points)
        return path

    def to_dict(self):
        return [p.to_dict() for p in self.points]

    def get_path_length(self):
        length = 0
        for idx, point in enumerate(self.points[:-1]):
            length += np.linalg.norm(point - self.points[idx+1])
        return length

    def quick_update_path(self, position):
        self.points[0] = position
        return Path().generate_path_from_points(self.points, self.speeds, None)



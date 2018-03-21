
from Util import Position, Path
from Engine.robot import Robot, MAX_LINEAR_ACCELERATION
from math import sqrt, sin


def path_smoother(robot: Robot):

    path = robot.raw_path.copy()
    path.start = robot.position

    if len(path) < 3:
        return path, robot.end_speed

    p1 = path[0]
    p2 = path[1]
    p3 = path[2]

    p4, p5 = compute_circle_points(p1, p2, p3, robot.cruise_speed, acc=MAX_LINEAR_ACCELERATION)

    if (p1 - p2).norm < (p4 - p2).norm or (p3 - p2).norm < (p5 - p2).norm:
        point_list = path[:3]
    else:
        point_list = [path.start, p4, p5]

    turn_radius, _ = compute_turn_radius(*point_list, speed=robot.cruise_speed, acc=MAX_LINEAR_ACCELERATION)
    next_speed = speed_in_corner(turn_radius, acc=MAX_LINEAR_ACCELERATION)

    return Path.from_points(point_list), next_speed


def compute_circle_points(p1, p2, p3, speed, acc):
    turn_radius, deviation_from_path = compute_turn_radius(p1, p2, p3, speed, acc)
    distance_on_segment = sqrt((deviation_from_path + turn_radius) ** 2 - turn_radius ** 2)
    p4 = point_on_segment(p2, p1, distance_on_segment)
    p5 = point_on_segment(p2, p3, distance_on_segment)

    return p4, p5


def speed_in_corner(radius, acc):

    speed = sqrt(radius * acc)

    return speed


def compute_turn_radius(p1, p2, p3, speed, max_deviation=50, acc=MAX_LINEAR_ACCELERATION):
    """Assume the raw path is p1->p2->p3.
       Deviation is compute from p2 to the circle with a line passing by the center of the circle."""

    radius_at_const_speed = speed ** 2 / acc
    path_angle = (p3 - p2).angle - (p1 - p2).angle

    const_speed_deviation = deviation(radius_at_const_speed, path_angle)

    if const_speed_deviation < max_deviation:
        deviation_from_path = const_speed_deviation
        turn_radius = radius_at_const_speed
    else:
        deviation_from_path = max_deviation
        turn_radius = deviation_from_path / (1 / sin(path_angle / 2) - 1)

    return turn_radius, deviation_from_path


def deviation(radius, theta):
    return radius / sin(theta / 2) - radius if sin(theta/2) != 0 else 0


def point_on_segment(start: Position, end: Position, distance: float):
    ratio = distance / (start-end).norm
    return start * (1-ratio) + end * ratio

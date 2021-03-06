from typing import Tuple

from Util import Position, Path
from Engine.Controller.robot import MAX_LINEAR_ACCELERATION
from math import sqrt, sin

from Util.geometry import wrap_to_pi


def path_smoother(path, speed, end_speed) -> Tuple[Path, float]:

    if end_speed < 200:
        end_speed = 0 # un end_speed tres petit prooque un overshoot en vitesse vraiment disproportione.
    if len(path) < 3:
        return path, end_speed

    p1 = path[0]
    p2 = path[1]
    p3 = path[2]

    p4, p5 = compute_circle_points(p1, p2, p3, speed, acc=MAX_LINEAR_ACCELERATION)

    if (p1 - p2).norm < (p4 - p2).norm or (p3 - p2).norm < (p5 - p2).norm:
        point_list = path[:3]
    else:
        point_list = [path.start, p4, p5]
    turn_radius, _ = compute_turn_radius(*point_list, speed, acc=MAX_LINEAR_ACCELERATION)
    next_speed = speed_in_corner(turn_radius, acc=MAX_LINEAR_ACCELERATION)
    next_speed = min(500.0, next_speed)
    return Path.from_sequence(point_list), next_speed


def compute_circle_points(p1, p2, p3, speed: float, acc: float) -> Tuple[Position, Position]:
    turn_radius, deviation_from_path = compute_turn_radius(p1, p2, p3, speed, acc=acc)
    distance_on_segment = sqrt((deviation_from_path + turn_radius) ** 2 - turn_radius ** 2)
    p4 = point_on_segment(p2, p1, distance_on_segment)
    p5 = point_on_segment(p2, p3, distance_on_segment)

    return p4, p5


def speed_in_corner(radius: float, acc: float) -> float:

    speed = sqrt(radius * acc)

    return speed


def compute_turn_radius(p1, p2, p3, speed: float, max_deviation: float=50, acc: float=MAX_LINEAR_ACCELERATION) -> Tuple[float, float]:
    """Assume the raw path is p1->p2->p3.
       Deviation is compute from p2 to the circle with a line passing by the center of the circle."""

    radius_at_const_speed = speed ** 2 / acc
    path_angle = wrap_to_pi((p3 - p2).angle - (p1 - p2).angle)
    const_speed_deviation = deviation(radius_at_const_speed, path_angle)
    if const_speed_deviation < max_deviation:
        speed_deviation = const_speed_deviation
        turn_radius = radius_at_const_speed
    else:
        speed *= 0.95
        radius = speed ** 2 / acc
        speed_deviation = deviation(radius, path_angle)
        turn_radius = speed_deviation / (1 / sin(path_angle / 2) - 1)
        while speed_deviation > max_deviation:
            speed *= 0.9
            radius = speed ** 2 / acc
            speed_deviation = deviation(radius, path_angle)
            turn_radius = speed_deviation / (1 / sin(path_angle / 2) - 1)
            if abs(speed) < 0.01:
                speed_deviation = 0
                turn_radius = 0
                break
    return abs(turn_radius), speed_deviation


def deviation(radius: float, theta: float) -> float:
    return abs(radius / sin(theta / 2)) - radius if sin(theta/2) != 0 else 0


def point_on_segment(start: Position, end: Position, distance: float):
    ratio = distance / (start-end).norm
    return start * (1-ratio) + end * ratio


def is_time_to_break(initial_speed, final_speed, delta_positon):
    return delta_positon < ((final_speed ** 2 - initial_speed ** 2) / 2 * MAX_LINEAR_ACCELERATION)


def get_good_speed_to_break(final_speed, delta_position):
    if final_speed ** 2 < 2 * MAX_LINEAR_ACCELERATION * delta_position:
        return 0
    return sqrt(final_speed ** 2 - 2 * MAX_LINEAR_ACCELERATION * delta_position)

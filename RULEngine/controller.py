
from multiprocessing import Queue
from queue import Empty
import logging
from math import cos, sin

from RULEngine.Util.PID import PID

from config.config_service import ConfigService

from typing import Dict, List

MAX_ROBOT = 12


def get_control_setting(game_type: str):

    if game_type == 'sim':
        translation = {'kp': .001, 'ki': 0.0005, 'kd': 0}
        rotation = {'kp': .002, 'ki': .001, 'kd': 0.0001}
    elif game_type == 'real':
        translation = {'kp': .001, 'ki': 0.0005, 'kd': 0}
        rotation = {'kp': .001, 'ki': 0.0035, 'kd': 0.0001}
    else:
        raise TypeError('No matching game type found in control setting')

    return {'translation': translation, 'rotation': rotation}


class Controller(list):
    def __init__(self, ai_queue: Queue):
        self.ai_queue = ai_queue

        logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.DEBUG)
        self.logger = logging.getLogger("Controller")

        self.cfg = ConfigService()

        control_setting = get_control_setting(self.cfg.config_dict['GAME']['type'])

        super().__init__(Robot(control_setting, robot_id) for robot_id in range(MAX_ROBOT))

    def update(self, robots_states: List[Dict]):
        for robot_states in robots_states:
            robot_id = robot_states['id']
            self[robot_id].update(robot_states)
            self[robot_id]['is_active'] = True

        try:
            ai_commands = self.ai_queue.get(block=False)
            for cmd in ai_commands:
                robot_id = cmd['id']
                self[robot_id]['target'] = cmd['target']
                self[robot_id]['control_type'] = cmd['control_type']
                self[robot_id]['kick_type'] = cmd['kick_type']
                self[robot_id]['has_target'] = True

        except Empty:
            pass

    def execute(self) -> Dict:

        active_robots = iter(robot for robot in self if robot['is_active'] and robot['has_target'])
        cmds = dict()
        for robot in active_robots:
            error = {state: robot['pose'][state] - robot['target'][state] for state in robot['pose']}
            command = robot['controller'].execute(error)
            command['x'], command['y'] = rotate(command['x'], command['y'], -robot['pose']['orientation'])
            robot['command'] = command
            cmds[robot['id']] = robot['command']
        return cmds


class Robot(dict):
    def __init__(self, control_setting, robot_id):
        super().__init__()
        self['controller'] = MotionControl(control_setting)
        self['command'] = {'x': None, 'y': None, 'orientation': None}
        self['target'] = {'x': None, 'y': None, 'orientation': None}
        self['pose'] = {'x': None, 'y': None, 'orientation': None}
        self['velocity'] = {'x': None, 'y': None, 'orientation': None}
        self['control_type'] = {'x': 'position', 'y': 'position', 'orientation': 'position'}
        self['kick_type'] = None
        self['is_active'] = False
        self['has_target'] = False
        self['id'] = robot_id


class MotionControl(object):
    def __init__(self, control_setting: Dict):
        self.control_setting = control_setting
        self.controllers = {'x': PID(**self.control_setting['translation']),
                            'y': PID(**self.control_setting['translation']),
                            'orientation': PID(**self.control_setting['rotation'], wrap_error=True)}

    def execute(self, error: Dict) -> Dict:
        return {state: self.controllers[state].execute(error[state]) for state in self.controllers}

    def reset(self):
        for controller in self.controllers.values():
            controller.reset()


def rotate(x: float, y: float, angle: float):
    return [cos(angle) * x - sin(angle) * y, sin(angle) * x + cos(angle) * y]


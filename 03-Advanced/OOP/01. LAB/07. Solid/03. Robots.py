from abc import ABC, abstractmethod


class Robot:
    sensors = None

    @abstractmethod
    def get_sensors(self):
        ...


class Android(Robot, ABC):
    sensors = 4

    def get_sensors(self):
        return self.__class__.sensors


class Chappie(Robot, ABC):
    sensors = 6

    def get_sensors(self):
        return self.__class__.sensors


def count_robot_sensors(robots: list):
    for robot in robots:
        print(robot.get_sensors())


robots = [Android(), Chappie()]
count_robot_sensors(robots)

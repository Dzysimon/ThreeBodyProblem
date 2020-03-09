# coding = utf-8

import numpy as np


class Star:

    def __init__(self, pos_x, pos_y, pos_z, mess=1):
        """
        Initialize a point.
        :param pos_x: x coordinate
        :param pos_y: y coordinate
        :param pos_z: z coordinate
        :param mess: mess of the point
        """
        self.__pos_x = float(pos_x)
        self.__pos_y = float(pos_y)
        self.__pos_z = float(pos_z)
        self.__mess = mess

    def get_x(self):
        """
        show x coordinate
        :return: float x
        """
        return self.__pos_x

    def set_x(self, x):
        self.__pos_x = x

    def get_y(self):
        return self.__pos_y

    def set_y(self, y):
        self.__pos_y = y

    def get_z(self):
        return self.__pos_z

    def set_z(self, z):
        self.__pos_z = z

    def get_mess(self):
        return self.__mess

    def __relative_coordinates(self, star):
        delta_x = star.get_x() - self.__pos_x
        delta_y = star.get_y() - self.__pos_y
        delta_z = star.get_z() - self.__pos_z
        return delta_x, delta_y, delta_z

    def distance(self, star):
        pos = self.__relative_coordinates(star)
        return np.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2)

    def gravitation(self, star, G=1):
        pos = self.__relative_coordinates(star)
        dis = self.distance(star)
        force_total = self.__mess*star.get_mess()*G/(dis**2)
        k = []
        for i in range(3):
            k.append(pos[i]/dis)
        force_x = force_total*k[0]
        force_y = force_total*k[1]
        force_z = force_total*k[2]
        return force_x, force_y, force_z



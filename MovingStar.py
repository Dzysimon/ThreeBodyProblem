# coding = utf-8

from Stars import Star
import copy
from decimal import Decimal


class MovingStar(Star):
    total_T = Decimal('0')
    delta_t = 0

    def __init__(self, pos_x, pos_y, pos_z, mess=1, velocity=[0, 0, 0], dt=0.01):
        super().__init__(pos_x, pos_y, pos_z, mess)
        self.velocity = copy.deepcopy(velocity)
        self.acc = [0, 0, 0]
        MovingStar.delta_t = Decimal(str(dt))

    def acceleration(self, star, star2):
        force = self.gravitation(star, 6.67425)
        force2 = self.gravitation(star2, 10)
        self.acc[0] = (force[0] + force2[0])/self.get_mess()
        self.acc[1] = (force[1] + force2[1])/self.get_mess()
        self.acc[2] = (force[2] + force2[2])/self.get_mess()

    def set_position(self):
        delta = [0, 0, 0]
        for i in range(3):
            delta[i] = self.velocity[i]*MovingStar.delta_t + 0.5*self.acc[i]*MovingStar.delta_t**2
        self.set_x(self.get_x() + delta[0])
        self.set_y(self.get_y() + delta[1])
        self.set_z(self.get_z() + delta[2])

    def get_position(self):
        return self.get_x(), self.get_y(), self.get_z()

    def set_velocity(self):
        for i in range(3):
            self.velocity[i] = self.acc[i]*MovingStar.delta_t + self.velocity[i]

# coding = utf-8

from MovingStar import MovingStar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as pl


class ThreeBodyProblem:

    def __init__(self, star1, star2, star3):
        self.__s1 = star1
        self.__s2 = star2
        self.__s3 = star3

    def run(self):
        p1 = [[], [], []]
        p2 = [[], [], []]
        p3 = [[], [], []]

        while MovingStar.total_T < 100:
            pos1 = self.__s1.get_position()
            pos2 = self.__s2.get_position()
            pos3 = self.__s3.get_position()
            print('t={:.6f}'.format(MovingStar.total_T) +
                  ' s1({:+.6f},{:+.6f},{:+.6f})'.format(pos1[0], pos1[1], pos1[2]) +
                  ' s2({:+.6f},{:+.6f},{:+.6f})'.format(pos2[0], pos2[1], pos2[2]) +
                  ' s3({:+.6f},{:+.6f},{:+.6f})'.format(pos3[0], pos3[1], pos3[2]))
            for i in range(3):
                p1[i].append(pos1[i])
                p2[i].append(pos2[i])
                p3[i].append(pos3[i])
            self.__s1.acceleration(self.__s2, self.__s3)
            self.__s2.acceleration(self.__s1, self.__s3)
            self.__s3.acceleration(self.__s1, self.__s2)
            self.__s1.set_position()
            self.__s2.set_position()
            self.__s3.set_position()
            self.__s1.set_velocity()
            self.__s2.set_velocity()
            self.__s3.set_velocity()
            MovingStar.total_T += MovingStar.delta_t

        fig = pl.figure()
        ax = Axes3D(fig)
        ax.plot3D(p1[0], p1[1], p1[2], c='r')
        ax.plot3D(p2[0], p2[1], p2[2], c='b')
        ax.plot3D(p3[0], p3[1], p3[2], c='y')
        plt.show()


if __name__ == "__main__":

    TBP = ThreeBodyProblem(MovingStar(0.0, 0.0, 0.0, 0.01, 1, [0, 0, 0]),
                           MovingStar(10.0, 0.0, 0.0, 0.01, 1, [0, 1, 0]),
                           MovingStar(0.0, 0.0, 10.0, 0.01, 1, [-1, 0, 0]))
    TBP.run()

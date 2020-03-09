# coding = utf-8

from MovingStar import MovingStar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as pl


s1 = MovingStar(0.0, 0.0, 0.0, 0.01, 1, [0, 0, 0])
s2 = MovingStar(10.0, 0.0, 0.0, 0.01, 1, [0, 1, 0])
s3 = MovingStar(0.0, 0.0, 10.0, 0.01, 1, [-1, 0, 0])


if __name__ == "__main__":
    p1 = [[], [], []]
    p2 = [[], [], []]
    p3 = [[], [], []]

    while MovingStar.total_T < 100:
        pos1 = s1.get_position()
        pos2 = s2.get_position()
        pos3 = s3.get_position()
        print('t={:.6f}'.format(MovingStar.total_T)+
              ' s1({:+.6f},{:+.6f},{:+.6f})'.format(pos1[0], pos1[1], pos1[2])+
              ' s2({:+.6f},{:+.6f},{:+.6f})'.format(pos2[0], pos2[1], pos2[2])+
              ' s3({:+.6f},{:+.6f},{:+.6f})'.format(pos3[0], pos3[1], pos3[2]))
        for i in range(3):
            p1[i].append(pos1[i])
            p2[i].append(pos2[i])
            p3[i].append(pos3[i])
        s1.acceleration(s2, s3)
        s2.acceleration(s1, s3)
        s3.acceleration(s1, s2)
        s1.set_position()
        s2.set_position()
        s3.set_position()
        s1.set_velocity()
        s2.set_velocity()
        s3.set_velocity()
        MovingStar.total_T += MovingStar.delta_t

    fig = pl.figure()
    ax = Axes3D(fig)
    ax.plot3D(p1[0], p1[1], p1[2], c='r')
    ax.plot3D(p2[0], p2[1], p2[2], c='b')
    ax.plot3D(p3[0], p3[1], p3[2], c='y')
    plt.show()


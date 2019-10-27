import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos


def checkPareto(index, allDots):
    for i, line in enumerate(allDots):
        if i != index and np.all(allDots[index, :] <= line):
            return False
    return True


if __name__ == "__main__":

    # ВХОДНЫЕ ДАННЫЕ
    dotsCount = 10
    dimension = 3
    const = 10
    dots = np.trunc(np.random.rand(dotsCount, dimension) * const)

    # НАХОЖДЕНИЕ ТОЧЕК ПАРЕТО
    pareto = []
    for index in range(dots.shape[0]):
        if checkPareto(index, dots):
            pareto.append(index)

    dots = np.append(dots, np.reshape(dots[:, 0], (dotsCount, 1)), axis=1)
    paretoLines = dots[pareto, :]
    alpha = 2 * np.pi * np.arange(dimension + 1, dtype=int) / dimension

    # ОТРИСОВКА
    _, ax = plt.subplots(1, 1, subplot_kw=dict(polar=True))
    ax.set_rmax(const)
    ax.set_thetagrids(np.arange(0, 360, 360 / dimension), labels=(np.arange(dimension) + 1))
    ax.grid(True)

    ax.set_title('PARETO FRONT')
    for line in paretoLines:
        ax.plot(alpha, line)

    plt.show()

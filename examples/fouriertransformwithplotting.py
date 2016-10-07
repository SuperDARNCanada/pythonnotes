import math
import cmath
from matplotlib import pyplot
import numpy as np

def dft(wave_list):
    """Compute a DFT from a list of wave samples"""
    num_samps = len(wave_list)

    ft_list = []
    for s in range(num_samps):
        ft = 0.0
        for i,samp in enumerate(wave_list):
            ft += samp * cmath.exp(-1j * 2 * cmath.pi * s * i / num_samps)
        ft_list.append(ft/num_samps)

    return ft_list


freq = 50
ampl = 1
num_samps = 360

wave_list = []
for n in range(num_samps):
    t = float(n) /num_samps * 2 * math.pi
    wave_samp = ampl * math.sin(freq * t)
    wave_list.append(wave_samp)

ft_list = dft(wave_list)

#computing the absolute values of dft
abs_ft_list = [abs(ft) for ft in ft_list]

x = np.arange(num_samps)

pyplot.subplot(2,1,1)
pyplot.plot(x,wave_list)

pyplot.subplot(2,1,2)
pyplot.plot(x,abs_ft_list)

pyplot.show()


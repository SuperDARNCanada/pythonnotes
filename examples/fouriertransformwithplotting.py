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

x_wave = np.arange(num_samps)

x_ft = np.arange(num_samps/2)
#x_ft = [x *(1/num_samps) for x in x_ft]

#Create figure for the first window
pyplot.figure()
pyplot.plot(x_wave,wave_list)
pyplot.title("Original Waveform")

#Create Figure for the second window
pyplot.figure()

#Slice the first half of the list for the single side FFT
single_side_ft = abs_ft_list[0:(num_samps/2)]
pyplot.plot(x_ft,single_side_ft)
pyplot.title("Single Side FFT Magnitude")

pyplot.show()


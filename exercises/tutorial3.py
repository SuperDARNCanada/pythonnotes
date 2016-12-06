from math import sin,cos,pi
from cmath import exp

num_samps = 100
f = 10 #Hz
ampl = 10

phase = [2 * pi * f * float(n)/num_samps for n in range(0,num_samps) ]
IQ_pairs = [complex(ampl * cos(p), ampl * sin(p)) for p in phase]

IQ_complex = [ampl * exp(1j * p) for p in phase]

print(IQ_pairs[0:10])
print(IQ_complex[0:10])

#IQ_pairs = [ampl * sin(2 * pi * f * float(n)/num_samps) for n in range(0,num_samps)]




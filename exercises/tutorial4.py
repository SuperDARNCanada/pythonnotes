import sys

speed_of_light = 3.0e8

class FOV(object):

    def __init__(self,number_beams, num_ranges, pulse_width, beam_width, pulse_seq, lat, lon,freq):
        self.number_beams = number_beams
        self.num_ranges = num_ranges
        self.pulse_seq = pulse_seq
        self.pulse_width = pulse_width
        self.beam_width = beam_width
        self.lat = lat
        self.lon = lon
        self.freq = freq

    def change_freq(self,freq):
        self.freq = freq

    def range_gate_distance_km(self,range_number):
        if range_number < 0 or range_number > self.num_ranges:
            print("Trouble in python land")
            raise ValueError("Problems!!!!",range_number)

        range_gate_distance_km = self.pulse_width * range_number * speed_of_light/1000.0

        return range_gate_distance_km






clyde_fov = FOV(16,75,300e-6,3.24,[0,4,6,7],59.4,-102.5,103e9)

clyde_fov.change_freq(12e6)

try:
    range_gate_distance_km = clyde_fov.range_gate_distance_km(-1)
except ValueError:
    range_gate_distance_km = clyde_fov.range_gate_distance_km(6)


print("Range gate distance(km) for range 5", range_gate_distance_km)


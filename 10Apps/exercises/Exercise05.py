#!/usr/bin/env python3
import Exercise03
import sys
if len(sys.argv) < 2:
    print("Not enough arguments")
    sys.exit()
input_filename = sys.argv[1]
output_filename = sys.argv[2]
with open(input_filename, 'r') as input_file:
    temps = input_file.read()
with open(output_filename, 'a+') as output_file:
    for temp in temps.split('\n'):
        if temp:
            output_file.write("%s \n" % str(Exercise03.CelsiusToFahrenheit(float(temp))))


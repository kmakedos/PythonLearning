#!/usr/bin/env python3
import sys
def CelsiusToFahrenheit(Cels):
    return  Cels * 9 / 5 + 32 if Cels > -273.15 else 0

if __name__ == "__main__":
    print(CelsiusToFahrenheit(float(sys.argv[1])))


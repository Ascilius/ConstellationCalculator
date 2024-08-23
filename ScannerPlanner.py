from math import *

VERSION = "1.0"

# planetary body radii (m)
RADII = {'Moho': 250000, 'Kerbin': 600000, 'Mun': 200000, 'Minmus': 60000, 'Eve': 700000}

print('Scanner Planner\nv{}\n'.format(VERSION))

# getting inputs
while True:
    body = input('Parent Body: ')
    if body in RADII:
        break
    else:
        print('Invalid input, please try again.')
r = RADII[body]
fov = int(input('KerbNet FOV (deg): ')) / 180 * pi
buf = float(input('Buffer: 1/'))
if buf != 0.0:
	buf = r  * (1.0/buf)

# confirming
print('\nSelected Body:\t{}\nRadius:\t\t{} m\nScanner FOV:\t{} rad\nBuffer:\t\t{} m\n'.format(body, r, round(fov, 3), buf))

# caculating
print('Calculating...')
x = (r+buf) / sin(fov)
alt = round(x - r)

# results
print('\nTarget Alt.:\t{} m'.format(alt))
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:19:35 2022

@author: jason

Constellation Calculator
"""

import math

VERSION = "1.3"
'''
Versions
v1.3
 - Improved math
 - Added more helpful text 
v1.2
 - Added input checkers
    - Ask for inputs again if invalid
 - Added recalculator in case first calculation results in negative alt
v1.1
 - Added synch and semi-synch modes
 - (wiki and calculated numbers are different???)
v1.0
 - Input parent planet, number of satellites, and
   target alt or period to calculate the target
   transfer peri or apo to create a cool-looking
   satellite constellation network
'''

# Gravitational Constant
G = 6.67430e-11 # N * m^2 * kg^-2

# Planetary Bodies
Moho = {'radius': 250000, 'mass': 2.5263314e21, 'sid_period': 1210000.0, 'min_alt': 10000}
Kerbin = {'radius': 600000, 'mass': 5.2915158e22, 'sid_period': 21549.425, 'min_alt': 100000} # m, kg, s, m
Mun = {'radius': 200000, 'mass': 9.7599066e20, 'sid_period': 138984.38, 'min_alt': 25000}
Minmus = {'radius': 60000, 'mass': 2.6457580e19, 'sid_period': 40400.0, 'min_alt': 10000}
Eve = {'radius': 700000, 'mass': 1.2243980e23, 'sid_period': 80500.0, 'min_alt': 100000}
Bodies = {'Moho': Moho, 'Kerbin': Kerbin, 'Mun': Mun, 'Minmus': Minmus, 'Eve': Eve}

print('Constellation Calculator')
print('v{}\n'.format(VERSION))

# getting inputs
while True:
    body = input('Parent Body: ')
    if body in Bodies:
        break
    else:
        print('Invalid input, please try again.\n')
parent_body = Bodies[body]
radius = parent_body['radius']
mass = parent_body['mass']
sid_period = parent_body['sid_period']
min_alt = parent_body['min_alt']
print(f'{body} selected:')
print(f'Radius:\t\t\t{radius} m')
print(f'Mass:\t\t\t{mass} kg')
print(f'Siderial Period:\t{sid_period} s')
print(f'Min. Alt.:\t\t{min_alt} m\n')

while True:
    num_sats = int(input('Number of Satellites: '))
    if num_sats > 1:
        break
    else:
        print('Invalid input, only >1 satellites are allowed.\n')
print(num_sats, 'satellites selected.\n')

allowed_modes = range(1, 5)
while True:
    # selecting mode
    print('1 - Target Altitude, 2 - Target Period, 3 - Synchronous, 4 - Semi-Synchronous')
    mode = int(input('Calculation Mode: '))
    if mode in allowed_modes:
        break
    else:
        print('Invalid input, only modes {}-{} allowed.\n'.format(allowed_modes[0], allowed_modes[-1]))
print('Mode', mode, 'selected.\n')

# from target alt
if mode == 1:
    target_alt = int(input('Target Altitude: '))
    print('Target altitude of', target_alt, 'm.\n')
    
    target_period = 2 * math.pi * ((target_alt + radius)**3 / (G * mass))**0.5

else:
    # from target period
    if mode == 2:
        target_period = float(input('Target Period: '))
        print('Target period of', target_period, 's.\n')
        
    # from siderial rotational period
    elif mode == 3:
        target_period = parent_body['sid_period']
        
    # semi-synchronous
    elif mode == 4:
        target_period = parent_body['sid_period'] / 2
        
    target_alt = ((G * mass * target_period**2) / (4 * math.pi**2))**(1.0 / 3.0) - radius

# calculating
print('Calculating...\n')
transfer_period = target_period * ((num_sats - 1) / num_sats)
transfer_sma = ((G * mass * transfer_period**2) / (4 * math.pi**2))**(1.0 / 3.0)
transfer_peri = transfer_sma * 2 - target_alt - radius * 2
print(f'Target Altitude:\t{round(target_alt)} m')
print(f'Transfer Periapsis:\t{round(transfer_peri)} m')

# recalculating
if transfer_peri <= min_alt:
    print('\nRecalculating...\n')
    transfer_period = target_period * ((num_sats + 1) / num_sats)
    transfer_sma = ((G * mass * transfer_period**2) / (4 * math.pi**2))**(1.0 / 3.0)
    transfer_alt = transfer_sma * 2 - target_alt - radius * 2
    print(f'Target Altitude:\t{round(target_alt)} m')
    print(f'Transfer Periapsis:\t{round(transfer_peri)} m')
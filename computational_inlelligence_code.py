# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:35:54 2024

@author: 
    Chen Wei Lun 19112697
    Chong Yu Cheng 15079395 
    Ch'ng Khye Ahn 15085111
    Yim Soon Keat 13045026
"""

import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
Membership Initialization

Occupancy measured in percentage
Natural Lighting measured in Lux unit
//https://www.electricalcounter.co.uk/lux-levels-chart
//https://blog.endaq.com/how-light-sensors-work#:~:text=called%20the%20candela.-,The%20Candela,a%20new%20unit:%20the%20lumen.

Temperature measured in celcius

Artifical Lighting also measured in Lux
Aircon also measured in celcius

'''
occupancy = ctrl.Antecedent(np.arange(0, 100, 0.1), 'occupancy')
natural_lighting = ctrl.Antecedent(np.arange(0, 1000, 0.1), 'natural_lighting')
temperature = ctrl.Antecedent(np.arange(0, 40, 0.1), 'temperature')
##weather = ctrl.Antecedent(np.arange(0, 100, 0.1), 'weather')

artificial_lighting = ctrl.Consequent(np.arange(0, 1000, 0.1), 'artificial_lighting')
aircon = ctrl.Consequent(np.arange(0, 100, 0.1), 'aircon')

##Antecedent
'''
Occupancy Level Antecedent
'''
occupancy['None'] = mf.trimf(occupancy.universe, [0, 0, 0])
occupancy['low'] = mf.trimf(occupancy.universe, [1, 10, 20])
occupancy['medium'] = mf.trimf(occupancy.universe, [15, 40, 70])
occupancy['high'] = mf.trimf(occupancy.universe, [60, 85, 100])
'''
Natural Lighting Antecedent
'''
natural_lighting['low'] = mf.trimf(natural_lighting.universe, [0, 35, 100])
natural_lighting['moderate'] = mf.trimf(natural_lighting.universe, [75, 300, 500])
natural_lighting['high'] = mf.trimf(natural_lighting.universe, [400, 750, 1000])

'''
Outside Temperature Antecedent
'''
temperature['low'] = mf.trimf(temperature.universe, [0, 18, 24])
temperature['comfortable'] = mf.trimf(temperature.universe, [20, 28, 30])
temperature['high'] = mf.trimf(temperature.universe, [25, 35, 40])

##Consequent

'''
Artificial Lighting Consequent
'''
artificial_lighting['off'] = mf.trimf(artificial_lighting.universe, [0, 0, 0])
artificial_lighting['low'] = mf.trimf(artificial_lighting.universe, [1, 120, 250])
artificial_lighting['moderate'] = mf.trimf(artificial_lighting.universe, [200, 500, 700])
artificial_lighting['high'] = mf.trimf(artificial_lighting.universe, [650, 750, 1000])

'''
Aircon Consequent (lower means cooler aircon)
'''
aircon['off'] = mf.trimf(aircon.universe, [0, 0, 0])
aircon['low'] = mf.trimf(aircon.universe, [1, 25, 30])
aircon['moderate'] = mf.trimf(aircon.universe, [30, 55, 70])
aircon['high'] = mf.trimf(aircon.universe, [65, 80, 100])


## Fuzzy Set Rules
'''
Intializing Rules
'''
rule1 = ctrl.Rule(occupancy['None'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule2 = ctrl.Rule(occupancy['None'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['off'], aircon['off']))
rule3 = ctrl.Rule(occupancy['None'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['off'], aircon['off']))
rule4 = ctrl.Rule(occupancy['None'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule5 = ctrl.Rule(occupancy['None'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['off'], aircon['off']))
rule6 = ctrl.Rule(occupancy['None'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['off'], aircon['off']))
rule7 = ctrl.Rule(occupancy['None'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule8 = ctrl.Rule(occupancy['None'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['off'], aircon['off']))
rule9 = ctrl.Rule(occupancy['None'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['off'], aircon['off']))

rule10 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['low'], aircon['off']))
rule11 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['low'], aircon['off']))
rule12 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['low'], aircon['moderate']))
rule13 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule14 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['off'], aircon['off']))
rule15 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['off'], aircon['moderate']))
rule16 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule17 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['off'], aircon['off']))
rule18 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['off'], aircon['moderate']))

rule19 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['moderate'], aircon['off']))
rule20 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['moderate'], aircon['low']))
rule21 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['moderate'], aircon['moderate']))
rule22 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['low'], aircon['off']))
rule23 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['low'], aircon['low']))
rule24 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['low'], aircon['moderate']))
rule25 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['off'], aircon['off']))
rule26 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['off'], aircon['low']))
rule27 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['off'], aircon['moderate']))

rule28 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['high'], aircon['low']))
rule29 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['high'], aircon['moderate']))
rule30 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['high'], aircon['high']))
rule31 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['moderate'], aircon['low']))
rule32 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['moderate'], aircon['moderate']))
rule33 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['moderate'], aircon['high']))
rule34 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['low'], aircon['low']))
rule35 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['low'], aircon['moderate']))
rule36 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['low'], aircon['high']))



'''
Combining Rules
'''
rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36]
'''
Training Fuzzy Model
'''
train_ctrl = ctrl.ControlSystem(rules=rules)
train = ctrl.ControlSystemSimulation(control_system=train_ctrl)

train.input['occupancy'] = 0
train.input['natural_lighting'] = 100
train.input['temperature'] = 24

train.compute()

# print the output values
print(train.output)

# to extract one of the outputs
print(train.output['aircon'])

'''
Printing Output
'''
artificial_lighting.view(sim=train)
aircon.view(sim=train)

'''
Maybe Not Needed

x, y = np.meshgrid(np.linspace(occupancy.universe.min(), occupancy.universe.max(), 100),
                   np.linspace(natural_lighting.universe.min(), natural_lighting.universe.max(), 100) )
z_artificial_lighting = np.zeros_like(x, dtype=float)
z_aircon = np.zeros_like(x, dtype=float)



for i,r in enumerate(x):
  for j,c in enumerate(r):
    train.input['occupancy'] = x[i,j]
    train.input['natural_lighting'] = y[i,j]
    try:
      z_artificial_lighting[i,j] = train.output['artificial_lighting']
      z_aircon[i,j] = train.output['aircon']
      train.compute()
    except:
      z_artificial_lighting[i,j] = float('inf')
      z_aircon[i,j] = float('inf')
     
      

##https://www.w3schools.com/python/matplotlib_labels.asp


def plot3d(x,y,z):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

  ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
  ax.contourf(x, y, z, zdir='x', offset=x.max()*1.5, cmap='viridis', alpha=0.5)
  ax.contourf(x, y, z, zdir='y', offset=y.max()*1.5, cmap='viridis', alpha=0.5)

  ax.view_init(30, 200)

plot3d(x, y, z_artificial_lighting)
plot3d(x, y, z_aircon)



'''


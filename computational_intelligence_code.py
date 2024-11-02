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
natural_lighting = ctrl.Antecedent(np.arange(0, 100, 0.1), 'natural')
temperature = ctrl.Antecedent(np.arange(0, 100, 0.1), 'temperature')
##weather = ctrl.Antecedent(np.arange(0, 100, 0.1), 'weather')

artificial_lighting = ctrl.Consequent(np.arange(0, 100, 0.1), 'artificial')
aircon = ctrl.Consequent(np.arange(0, 100, 0.1), 'aircon')

##Antecedent
'''
Occupancy Level Antecedent
'''
occupancy['None'] = mf.trimf(occupancy.universe, [0, 0, 0])
occupancy['low'] = mf.trimf(occupancy.universe, [0, 25, 35])
occupancy['medium'] = mf.trimf(occupancy.universe, [30, 50, 65])
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
temperature['high'] = mf.trimf(temperature.universe, [25, 40, 100])

##Consequent

'''git
Artificial Lighting Consequent
'''
artificial_lighting['off'] = mf.trimf(artificial_lighting.universe, [0, 0, 0])
artificial_lighting['low'] = mf.trimf(artificial_lighting.universe, [0, 120, 250])
artificial_lighting['moderate'] = mf.trimf(artificial_lighting.universe, [200, 500, 700])
artificial_lighting['high'] = mf.trimf(artificial_lighting.universe, [650, 750, 1000])

'''
Aircon Consequent (lower means cooler aircon)
'''
aircon['off'] = mf.trimf(aircon.universe, [0, 0, 0])
aircon['low'] = mf.trimf(aircon.universe, [16, 18, 20])
aircon['moderate'] = mf.trimf(aircon.universe, [18, 22, 24])
aircon['high'] = mf.trimf(aircon.universe, [20, 25, 30])


## Fuzzy Set Rules
'''
New Intializing Rules Just Dropped
'''
## occupancy + lighting => artifical lighting
rule1 = ctrl.Rule(occupancy['None'] & natural_lighting['low'], (artificial_lighting['off']))
rule2 = ctrl.Rule(occupancy['None'] & natural_lighting['moderate'], (artificial_lighting['off']))
rule3 = ctrl.Rule(occupancy['None'] & natural_lighting['high'], (artificial_lighting['off']))

rule4 = ctrl.Rule(occupancy['low'] & natural_lighting['low'], (artificial_lighting['low']))
rule5 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'], (artificial_lighting['off']))
rule6 = ctrl.Rule(occupancy['low'] & natural_lighting['high'], (artificial_lighting['off']))

rule7 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'], (artificial_lighting['moderate']))
rule8 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'], (artificial_lighting['low']))
rule9 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'], (artificial_lighting['low']))

rule10 = ctrl.Rule(occupancy['high'] & natural_lighting['low'], (artificial_lighting['high']))
rule11 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'], (artificial_lighting['moderate']))
rule12 = ctrl.Rule(occupancy['high'] & natural_lighting['high'], (artificial_lighting['low']))

## occupancy + temp => ac settings
rule13 = ctrl.Rule(occupancy['None'] & temperature['low'], (aircon['off']))
rule14 = ctrl.Rule(occupancy['None'] & temperature['comfortable'], (aircon['off']))
rule15 = ctrl.Rule(occupancy['None'] & temperature['high'], (aircon['off']))

rule16 = ctrl.Rule(occupancy['low'] & temperature['low'], (aircon['off']))
rule17 = ctrl.Rule(occupancy['low'] & temperature['comfortable'], (aircon['off']))
rule18 = ctrl.Rule(occupancy['low'] & temperature['high'], (aircon['moderate']))

rule19 = ctrl.Rule(occupancy['medium'] & temperature['low'], (aircon['moderate']))
rule20 = ctrl.Rule(occupancy['medium'] & temperature['comfortable'], (aircon['moderate']))
rule21 = ctrl.Rule(occupancy['medium'] & temperature['high'], (aircon['low']))

rule22 = ctrl.Rule(occupancy['high'] & temperature['low'], (aircon['high']))
rule23= ctrl.Rule(occupancy['high'] & temperature['comfortable'], (aircon['moderate']))
rule24 = ctrl.Rule(occupancy['high'] & temperature['high'], (aircon['low']))



'''
Combining Rules
'''
rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24]
'''
Training Fuzzy Model
'''
train_ctrl = ctrl.ControlSystem(rules=rules)
train = ctrl.ControlSystemSimulation(control_system=train_ctrl)


# define the values for the inputs
train.input['occupancy'] = 0
train.input['natural'] = 2000
train.input['temperature'] = 2000



# compute the outputs
train.compute()

# print the output values
print(train.output)

# to extract one of the outputs
print(train.output['artificial'])
print(train.output['aircon'])




'''
Printing Output
'''
artificial_lighting.view(sim=train)
aircon.view(sim=train)


'''
View the control / Output space
'''
x, y, z = np.meshgrid(np.linspace(occupancy.universe.min(), occupancy.universe.max(), 100),
                   np.linspace(natural_lighting.universe.min(), natural_lighting.universe.max(), 100)
                   , np.linspace(temperature.universe.min(), temperature.universe.max(), 100) )
z_artificial_lighting = np.zeros_like(x, dtype=float)
z_aircon = np.zeros_like(x, dtype=float)

'''
Loopy Loop
'''
for i,r in enumerate(x):
  for j,c in enumerate(r):
    train.input['occupancy'] = x[i,j]
    train.input['natural'] = y[i,j]
    train.input['temperature'] = z[i,j]
    try:
      z_artificial_lighting[i,j] = train.output['artificial']
      z_aircon[i,j] = train.output['aircon']
      train.compute()
    except:
      z_artificial_lighting[i,j] = float('inf')
      z_aircon[i,j] = float('inf')

'''
Graph in the corner, plotting world domination
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

##https://www.w3schools.com/python/matplotlib_labels.asp





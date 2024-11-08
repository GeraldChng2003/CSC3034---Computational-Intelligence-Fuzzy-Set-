# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:08:37 2024

@author: 
    Chen Wei Lun 19112697
    Chong Yu Cheng 15079395 
    Ch'ng Khye Ahn 15085111
    Yim Soon Keat 13045026
"""

import matplotlib.pyplot as plt
import numpy as np
from skfuzzy import control as ctrl
from skfuzzy import membership as mf


# Construct the Antedecent for inputs and Consequent for the outputs while defining the range as well
occupancy = ctrl.Antecedent(np.arange(0, 30, 0.1), 'occupancy')
natural_lighting = ctrl.Antecedent(np.arange(0, 1000, 0.1), 'natural_lighting')
temperature = ctrl.Antecedent(np.arange(0, 40, 0.1), 'temperature')

artificial_lighting = ctrl.Consequent(np.arange(0, 1000, 0.1), 'artificial_lighting')
aircon = ctrl.Consequent(np.arange(0, 100, 0.1), 'aircon')

# Define the membership functions for the inputs and ouputs
occupancy['very low'] = mf.trimf(occupancy.universe, [0, 0, 3])
occupancy['low'] = mf.trimf(occupancy.universe, [2, 5, 10])
occupancy['medium'] = mf.trimf(occupancy.universe, [7, 12, 20])
occupancy['high'] = mf.trimf(occupancy.universe, [16, 25, 30])

natural_lighting['low'] = mf.trimf(natural_lighting.universe, [0, 35, 300])
natural_lighting['moderate'] = mf.trimf(natural_lighting.universe, [250, 500, 650])
natural_lighting['high'] = mf.trimf(natural_lighting.universe, [600, 750, 1000])

temperature['low'] = mf.trimf(temperature.universe, [0, 18, 24])
temperature['comfortable'] = mf.trimf(temperature.universe, [20, 28, 30])
temperature['high'] = mf.trimf(temperature.universe, [25, 35, 40])

artificial_lighting['very low'] = mf.trimf(artificial_lighting.universe, [0, 50, 200])
artificial_lighting['low'] = mf.trimf(artificial_lighting.universe, [150, 250, 400])
artificial_lighting['moderate'] = mf.trimf(artificial_lighting.universe, [350, 500, 750])
artificial_lighting['high'] = mf.trimf(artificial_lighting.universe, [650, 750, 850])
artificial_lighting['very high'] = mf.trimf(artificial_lighting.universe, [750, 850, 1000])

aircon['very low'] = mf.trimf(aircon.universe, [0, 5, 10])
aircon['low'] = mf.trimf(aircon.universe, [1, 25, 40])
aircon['moderate'] = mf.trimf(aircon.universe, [35, 55, 70])
aircon['high'] = mf.trimf(aircon.universe, [65, 80, 100])

# The rules for the fuzzy system
rule1 = ctrl.Rule(occupancy['very low'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['very low'], aircon['very low']))
rule2 = ctrl.Rule(occupancy['very low'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['very low'], aircon['very low']))
rule3 = ctrl.Rule(occupancy['very low'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['very low'], aircon['very low']))
rule4 = ctrl.Rule(occupancy['very low'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['very low'], aircon['very low']))
rule5 = ctrl.Rule(occupancy['very low'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['very low'], aircon['very low']))
rule6 = ctrl.Rule(occupancy['very low'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['very low'], aircon['very low']))
rule7 = ctrl.Rule(occupancy['very low'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['very low'], aircon['very low']))
rule8 = ctrl.Rule(occupancy['very low'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['very low'], aircon['very low']))
rule9 = ctrl.Rule(occupancy['very low'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['very low'], aircon['very low']))

rule10 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['moderate'], aircon['very low']))
rule11 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['moderate'], aircon['very low']))
rule12 = ctrl.Rule(occupancy['low'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['moderate'], aircon['moderate']))
rule13 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['low'], aircon['very low']))
rule14 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['low'], aircon['very low']))
rule15 = ctrl.Rule(occupancy['low'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['low'], aircon['moderate']))
rule16 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['very low'], aircon['very low']))
rule17 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['very low'], aircon['very low']))
rule18 = ctrl.Rule(occupancy['low'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['very low'], aircon['moderate']))

rule19 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['high'], aircon['very low']))
rule20 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['high'], aircon['low']))
rule21 = ctrl.Rule(occupancy['medium'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['high'], aircon['moderate']))
rule22 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['moderate'], aircon['very low']))
rule23 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['moderate'], aircon['low']))
rule24 = ctrl.Rule(occupancy['medium'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['moderate'], aircon['moderate']))
rule25 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['low'], aircon['very low']))
rule26 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['low'], aircon['low']))
rule27 = ctrl.Rule(occupancy['medium'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['low'], aircon['moderate']))

rule28 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['low'], (artificial_lighting['very high'], aircon['low']))
rule29 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['comfortable'], (artificial_lighting['very high'], aircon['moderate']))
rule30 = ctrl.Rule(occupancy['high'] & natural_lighting['low'] & temperature['high'], (artificial_lighting['very high'], aircon['high']))
rule31 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['low'], (artificial_lighting['high'], aircon['low']))
rule32 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['comfortable'], (artificial_lighting['high'], aircon['moderate']))
rule33 = ctrl.Rule(occupancy['high'] & natural_lighting['moderate'] & temperature['high'], (artificial_lighting['high'], aircon['high']))
rule34 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['low'], (artificial_lighting['moderate'], aircon['low']))
rule35 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['comfortable'], (artificial_lighting['moderate'], aircon['moderate']))
rule36 = ctrl.Rule(occupancy['high'] & natural_lighting['high'] & temperature['high'], (artificial_lighting['moderate'], aircon['high']))

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36]

train_ctrl = ctrl.ControlSystem(rules=rules)
train = ctrl.ControlSystemSimulation(control_system=train_ctrl)

def input_occupancy():
    print("=================================================================================")
    print("> Please enter the input for occupancy (0 - 30)")
    print("=================================================================================")
    occupancy_input = int(input())
    if occupancy_input < 0 or occupancy_input > 30: # invalid input
        print("[x] ERROR: Please enter a number between 0 and 30")
        print("")
        return input_occupancy()
    else:
        print("...")
        print("")
        return occupancy_input

def input_natural_lighting():
    print("=================================================================================")
    print("> Please enter the input for natural lighting (0 - 1000)")
    print("=================================================================================")
    natural_lighting_input = int(input())
    if natural_lighting_input < 0 or natural_lighting_input > 1000:
        print("[x] ERROR: Please enter a number between 0 and 1000")
        print("")
        return input_natural_lighting()
    else:
        print("...")
        print("")
        return natural_lighting_input

def input_temperature():
    print("=================================================================================")
    print("> Please enter the input for temperature (0 - 40)")
    print("=================================================================================")
    temperature_input = int(input())
    if temperature_input < 0 or temperature_input > 40:
        print("[x] ERROR: Please enter a number between 0 and 40")
        print("")
        return input_temperature()
    else:
        print("...")
        print("")
        return temperature_input

def beginning_input():
    print("---------------------------------------------------------------------------------")
    print("> Welcome to Energy Mangement Fuzzy System!")
    print("> This system aims to help you optimize your aircon fanspeed and lighting settings!")
    print("> This system to built in accordance to SDG 7,11 and 12.")
    print("---------------------------------------------------------------------------------")
    train.input['occupancy'] = input_occupancy()
    train.input['natural_lighting'] = input_natural_lighting()
    train.input['temperature'] = input_temperature()
    train.compute()
    print("=================================================================================")
    print("")
    print("> Results:")
    print("> Recommended aircon fanspeed: " + str(int(train.output['aircon'])) + "%")
    print("> Recommended lighting level: " + str(int(train.output['artificial_lighting'])) + " lumen")
    print("")
    print("=================================================================================")
def program():
    beginning_input()
    print("Would you like to enter another input?")
    print("---------------------------------------------------------------------------------")
    print("Enter 'yes' to enter new inputs")
    print("Enter 'no' to quit")
    print("Enter 'graph' to generate membership graph")
    print("---------------------------------------------------------------------------------")
    choice = input()
    if choice == "graph":
        artificial_lighting.view(sim=train)
        aircon.view(sim=train)
        plt.show()
        print("---------------------------------------------------------------------------------")
        print("Thank you for using our program")
        print("---------------------------------------------------------------------------------")
    if choice == "yes":
        program()
    if choice == "no":
        print("---------------------------------------------------------------------------------")
        print("Thank you for using our program")
        print("---------------------------------------------------------------------------------")

program()





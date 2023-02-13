# myBots

In this branch I created a program to generate random 3D creatures. Creatures consist of a randomly sized main body cube. Randomly sized limbs are then randomly attached to any side of the body. The creature can have 2-4 limbs. Each limb consists of a motorized joint. Each joint acts as a ball joint. The motors are controlled by touch sensors throughout the creature. Body parts with touch sensors are green. Body parts without sensors are blue. The touch sensors are connected to each motor in the body to create synapses. Each synapse is given a random weight. This leads to random motion in the motors when the touch sensors are activated.

To run this program, simply click the run button in the "button.py" file.

This takes inspiration from https://www.reddit.com/r/ludobots/

This program is built using pyrosim.

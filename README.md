In this branch I created a program to generate and evolve random 3D creatures. Creatures consist of a randomly sized main body cube. Randomly sized limbs are then randomly attached to any side of the body. Limbs can only attach to the main body cube and not to each other. The creature can have 4-6 limbs. Each limb consists of a motorized joint. Each joint acts as a ball joint. The motors are controlled by touch sensors throughout the creature. Body parts with touch sensors are green. Body parts without sensors are blue. The touch sensors are connected to each motor in the body to create synapses. Each synapse is given a random weight. This leads to random motion in the motors when the touch sensors are activated.

Each creature can be evolved for a specified number of generations. The current number of generations is 500. The evolve method removes one random limb on the creature and replaces it with a new random limb. 

To run this program, simply click the run button in the "button.py" file.

![Untitled design](https://user-images.githubusercontent.com/110938963/220187874-6f3d3b2f-1173-4c84-890a-fc218051418f.png)
(An example morphology for the creature. Limbs can attach on any side except for the bottom.)

Joint locations are determined by generating random coordinates anywhere on the body.
Limbs are then placed at each joint location. Limb sizes are determined by generating random numbers.

This project is built on top of code from ludobots. https://www.reddit.com/r/ludobots/

This program is built using pyrosim. https://github.com/jbongard/pyrosim

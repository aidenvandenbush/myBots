This is a program created for the Northwestern University class COMP_SCI 396: Artificial Life

This program creates random moving creatures through evolution. Creatures consist of a randomly sized main body cube. Randomly sized limbs are then attached to any side of the body. Limbs can only attach to the main body cube and not to each other. The creature can have 4-6 limbs. Each limb consists of a motorized joint, and each joint acts as a ball joint. The motors are controlled by touch sensors throughout the creature. Body parts with touch sensors are green. Body parts without sensors are blue. The touch sensors are connected to each motor in the body to create synapses. Each synapse is given a random weight. This leads to random motion in the motors when the touch sensors are activated.

I set out to test whether different methods of evolution would lead to higher levels of fitness. Fitness is determined by how far the creature moves a block that starts near it. For the selection process, each parent was compared to their evolved child, and the creature that moved the block further was kept and evolved again.

The first evolution method I tested removed one limb at random from the creature and replaced it with a new random limb. New limbs can be placed anywhere on the body cube just like the original limbs.

The other method I used to evolve the creatures was the same for the first 125 generations, replacing a random limb. After 125 generations, the body plan was kept constant. Instead, the brain was evolved by changing the weight of one synapse every generation.

I tested both methods 5 times each, using a population size of 50 over 250 generations. This led to a total of 125,000 simulations.


To run this program, simply click the run button in the "button.py" file.

2 Minute Summary: https://youtu.be/xTxmNU9HIq0

<p align="center">
  <img src=https://user-images.githubusercontent.com/110938963/224574336-ab672e52-78bb-46da-a634-d1fd572c9874.gif>
</p>

![Ludobots (4)](https://user-images.githubusercontent.com/110938963/224574637-0bc439b6-5efb-481c-a4c5-054323d61b0d.jpg)

![Ludobots (5)](https://user-images.githubusercontent.com/110938963/224574644-7784b5af-5aae-4425-933b-2cdb722bee3f.jpg)

![Ludobots (6)](https://user-images.githubusercontent.com/110938963/224574655-6bdfb508-bc07-4ace-9d1f-567d8cbe1529.jpg)

![Ludobots (7)](https://user-images.githubusercontent.com/110938963/224574662-51fe2a52-8031-43c9-a149-ad3ff3b77372.jpg)



This project is built on top of code from ludobots. https://www.reddit.com/r/ludobots/

This program is built using pyrosim. https://github.com/jbongard/pyrosim

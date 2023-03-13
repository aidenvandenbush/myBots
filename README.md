This is a program created for the Northwestern University class COMP_SCI 396: Artificial Life

This program creates random moving creatures through evolution. Creatures consist of a randomly sized main body cube. Randomly sized limbs are then attached to any side of the body. Limbs can only attach to the main body cube and not to each other. The creature can have 4-6 limbs. Each limb consists of a motorized joint, and each joint acts as a ball joint. The motors are controlled by touch sensors throughout the creature. Body parts with touch sensors are green. Body parts without sensors are blue. The touch sensors are connected to each motor in the body to create synapses. Each synapse is given a random weight. This leads to random motion in the motors when the touch sensors are activated.

I set out to test whether different methods of evolution would lead to higher levels of fitness. Fitness is determined by how far the creature moves a block that starts near it. For the selection process, each parent was compared to their evolved child, and the creature that moved the block further was kept and evolved again.

The first evolution method I tested removed one limb at random from the creature and replaced it with a new random limb. New limbs can be placed anywhere on the body cube just like the original limbs.

The other method I used to evolve the creatures was the same as the first method for the first 125 generations, replacing a random limb. After 125 generations, the body plan was kept constant. Instead, the brain was evolved by changing the weight of one synapse every generation.

I tested both methods 5 times each, using a population size of 50 over 250 generations. This led to a total of 125,000 simulations. The only variable changed between the two methods was the mutation method that was used. This allowed me to test which mutation method led to a higher fitness.


To run this program, simply click the run button in the "button.py" file.

2 Minute Summary: https://youtu.be/xTxmNU9HIq0

<p align="center">
  <img src=https://user-images.githubusercontent.com/110938963/224574336-ab672e52-78bb-46da-a634-d1fd572c9874.gif>
</p>

![Ludobots (4)](https://user-images.githubusercontent.com/110938963/224574637-0bc439b6-5efb-481c-a4c5-054323d61b0d.jpg)

![Ludobots (5)](https://user-images.githubusercontent.com/110938963/224574644-7784b5af-5aae-4425-933b-2cdb722bee3f.jpg)

![Ludobots (6)](https://user-images.githubusercontent.com/110938963/224574655-6bdfb508-bc07-4ace-9d1f-567d8cbe1529.jpg)

![Ludobots (7)](https://user-images.githubusercontent.com/110938963/224574662-51fe2a52-8031-43c9-a149-ad3ff3b77372.jpg)


The second method of evolution that involved evolving the creature's brain after evolving the body did slighty better than the first method of only evolving the body.
The average fitness for the final creature of the second method was 1.958. The average fitness for the final creature of the first method was 1.811. Evolving the brain and not the body after generation 125 led to more increases in the maximum fitness of a population. Evolving the body only seemed to lead to a peak fitness between 1.5 and 2. Also, this ideal body plan was also normally found in the first 125 generations, with very little improvement being made afterward. By evolving the brain after this ideal body plan was found, we were able to fully optimize the creature.

![Fitness of Evolved Creatures](https://user-images.githubusercontent.com/110938963/224584903-0d1b81f6-f816-422e-ad9a-21c59da16f2e.png)

If I had more time, I would attempt to implement variations of the second evolution method. I would vary the generation at which I switch from evolving the body to evolving the brain. Switching to evolving the brain sooner, at around generation 50, could lead to better results. Doing the opposite and waiting until generation 200 to switch to evolution of the brain could also be effective.

This project is built on top of code from ludobots. https://www.reddit.com/r/ludobots/

This program is built using pyrosim. https://github.com/jbongard/pyrosim

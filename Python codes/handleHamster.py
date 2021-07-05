from roboid import *

hamster = Hamster()

def calc_speed(proximity):
    if proximity > 10:
        return (40 - proximity) * 4
    else:
        return 0

while True:

    left_speed = calc_speed(hamster.left_proximity())
    right_speed = calc_speed(hamster.right_proximity())
   
    hamster.wheels(left_speed, right_speed)

    wait(20)

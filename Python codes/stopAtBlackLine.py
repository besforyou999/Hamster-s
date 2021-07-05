from roboid import *

hamster = Hamster()

while hamster.left_floor() > 20 and hamster.right_floor() > 20:
    hamster.wheels(30)
    wait(20)

hamster.stop()

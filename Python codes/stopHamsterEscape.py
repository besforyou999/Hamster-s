from roboid import *

hamster = Hamster()

while True:
    if hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        hamster.wheels(30)
    else:
        hamster.wheels(-30, 30)
        wait(2000)

    wait(20)


from roboid import *

hamster = Hamster()

left = False

while True:
    key = Keyboard.read()
    if key == ' ':
        left = not left

    if left:
        hamster.wheels(0, 50)
    else:
        hamster.wheels(50, 0 )

    wait(20)

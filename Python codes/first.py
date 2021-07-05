from roboid import *

hamster = Hamster()


while True:
    key = Keyboard.read()
    if key:
        if key == Keyboard.UP:
            hamster.wheels(50)
        elif key == Keyboard.DOWN:
            hamster.wheels(-50)
        elif key == Keyboard.LEFT:
            hamster.wheels(-50, 50)
        elif key == Keyboard.RIGHT:
            hamster.wheels(50, -50)
        elif key == ' ':
            hamster.stop()
            
    wait(20)
  

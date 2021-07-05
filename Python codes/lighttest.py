from roboid import *

hamster = Hamster()

while True:
    if hamster.light() < 60:
        tune = hamster.light()
        hamster.buzzer(2100 - tune * 20)
    else:
        hamster.buzzer(0)
    wait(20)

    

from roboid import *

hamster = Hamster()

while True:
    key = Keyboard.read()
    if key:
        if key == 'a':
            hamster.note(Hamster.NOTE_C_4)
        elif key == 's':
            hamster.note(Hamster.NOTE_D_4)
        elif key == 'd':
            hamster.note(Hamster.NOTE_E_4)
        elif key == 'f':
            hamster.note(Hamster.NOTE_F_4)
        elif key == 'g':
            hamster.note(Hamster.NOTE_G_4)
        elif key == 'h':
            hamster.note(Hamster.NOTE_A_4)
        elif key == 'j':
            hamster.note(Hamster.NOTE_B_4)
        elif key == 'k':
            hamster.note(Hamster.NOTE_C_5)
        elif key == 'l':
            hamster.note(Hamster.NOTE_D_5)
        elif key == ';':
            hamster.note(Hamster.NOTE_E_5)
        elif key == "'":
            hamster.note(Hamster.NOTE_F_5)
        elif key == ' ':
            hamster.note(0)

    wait(20)

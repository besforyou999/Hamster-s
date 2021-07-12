from roboid import *
import roboidai as ai

hamster = HamsterS()

cam = ai.Camera('ip0', flip ='h')

detector = ai.FaceMesh()
detector.load_model()

id = []

while True:
    image = cam.read()
    if detector.detect(image):
        image = detector.draw_result(image)
        id = detector.get_xy('nose')
        print(id)
    cam.show(image)

    if cam.check_key() == 'esc': break



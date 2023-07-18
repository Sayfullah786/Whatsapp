from pynput.mouse import Controller,Button

class Mouse:
    def __init__(self):
        self.controller = Controller()


    def click(self):
        self.controller.position = (731,967)
        self.controller.click(Button.left, 1)

        #871 , 970
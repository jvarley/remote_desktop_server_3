from pymouse import PyMouse

class MouseController:
    def __init__(self):
        self.mouse = PyMouse()

    def set_mouse_position(self,x,y):
        self.mouse.move(x,y)
    
    def get_mouse_position(self):
        return self.mouse.position()

    def get_screen_size(self):
        return self.mouse.screen_size()

    #x,y, button possible values are 1: left, 2: middle, 3: right
    def click_at_location(self,x,y,button_id):
        self.mouse.click(x,y,button_id)

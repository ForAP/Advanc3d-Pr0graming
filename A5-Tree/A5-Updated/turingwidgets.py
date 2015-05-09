# File name: turingwidgets.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty
from kivy.graphics import Line
from state import State

class DraggableWidget(RelativeLayout):
    stateName = NumericProperty(0)

    def __init__(self,  **kwargs):
        self.selected = None
        self.touched = False
        super(DraggableWidget, self).__init__(**kwargs)

    def set_state(self):
        self.stateName = self.parent.general_options.nameCounter - 1
        print self.stateName

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.touched = True
            self.select()
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def select(self):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0,0,self.width,self.height), dash_offset=2)

    def on_touch_move(self, touch):
        (x,y) = self.parent.to_parent(touch.x, touch.y)
        if self.selected and self.touched and self.parent.collide_point(x - self.width/2, y -self.height/2):
            go = self.parent.general_options
            go.translation=(touch.x-self.ix,touch.y-self.iy)
            return True
        return super(DraggableWidget, self).on_touch_move(touch)

    def translate(self, x, y):
        self.center_x = self.ix = self.ix + x
        self.center_y = self.iy = self.iy + y

    def on_touch_up(self, touch):
        self.touched = False
        if self.selected:
            if not self.parent.general_options.group_mode:
                self.unselect()
        return super(DraggableWidget, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None

class StickMan(DraggableWidget):
    r = NumericProperty(1)

    def change_r(self, change):
        self.r = change

    def goback(self):
        self.r = 1

    # def __init__(self, **kwargs):
    #     self.size= [50,50]
    #     self.pos = [100,50]
    #     self.r = 0
    #     super(StickMan, self).__init__(**kwargs)
    #
    # def on_touch_down(self, touch):
        # if self.collide_point(touch.x,touch.y):
        #     self.r = 100.0                       # <---- This does nothing!

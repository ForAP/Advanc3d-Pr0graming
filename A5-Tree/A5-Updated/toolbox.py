# File name: toolbox.py
import kivy
kivy.require('1.7.0')
import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from turingwidgets import StateRep, DraggableWidget
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Line, Bezier
from state import State

class ToolState(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolState, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        sm = StateRep(width=48, height=48)
        sm.center = (x,y)
        sm.opacity = 0.9
        state = State()
        print "\nThis is the state that you just created, will you name it?" + str(state)
        print type(ds.children)
        print "ds children is " + str(ds.children)
        print "ds children's length is " + str(len(ds.children))
        self.parent.general_options.add_state(state)
        ds.add_widget(sm)
        ds.children[0].set_state()

        #if len(ds.children) > 2:
        #    tool = ToolTransition()
        #    tool.draw(ds,ds.children[-1],ds.children[-2])


class ToolTransition(ToggleButton):
    #still to test and fix...
    def draw_transition(self, stateRepOne, stateRepTwo):
        posOfOne = stateRepOne.get_local
        postOfTwo = stateRepTwo.get_local
        #draw
        with self.canvas:
            d = 50
            #touch.ud["line"] = Line(points=(touch.x,touch.y))
            Line(points=(posOfOne[0], posOfOne[1], postOfTwo[0], postOfTwo[1]))

# File name: toolbox.py
import kivy
kivy.require('1.7.0')
import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from turingwidgets import StateRep, DraggableWidget, Transition1, Transition2
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Line, Bezier


class ToolState(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            print (x,y)
            self.draw(ds, x, y)
            return True
        return super(ToolState, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        sm = StateRep(width=48, height=48)
        sm.center = (x,y)
        sm.opacity = 1
        print type(ds.children)
        print "ds children is " + str(ds.children)
        print "ds children's length is " + str(len(ds.children))
        go = self.parent.general_options
        go.add_state()
        ds.add_widget(sm)
        ds.children[0].set_state(go.nameCounter - 1)

        #if len(ds.children) > 2:
        #    tool = ToolTransition()
        #    tool.draw(ds,ds.children[-1],ds.children[-2])


class ToolTransition(ToggleButton):
    #still to test and fix...
    def draw_transition(self, current_state, transInfo, transitionCounter):
        ds = self.parent.drawing_space
        go = self.parent.general_options
        print ds.children
        stateOneID = int(current_state) + transitionCounter + 1
        print stateOneID
        stateOne = ds.children[-(stateOneID)]
        # search for whether transition has already been created
        if (current_state, transInfo[2]) in go.transitions:
            key = go.transitions[(current_state, transInfo[2])]
        # searches through the drawingspace for the transition and updates the label
            for child in ds.children:
                if isinstance(child, Transition1) or isinstance(child, Transition2):
                    if child.key == key:
                        child.update_label(transInfo)
        # find what kind of transition is to be drawn
        if current_state == transInfo[2]:
            t = Transition1(stateOne,transInfo,go.keyNum)
            ds.add_widget(t)
            go.transitions.update({(current_state, transInfo[2]):go.keyNum})
            go.keyNum += 1
            go.transitionCounter += 1
        else:
            stateTwo = ds.children[-(int(transInfo[2])+transitionCounter+1)]
            t = Transition2(stateOne,stateTwo,transInfo,go.keyNum)
            ds.add_widget(t)
            go.transitions.update({(current_state, transInfo[2]):go.keyNum})
            go.keyNum += 1
            go.transitionCounter += 1

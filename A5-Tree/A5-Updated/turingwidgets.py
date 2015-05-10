# File name: turingwidgets.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
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
        ''' double tap to add transitions to a tm directly'''
        if touch.is_double_tap and self.collide_point(touch.x, touch.y):
            self.transition_popups()
            print self.parent.general_options.tm.states
            #test
            self.parent.general_options.tm.states[str(self.stateName)].add_transition('0', '1','1','L') #seensym, writesym, newstate, move
        if self.collide_point(touch.x, touch.y):
            self.touched = True
            self.select()
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def transition_popups(self):
        p4 = MovePopup()
        p4.bind(on_dismiss=self.move_callback)
        p4.open()
        p3 = NewStatePopup()
        p3.bind(on_dismiss=self.newstate_callback)
        p3.open()
        p2 = WriteSymPopup()
        p2.bind(on_dimiss=self.writesym_callback)
        p2.open()
        p1 = SeenSymPopup()
        p1.bind(on_dimiss=self.seensym_callback)
        p1.open()

    '''fix this shit for me cos it's 6am and i ceebs and do the error checking'''

    def move_callback(self, instance):
        self.initialtape = instance.getInfo()
        print self.initialtape
        self.updateTM
        return False

    def newstate_callback(self, instance):
        self.alphabet = instance.getInfo()
        print self.alphabet
        return False

    def writesym_callback(self, instance):
        self.alphabet = instance.getInfo()
        print self.alphabet
        return False

    def seensym_callback(self, instance):
        self.alphabet = instance.getInfo()
        print self.alphabet
        return False

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
'''might have to fix up this one a bit'''


    def on_touch_up(self, touch):
        # go = self.parent.general_options
        self.touched = False
        if self.selected:
            if self.parent.general_options.set_state:
                # self.parent.general_options.initialstate = self.stateName
                self.parent.general_options.tm.set_initialstate(self.stateName)
                print "New Initial State is: " + str(self.parent.general_options.tm.initialstate)
            if self.parent.general_options.final_states:
                # self.parent.general_options.finalstates.add(self.stateName)
                self.parent.general_options.tm.set_finalstates(self.stateName)
                print "The final states are: " + str(self.parent.general_options.tm.finalstates)
            self.unselect()
        return super(DraggableWidget, self).on_touch_up(touch)

    # def do_transition(self):
    #

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None

class StateRep(DraggableWidget):
    r = NumericProperty(1)

    def change_r(self, change):
        self.r = change

    def goback(self):
        self.r = 1

class MovePopup(Popup):
    pass
class NewStatePopup(Popup):
    pass
class WriteSymPopup(Popup):
    pass
class SeenSymPopup(Popup):
    pass

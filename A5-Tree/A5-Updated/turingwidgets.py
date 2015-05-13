# File name: turingwidgets.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.graphics import Line
from kivy.graphics import Color,Ellipse
from kivy.uix.label import Label
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
        # double tap to add transitions to a tm directly
        if touch.is_double_tap and self.collide_point(touch.x, touch.y):
            self.transition_popups()
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
        p2.bind(on_dismiss=self.writesym_callback)
        p2.open()
        p1 = SeenSymPopup()
        p1.bind(on_dismiss=self.seensym_callback)
        p1.open()


    def move_callback(self, instance):
        print "CALL BACK CALLED for move"
        #TODO -- PASS this info to the TM (preferably as a complete transition)
        self.parent.general_options.collect_trans_info(instance.getInfo(),4,str(self.stateName))
        self.unselect()
        return False

    def newstate_callback(self, instance):

        print "CALL BACK CALLED __ for new state"
        print str(self.stateName) + " is the currentStateName"
        #TO CAN YOU GET THE DRAWING SPACE TO CALL GENERAL OPTIONS???
        self.parent.general_options.collect_trans_info(instance.getInfo(),3,str(self.stateName))
        return False

    def writesym_callback(self, instance):
        print "CALL BACK CALLED to write \n-------------------------------\n"
        self.parent.general_options.collect_trans_info(instance.getInfo(),2,str(self.stateName))
        #TODO -- PASS this info to the TM (preferably as a complete transition)
        return False

    def seensym_callback(self, instance):
        self.parent.general_options.collect_trans_info(instance.getInfo(),1,str(self.stateName))
        print "CALL BACK CALLED FOR SYM"
        #TODO -- PASS this info to the TM (preferably as a complete transition)

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

    #changes a stateRep object Red
    def redraw_red_accepting(s, *args):
        print "Redraw method has been activated, changing to red"
        s.canvas.clear()
        with s.canvas:
            Color(s.r, 0, 0, 1)
            Ellipse(pos = (9,9), size = (30,30))
        s.add_widget(Label(text="ID:" + str(s.stateName),padding_x=(20), padding_y=(25),halign="right",valign="top"))
        s.add_widget((Label(text=str("[color=000000]A[/color]"),markup =True)))

    #Changes a stateRep object Blue
    def redraw_white_initial(s, *args):
        print "Redraw method has been activated, changing to white"
        s.canvas.clear()
        with s.canvas:
            Color(s.r, 1, 1, 1)
            Ellipse(pos = (9,9), size = (30,30))
        s.add_widget(Label(text="ID:" + str(s.stateName),padding_x=(20), padding_y=(25),halign="right",valign="top"))
        s.add_widget((Label(text=str("[color=000000]I[/color]"),markup =True)))
        #changes a stateRep object Red

    def redraw_highlight(s, *args):
        print "Redraw method has been activated, changing to red"
        s.canvas.clear()
        with s.canvas:
            Color(s.r, 0, 1, 1)
            Ellipse(pos = (9,9), size = (30,30))
        s.add_widget(Label(text="ID:" + str(s.stateName),padding_x=(20), padding_y=(25),halign="right",valign="top"))

    #this method calls the redraw method above... Not working as we wanted yet.
    def change_color_please(self,color):
        if color == "red":
            self.redraw_red_accepting(self)
        elif color == "white":
            self.redraw_white_initial(self)
        elif color == "highlight":
            self.redraw_red_highlight(self)


    def change_r(self, change):
        self.r = change

    def goback(self):
        self.r = 1


    def printMe(self):
        print "My details are "
        print "seen:\t" + self.seen
        print self.move
        print self.newState
        print self.write

class MovePopup(Popup):
    move = ''

    def getInfo(self):
        return self.move

    def get_useful_input(self,root,id):
        print  id.text
        input = id.text
        input = input.replace(" ", "")
        input = input.upper()

        if input == "L" or input == "R":
            print "YEP that is an L or R"
            self.move = input
            #TODO: send this to the tm
            root.dismiss()
        else:
            id.text= ""
            id.hint_text = "ERROR: INVALID INPUT ENTERED\nInput must be either L or R\nPLEASE ENTER AGAIN"


class NewStatePopup(Popup):
    newstate = ''

    def getInfo(self):
        return self.newstate

    def RepresentsInt(self,s):
        try:
            int(s)
            if int(s) >= 0:
                return True
        except ValueError:
            return False


    def get_useful_input(self,root,id):
        input = id.text
        input = input.replace(" ", "")
        input = input.lower()

        if self.RepresentsInt(input):
            print "Accepted"
            self.newstate = input
            #TODO: send this to the tm
            root.dismiss()

        else:
            id.text= ""
            id.hint_text = "ERROR: INVALID INPUT ENTERED\nInput must be a state ID\nPLEASE ENTER AGAIN"

class WriteSymPopup(Popup):
    writesym = ''

    def getInfo(self):
        return self.writesym

    def get_useful_input(self,root,id):
        input = id.text
        input = input.replace(" ", "")
        input = input.lower()

        if len(input) == 1:
            print "Accepted"
            self.writesym = input
            #TODO: HEY DAVE, FOR SOME REASON THIS root.dismiss() is not calling the call back... it works for move and newState but not this or seen state.  ???????????
            root.dismiss()

        else:
            id.text= ""
            id.hint_text = "ERROR: INVALID INPUT ENTERED\nInput must be one character from the alphabet\nPLEASE ENTER AGAIN"


class SeenSymPopup(Popup):
    seensym = ''

    def getInfo(self):
        return self.seensym

    def get_useful_input(self,root,id):
        input = id.text
        input = input.replace(" ", "")
        input = input.lower()

        if len(input) == 1:
            print "Accepted"
            self.seensym = input
            #TODO: send this to the tm
            root.dismiss()
        else:
            id.text= ""
            id.hint_text = "ERROR: INVALID INPUT ENTERED\nInput must be one character from the alphabet\nPLEASE ENTER AGAIN"

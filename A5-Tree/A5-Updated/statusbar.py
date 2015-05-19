# File name: statusbar.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.effects.scroll import ScrollEffect
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
from functools import partial

class StatusBar(BoxLayout):
    tape = StringProperty('')
    nextstep = BooleanProperty(False)
    paused = BooleanProperty(False)

    def stepthrough(self, currentstate, currenttape):
        self.msg_label1.text = "Current State: " + currentstate
        self.msg_label2.text = "Tape: " + currenttape

    def pausechange(self, bool1):
        self.paused = bool1
        print self.paused

    def nextchange(self):
        self.parent.general_options.step_tm()

    def finished(self, halted, finaltape):
        self.msg_label1.text = halted
        self.msg_label2.text = "Tape" + finaltape

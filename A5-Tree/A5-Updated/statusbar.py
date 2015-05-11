# File name: statusbar.py
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
from functools import partial

class StatusBar(BoxLayout):
    tape = StringProperty('')
    counter = NumericProperty(0)
    previous_counter = 0

    def on_counter(self, instance, value):
        self.msg_label.text = 'Tape: ' + self.parent.general_options.tm.gettape()

    def finished(self, halted, finaltape):
        Clock.schedule_interval(partial(self.my_callback, halted, finaltape), 10)

    def my_callback(self, halted, finaltape, *largs):
        self.msg_label.text = halted
        Clock.schedule_once(partial(self.my_callback2, finaltape), 5)

    def my_callback2(self, finaltape, *largs):
        self.msg_label.text = 'Tape: ' + finaltape

        # if value == 0
        #     self.msg_label.text = "TM cleared"
        # elif value - 1 == self.__class__.previous_counter:
        #     self.msg_label.text = self.parent.general_options.test()
        # elif value + 1 == StatusBar.previous_counter:
        #     self.msg_label.text = "State removed"
        # self.__class__.previous_counter = value
        # tape = self.parent.general_options.tm.gettape()

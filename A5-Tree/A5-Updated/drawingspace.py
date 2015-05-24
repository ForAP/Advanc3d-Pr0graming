# File name: drawingspace.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout
from turingwidgets import Transition1, Transition2

class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        if isinstance(self.children[0], Transition1) or isinstance(self.children[0], Transition2):
            move = self.children.pop(0)
            self.children.append(move)

    def delete_transitions(self):
        for child in self.children:
            if isinstance(child, Transition1) or isinstance(child, Transition2):
                self.remove_widget(child)

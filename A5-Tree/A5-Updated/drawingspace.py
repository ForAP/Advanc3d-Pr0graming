# File name: drawingspace.py
import kivy
kivy.require('1.7.0')
from kivy.uix.relativelayout import RelativeLayout
from toolbox import Transition

class DrawingSpace(RelativeLayout):
    def on_children(self):
        if isinstance(self.children[0], Transition):
            move = self.children.pop([0])
            self.children.append(move)

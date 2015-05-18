__author__ = 'Fabrizio'

#kivy.require(1.8.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Rectangle, Line
from kivy.uix import label

"""
http://robertour.com/2013/07/19/10-things-you-should-know-about-the-kivy-canvas/
That is just a little more info about a canvas


More learnt things:
    If we use the screen manager we can also save a canvas (This will store the Visual representation of a Turing machine)
    If we can load the canvas with the TM xml file then that wil work.  Run app to see. you can change between screens
    and not lose the circles or lines.

"""


class Painter(Widget):

    # Just a random method that isn't called at all
    def lets_print_something(self):
        print "You have just called this method, you can easily change this print statement to include:\n\tAdd State\n\tAdd Transisiton\n\tCreate TM\n\nWhy not try?"

    # The on touch down event which creates a circle (Ellipse) and start the line
    def on_touch_down(self, touch):
        with self.canvas:
            d = 50
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud["line"] = Line(points=(touch.x,touch.y))

    # The move event which adds length to the line depending on the touch motion
    def on_touch_move(self, touch):
       touch.ud['line'].points += [touch.x, touch.y]

    # The on touch up event which ends the line and adds a circle in the touch up spot
    def on_touch_up(self, touch):
        touch.ud["line"].points += [touch.x,touch.y]
        with self.canvas:
            d = 50
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
        print "I have run some things"



#These are all sample screens, you can add methods here if you like but it is probably better to just keep the implementation in the kivy file
class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

#This is the head honcho!!! This bad boy controls the layouts.
class ScreenManagement(ScreenManager):
    pass

#this defines the fist kivy file to be used.
presentation = Builder.load_file("main.kv")

#The rest is basic kivy stuff...
class MainApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    MainApp().run()
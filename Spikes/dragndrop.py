# File name: comiccreator.py
import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('comicwidgets.kv')

class DragNDrop(AnchorLayout):
    pass

class DragNDropApp(App):
    def build(self):
        return DragNDrop()

if __name__=="__main__":
    DragNDropApp().run()

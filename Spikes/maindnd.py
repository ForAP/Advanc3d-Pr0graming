# File name: maindnd.py
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('drawingspace.kv')
Builder.load_file('dnd.kv')

class DragNDrop(AnchorLayout):
    pass

class DragNDropApp(App):
    def build(self):
        return DragNDrop()

if __name__=="__main__":
    DragNDropApp().run()

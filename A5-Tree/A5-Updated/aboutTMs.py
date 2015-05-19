__author__ = 'Fabrizio'
__author__ = 'Fabrizio'
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import sys

class AboutScreen(Screen):
    def endProgram(self):
        sys.exit()

    def back(self):
        pass


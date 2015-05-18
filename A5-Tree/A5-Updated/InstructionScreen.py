__author__ = 'Fabrizio'
import kivy
kivy.require('1.7.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import sys

class InstructionScreen(Screen):
    def endProgram(self):
        sys.exit()

    def back(self):
        pass

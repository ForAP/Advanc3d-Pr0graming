from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(Screen):
    pass

presentation = Builder.load_file("builderSpike.kv")

class builderSpikeApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    builderSpikeApp().run()
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label 
from kivy.uix.widget import Widget

# _____ _____ _____ _____ _____ _____ _____
from kivy import Config
Config.set('graphics','multisamples','0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# _____ _____ _____ _____ _____ _____ _____

class Widgets(Widget): 
    pass 

class Simple(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    Simple().run()


from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput

# _____ _____ _____ _____ _____ _____ _____
from kivy import Config
Config.set('graphics','multisamples','0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# _____ _____ _____ _____ _____ _____ _____


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) 
        self.cols=2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

class CellbreakerSupervisor(App):
    def build(self):
        #return Label(text="Coucou") 
        return LoginScreen() 
if __name__ == "__main__":
    CellbreakerSupervisor().run()



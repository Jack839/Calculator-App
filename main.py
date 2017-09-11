#Kivy Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Window.size = (570, 720)

#Other Imports
import __future__
from math import pi

class CalcLayout(FloatLayout):
    Window.clearcolor = (1, 1, 1, 1)
    data_text=StringProperty()
    def valEnter(self,inputVal):
        if inputVal=="":
            self.data_text=self.data_text[0:-1]
        elif self.data_text=="Error":
            self.data_text=inputVal
        else:
            self.data_text+=inputVal
    def calc(self,valToEval):
        try:
            self.data_text=str(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag)))
        except:
            self.data_text="Error"
            
buildKV = Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

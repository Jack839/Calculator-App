import kivy
import __future__

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class CalcLayout(FloatLayout):
    Window.clearcolor = (1, 1, 1, 1)
    def valEnter(self,inputVal):
        if inputVal=="":
            self.data.text=""
        elif self.data.text=="Error":
            self.data.text=inputVal
        else:
            self.data.text+=inputVal
    def calc(self,valToEval):
        try:
            self.data.text=str(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag)))
        except:
            self.data.text="Error"
class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

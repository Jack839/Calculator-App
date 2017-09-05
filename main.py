import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class CalcLayout(GridLayout):
    Window.clearcolor = (1, 1, 1, 1)
    def valEnter(self,inputVal):
        if inputVal=="":
            self.data.text=""
        elif self.data.text=="Error":
            self.data.text=inputVal+".0 "
        else:
            if inputVal=="+" or inputVal=="-" or inputVal=="*" or inputVal=="/":
                self.data.text+=inputVal+" "
            else:
                self.data.text+=inputVal+".0 "
    def calc(self,valToEval):
        try:
            self.data.text=str(eval(valToEval))+" "
        except:
            self.data.text="Error"
class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

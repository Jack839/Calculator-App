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
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

#Window.size = (570, 720)

#Other Imports
import __future__
import math
#import android
import webbrowser

def evalFunction(a):
    b=""
    k="+"
    for j in range(0,5):
        for i in a.split(k):
            if i==a.split(k)[-1]:
                b+=i.strip("0")
            else:
                b+=i.strip("0")+k
        a,b=b,""
        if j==0:k="-"
        elif j==1:k="*"
        elif j==2:k="/"
        elif j==3:k="%"
    return a
def fact(x):
    n=1
    for i in range(x,0,-1):
       n=n*i
    return str(n)

class CalcLayout(FloatLayout):
    Window.clearcolor = (1, 1, 1, 1)
    data_text=StringProperty()
    def valEnter(self,inputVal):
        if inputVal=="":
            if self.data_text=="Error":
                self.data_text=""
            else:
                self.data_text=self.data_text[0:-1]
        elif self.data_text=="Error":
            self.data_text=inputVal
        else:
            if inputVal=="*" or inputVal=="/":
                if self.data_text !="" :
                    if self.data_text[len(self.data_text)-1]=="*" or self.data_text[len(self.data_text)-1]=="/" or self.data_text[len(self.data_text)-1]=="+" or self.data_text[len(self.data_text)-1]=="-":
                        self.data_text=self.data_text
                    else:
                        self.data_text+=inputVal
            else:
                self.data_text+=inputVal
    def internetActivity(self,Url):
        webbrowser.open(Url)
    def calc(self,valToEval):
        if len(valToEval)>0:
            try:
                valToEvalwithZeros=""
                k="+"
                for j in range(0,5):
                    for i in valToEval.split(k):
                        if i==valToEval.split(k)[-1]:
                            valToEvalwithZeros+=i.strip("0")
                        else:
                            valToEvalwithZeros+=i.strip("0")+k
                    valToEval,valToEvalwithZeros=valToEvalwithZeros,""
                    if j==0:k="-"
                    elif j==1:k="*"
                    elif j==2:k="/"
                    elif j==3:k="%"
                bool1=True
                while bool1:
                    if valToEval.find("sin(")!=-1:
                        valToEval=valToEval[:valToEval.find("sin(")]+str(math.sin(math.radians(float(calc(valToEval[valToEval.find("sin(")+4:(valToEval.find("sin(")+4+valToEval[valToEval.find("sin(")+4:].find(")"))])))))+valToEval[(valToEval.find("sin(")+4+valToEval[valToEval.find("sin(")+4:].find(")"))+1:]
                    elif valToEval.find("cos(")!=-1:
                        valToEval=valToEval[:valToEval.find("cos(")]+str(math.cos(math.radians(float(calc(valToEval[valToEval.find("cos(")+4:(valToEval.find("cos(")+4+valToEval[valToEval.find("cos(")+4:].find(")"))])))))+valToEval[(valToEval.find("cos(")+4+valToEval[valToEval.find("cos(")+4:].find(")"))+1:]
                    elif valToEval.find("tan(")!=-1:
                        valToEval=valToEval[:valToEval.find("tan(")]+str(math.tan(math.radians(float(calc(valToEval[valToEval.find("tan(")+4:(valToEval.find("tan(")+4+valToEval[valToEval.find("tan(")+4:].find(")"))])))))+valToEval[(valToEval.find("tan(")+4+valToEval[valToEval.find("tan(")+4:].find(")"))+1:]
                    elif valToEval.find("log(")!=-1:
                        valToEval=valToEval[:valToEval.find("log(")]+str(math.log10(float(calc(valToEval[valToEval.find("log(")+4:(valToEval.find("log(")+4+valToEval[valToEval.find("log(")+4:].find(")"))]))))+valToEval[(valToEval.find("log(")+4+valToEval[valToEval.find("log(")+4:].find(")"))+1:]
                    elif valToEval.find("ln(")!=-1:
                        valToEval=valToEval[:valToEval.find("ln(")]+str(math.log(float(calc(valToEval[valToEval.find("ln(")+3:(valToEval.find("ln(")+3+valToEval[valToEval.find("ln(")+3:].find(")"))]))))+valToEval[(valToEval.find("ln(")+3+valToEval[valToEval.find("ln(")+3:].find(")"))+1:]
                    elif valToEval.find("!")!=-1:
                        for op in range(valToEval.find("!"),-1,-1):
                            if valToEval[op]=="*" or valToEval[op]=="/" or valToEval[op]=="+" or valToEval[op]=="-":
                                valToEval=valToEval[:op+1]+fact(int(valToEval[op+1:valToEval.find("!")]))+valToEval[valToEval.find("!")+1:]
                                break
                            elif op==0:
                                valToEval=fact(int(evalFunction(valToEval[0:valToEval.find("!")])))+valToEval[valToEval.find("!")+1:]
                    else:
                        bool1=False
                self.data_text=str(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag)))
            except:
                self.data_text="Error"

#buildKV = Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

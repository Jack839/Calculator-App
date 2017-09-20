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
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

#Window.size = (570, 720)

#Other Imports
import __future__
import math
#import android
import urllib2
import webbrowser
import time

__version__=2.3

def evalFunction(valToEval):
    b=""
    k="+"
    for j in range(0,5):
        for i in range(0,len(valToEval.split(k))):
            if i==len(valToEval.split(k))-1:
                b+=valToEval.split(k)[i].lstrip("0")
            else:
                b+=valToEval.split(k)[i].lstrip("0")+k
        valToEval,b=b,""
        if j==0 and valToEval.find("-")!=-1:k="-"
        elif j==1 and valToEval.find("*")!=-1:k="*"
        elif j==2 and valToEval.find("/")!=-1:k="/"
        elif j==3 and valToEval.find("%")!=-1:k="%"
    return str(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag)))
def fact(x):
    n=1
    for i in range(x,0,-1):
       n=n*i
    return str(n)

class CalcLayout(FloatLayout):
    Window.clearcolor = (1, 1, 1, 1)
    data_text=StringProperty()
    update_text=StringProperty()
    title_text=StringProperty()
    def __init__(self):
        super(CalcLayout, self).__init__()
        try:
            changeLog=open("ota.txt","r+")
            file_data=changeLog.read()
            changeLog.close()
            ota_check=urllib2.urlopen("https://raw.githubusercontent.com/Jack839/Calculator-App/master/ota.txt")
            read_data=ota_check.read()
            if float(read_data[1:4])>__version__:
                ota=open("ota.txt","w+")
                ota.write(read_data)
                ota.close()
                self.title_text="Update Available: v"+read_data[1:4]
                self.update_text=read_data[6:-3]
                self.ids.updatePop.open()
            elif int(file_data[-2])==0:
                file_data=file_data[:-2]+str(int(file_data[-2])+1)+"\n"
                ota=open("ota.txt","w+")
                ota.write(file_data)
                ota.close()
                self.title_text="ChangeLogs"
                self.update_text=read_data[6:-3]
                self.ids.updatePop.open()
            else:
                self.remove_widget(self.ids.updatePop)
        except Exception:
            self.remove_widget(self.ids.updatePop)
    def valEnter(self,inputVal):
        if self.data_text=="Error":
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
    def onLongPressCheck(self,pressCheck):
        if pressCheck=="":
            global start_time
            start_time=time.time()
        elif pressCheck==" ":
            time_passed=time.time()-start_time
            if time_passed>=0.5:
                self.data_text=""
            else:
                if self.data_text=="Error":
                    self.data_text=""
                else:
                    self.data_text=self.data_text[0:-1]
    def internetActivity(self,Url):
        webbrowser.open(Url)
    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(text_input.text,text_input.tab_width,text_input._label_cached)
        text_input.padding_x = (text_input.width - text_width)/2
    def calc(self,valToEval):
        if len(valToEval)>0:
            try:
                bool1=True
                while bool1:
                    if valToEval.find("sin(")!=-1:
                        valToEval=valToEval[:valToEval.find("sin(")]+str(math.sin(math.radians(float(evalFunction(valToEval[valToEval.find("sin(")+4:(valToEval.find("sin(")+4+valToEval[valToEval.find("sin(")+4:].find(")"))])))))+valToEval[(valToEval.find("sin(")+4+valToEval[valToEval.find("sin(")+4:].find(")"))+1:]
                    elif valToEval.find("cos(")!=-1:
                        valToEval=valToEval[:valToEval.find("cos(")]+str(math.cos(math.radians(float(evalFunction(valToEval[valToEval.find("cos(")+4:(valToEval.find("cos(")+4+valToEval[valToEval.find("cos(")+4:].find(")"))])))))+valToEval[(valToEval.find("cos(")+4+valToEval[valToEval.find("cos(")+4:].find(")"))+1:]
                    elif valToEval.find("tan(")!=-1:
                        valToEval=valToEval[:valToEval.find("tan(")]+str(math.tan(math.radians(float(evalFunction(valToEval[valToEval.find("tan(")+4:(valToEval.find("tan(")+4+valToEval[valToEval.find("tan(")+4:].find(")"))])))))+valToEval[(valToEval.find("tan(")+4+valToEval[valToEval.find("tan(")+4:].find(")"))+1:]
                    elif valToEval.find("log(")!=-1:
                        valToEval=valToEval[:valToEval.find("log(")]+str(math.log10(float(evalFunction(valToEval[valToEval.find("log(")+4:(valToEval.find("log(")+4+valToEval[valToEval.find("log(")+4:].find(")"))]))))+valToEval[(valToEval.find("log(")+4+valToEval[valToEval.find("log(")+4:].find(")"))+1:]
                    elif valToEval.find("ln(")!=-1:
                        valToEval=valToEval[:valToEval.find("ln(")]+str(math.log(float(evalFunction(valToEval[valToEval.find("ln(")+3:(valToEval.find("ln(")+3+valToEval[valToEval.find("ln(")+3:].find(")"))]))))+valToEval[(valToEval.find("ln(")+3+valToEval[valToEval.find("ln(")+3:].find(")"))+1:]
                    elif valToEval.find("!")!=-1:
                        for op in range(valToEval.find("!"),-1,-1):
                            if valToEval[op]=="*" or valToEval[op]=="/" or valToEval[op]=="+" or valToEval[op]=="-":
                                valToEval=valToEval[:op+1]+fact(int(valToEval[op+1:valToEval.find("!")]))+valToEval[valToEval.find("!")+1:]
                                break
                            elif op==0:
                                valToEval=fact(int(valToEval[0:valToEval.find("!")]))+valToEval[valToEval.find("!")+1:]
                    else:
                        bool1=False
                self.data_text=evalFunction(valToEval)
            except:
                self.data_text="Error"

#buildKV = Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

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
from math import *
#import android
import urllib2
import webbrowser
import time

__version__=2.5

def evalFunction(valToEval):
    b=""
    k="+"
    for j in range(0,6):
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
        elif j==4 and valToEval.find("(")!=-1:k="("
    return str(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag),{'sin': sin,'cos': cos,'tan': tan,'log': log10,'ln': log,'pi': pi}))

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
        changeLog=open("ota.txt","r+")
        file_data=changeLog.read()
        changeLog.close()
        try:
            ota_check=urllib2.urlopen("https://raw.githubusercontent.com/Jack839/Calculator-App/master/ota.txt")
            read_data=ota_check.read()
            if float(read_data[1:4])>__version__:
                ota=open("ota.txt","w+")
                ota.write(read_data)
                ota.close()
                self.title_text="Update Available: v"+read_data[1:4]
                self.update_text=read_data[6:-3]
                self.ids.updatePop.open()
        except Exception:
            pass
        finally:
            if int(file_data[-2])==0:
                file_data=file_data[:-2]+str(int(file_data[-2])+1)+"\n"
                ota=open("ota.txt","w+")
                ota.write(file_data)
                ota.close()
                self.title_text="ChangeLogs"
                self.update_text=file_data[125:-3]
                self.ids.updatePop.open()
            else:
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
    def calc(self,valToEval):
        if len(valToEval)>0:
            bool1=True
            while bool1:
                if valToEval.find("!")!=-1:
                    for op in range(valToEval.find("!"),-1,-1):
                        if valToEval[op]=="*" or valToEval[op]=="/" or valToEval[op]=="+" or valToEval[op]=="-":
                            valToEval=valToEval[:op+1]+fact(int(valToEval[op+1:valToEval.find("!")]))+valToEval[valToEval.find("!")+1:]
                            break
                        elif op==0:
                            valToEval=fact(int(valToEval[0:valToEval.find("!")]))+valToEval[valToEval.find("!")+1:]
                else:
                    bool1=False
            try:
                self.data_text=evalFunction(valToEval)
            except:
                self.data_text="Error"

#buildKV = Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

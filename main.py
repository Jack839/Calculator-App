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

#Window.size = (570, 720)

#Other Imports
import android
from math import *
from decimal import *
import __future__
import urllib2
import webbrowser
import time

#Global Variables
__version__=2.7
mode_count=1
angle_count=1

def zeroChange(valToEval,toFind,toReplace):
    if toFind=="0":
        for indexVal in range(0,len(valToEval)):
            if valToEval.find(toFind)!=-1:
                try:
                    if valToEval[indexVal]==toFind:
                        if valToEval[indexVal-1]=="+" or valToEval[indexVal-1]=="-" or valToEval[indexVal-1]=="/" or valToEval[indexVal-1]=="*" or valToEval[indexVal-1]=="%" or valToEval[indexVal-1]=="(" or valToEval[indexVal-1]==")" or valToEval[indexVal-1]=="^":
                            for nextIndex in range(indexVal,len(valToEval)):
                                if valToEval[nextIndex]=="+" or valToEval[nextIndex]=="-" or valToEval[nextIndex]=="/" or valToEval[nextIndex]=="*" or valToEval[nextIndex]=="%" or valToEval[nextIndex]=="(" or valToEval[nextIndex]==")" or valToEval[nextIndex]=="^":
                                    if valToEval[indexVal:nextIndex]!="c":
                                        if str(eval(valToEval[indexVal:nextIndex]))==toFind:
                                            valToEval=valToEval[:indexVal]+toReplace+valToEval[nextIndex:]
                                            break
                                    else:
                                        if valToEval[indexVal:nextIndex]==toFind:
                                            valToEval=valToEval[:indexVal]+toReplace+valToEval[nextIndex:]
                                            break
                except Exception:
                    pass
    else:
        for indexVal in range(0,len(valToEval)):
            if valToEval[indexVal]==toFind:
                valToEval=valToEval[:indexVal]+"0"+valToEval[indexVal+1:]
    if valToEval[0]=="c" or valToEval[0]=="0" or valToEval[-1]=="0" or valToEval[-1]=="c" :
        for numVal in range(0,len(valToEval)):
            if valToEval[numVal]=="+" or valToEval[numVal]=="-" or valToEval[numVal]=="*" or valToEval[numVal]=="/" or valToEval[numVal]=="%" or valToEval[numVal]=="^" or valToEval[numVal]=="(" or valToEval[numVal]==")":
                if valToEval[:numVal]==toFind:
                    valToEval=toReplace+valToEval[numVal:]
                    break
                elif str(float(eval(valToEval[:numVal])))==toFind+".0":
                    valToEval=toReplace+valToEval[numVal:]
                    break
                else:
                    break
        for numVal in range(len(valToEval)-1,-1,-1):
            if valToEval[numVal]=="+" or valToEval[numVal]=="-" or valToEval[numVal]=="*" or valToEval[numVal]=="/" or valToEval[numVal]=="%" or valToEval[numVal]=="^" or valToEval[numVal]=="(" or valToEval[numVal]==")":
                if valToEval[numVal+1:]==toFind:
                    valToEval=valToEval[:numVal+1]+toReplace
                    break
                elif str(float(eval(valToEval[numVal+1:])))==toFind+".0":
                    valToEval=valToEval[:numVal+1]+toReplace
                    break
                else:
                    break
    return valToEval

def fact(x):
    if type(factorial(x))==long:
        return '{:.8e}'.format(Decimal(factorial(x)))
    else:
        return factorial(x)

def evalFunction(valToEval):
    b=""
    l=["+","-","*","/","%","^",")","("]
    valToEval=zeroChange(valToEval,"0","z")
    checkValToEval=valToEval
    for j in l:
        for i in range(0,len(valToEval.split(j))):        
            if i==len(valToEval.split(j))-1:
                b+=valToEval.split(j)[i].lstrip("0")
            else:
                b+=valToEval.split(j)[i].lstrip("0")+j
        valToEval,b=b,""
    valToEval=zeroChange(valToEval,"z","0")
    valToEval=changeInString(valToEval,True)
    finalResult=round(float(eval(compile(valToEval, '<string>', 'eval', __future__.division.compiler_flag),{"sqrt": sqrt, 'log': log10,'ln': log,'pi': pi,"e":e,"fact": fact, "rad": radians, "deg": degrees, 'sin': sin,'cos': cos,'tan': tan, "asin": asin,"acos": acos,"atan": atan})),15)
    if type(finalResult)==long:
        finalResult=str('{:.8e}'.format(Decimal(finalResult)))
    elif str(finalResult).find("e-")!=-1:
        finalResult=str(format(finalResult, '.8f'))
    else:
        finalResult=str(finalResult)
    return finalResult

def bracketValue(strToEval,index,t=0):
    if t==0:
        count_open=0
        count_close=1
        check=1
        for last_open in range(index,-1,-1):
            if strToEval[last_open]=="(":
                count_open+=1
            elif strToEval[last_open]==")":
                if check==1:
                    check=0
                else:
                    count_close+=1
            if count_open==count_close:
                break
        return last_open
    else:
        count_open=1
        count_close=0
        check=1
        for last_close in range(index,len(strToEval)):
            if strToEval[last_close]=="(":
                if check==1:
                    check=0
                else:
                    count_open+=1
            elif strToEval[last_close]==")":
                count_close+=1
            if count_open==count_close:
                break
        return last_close+1

def changeInString(valToEval,bool4=False):
    bool3=True
    while bool3:
        if valToEval.find("sin[sup]-1[/sup]")!=-1:
            valToEval=valToEval[:valToEval.find("sin[sup]-1[/sup]")]+"asin"+valToEval[valToEval.find("sin[sup]-1[/sup]")+16:]
        elif valToEval.find("cos[sup]-1[/sup]")!=-1:
            valToEval=valToEval[:valToEval.find("cos[sup]-1[/sup]")]+"acos"+valToEval[valToEval.find("cos[sup]-1[/sup]")+16:]
        elif valToEval.find("tan[sup]-1[/sup]")!=-1:
            valToEval=valToEval[:valToEval.find("tan[sup]-1[/sup]")]+"atan"+valToEval[valToEval.find("tan[sup]-1[/sup]")+16:]
        elif bool4:
            if valToEval.find("^")!=-1:            
                valToEval=valToEval[:valToEval.find("^")]+"**"+valToEval[valToEval.find("^")+1:]
                continue
            else:
                bool3=False
        else:
            bool3=False
    return valToEval

def angleConversion(valToEval):
    _list = ["sin", "cos", "tan"]
    for _substring in _list:
        _index = 0
        while ((valToEval.find(_substring, _index)) != -1) :
            _condition = 0
            _index = valToEval.find(_substring, _index)
            if valToEval[_index-1] == "a" : _condition = 1
            count_a = 1
            count_b = 0
            x = _index + 3 + _condition
            while count_a != count_b :
                x = x + 1
                if valToEval[x] == "(" : count_a = count_a + 1
                elif valToEval[x] == ")" : count_b = count_b + 1
            if _condition : valToEval = valToEval[:_index-1] + ("deg(") + valToEval[_index-1:x] + (")") + valToEval[x:]
            else : valToEval = valToEval[:_index+4] + ("rad(") + valToEval[_index+4:x] + (")") + valToEval[x:]
            _index = _index + 4 + _condition        
    return valToEval
                
class CalcLayout(FloatLayout):

    Window.clearcolor = (1, 1, 1, 1)
    data_text=StringProperty()
    update_text=StringProperty()
    title_text=StringProperty()
    button_sin_text=StringProperty()
    button_cos_text=StringProperty()
    button_tan_text=StringProperty()
    button_ln_text=StringProperty()
    button_log_text=StringProperty()
    button_angle_text=StringProperty()
    
    def __init__(self):
        super(CalcLayout, self).__init__()
        self.inverseMode()
        self.angleChange()
        timeCheckFile=open("time_check.dat","r+")
        timeCheckData=timeCheckFile.read()
        timeCheckFile.seek(0,0)
        initialCheck=timeCheckData[:9]
        lastTimeUpdateCheck=timeCheckFile.read(2)
        changeLog=open("ota.txt","r+")
        file_data=changeLog.read()
        changeLog.close()
        if initialCheck=="EmptyFile" or fabs(float(lastTimeUpdateCheck)-float(time.ctime()[11:13]))>=12:
            try:
                ota_check=urllib2.urlopen("https://raw.githubusercontent.com/Jack839/Calculator-App/master/ota.txt")
                read_data=ota_check.read()
                bool6=True
            except Exception:
                bool6=False
            if float(read_data[1:4])>__version__ and bool6:
                ota=open("ota.txt","w+")
                ota.write(read_data)
                ota.close()
                self.title_text="Update Available: v"+read_data[1:4]
                self.update_text=read_data[6:read_data.find("ChangeLog(v2.6):")]
                self.ids.updatePop.open()
            elif file_data[-2]=="0" and float(read_data[1:4])==__version__:
                file_data=file_data[:-2]+str(int(file_data[-2])+1)+"\n"
                ota=open("ota.txt","w+")
                ota.write(file_data)
                ota.close()
                self.title_text="ChangeLogs"
                self.update_text=file_data[125:-3]
                self.ids.updatePop.open()
            else:
                self.remove_widget(self.ids.updatePop)
            timeCheckFile=open("time_check.dat","w")
            timeCheckFile.write(time.ctime()[11:13])
            timeCheckFile.close()
        else:
            if file_data[-2]=="0":
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
        if self.data_text=="[color=F50057]Bad Expression[/color]" or self.data_text=="[color=F50057]Domian Error[/color]" or self.data_text=="[color=F50057]Infinity[/color]" or self.data_text=="[color=F50057]Not Defined[/color]":
            self.data_text=inputVal
        else:
            if inputVal=="*" or inputVal=="/" or inputVal=="%" or inputVal=="^":
                if self.data_text !="" :
                    if self.data_text[len(self.data_text)-1]=="*" or self.data_text[len(self.data_text)-1]=="/" or self.data_text[len(self.data_text)-1]=="+" or self.data_text[len(self.data_text)-1]=="-" or self.data_text[len(self.data_text)-1]=="%" or self.data_text[len(self.data_text)-1]=="^":
                        self.data_text=self.data_text
                    else:
                        self.data_text+=inputVal
            elif inputVal=="+" or inputVal=="-":
                if self.data_text !="" :
                    if self.data_text[-2:]=="++" or self.data_text[-2:]=="--":
                        self.data_text=self.data_text
                    else:
                        self.data_text+=inputVal
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
                if self.data_text=="[color=F50057]Bad Expression[/color]" or self.data_text=="[color=F50057]Domian Error[/color]" or self.data_text=="[color=F50057]Infinity[/color]" or self.data_text=="[color=F50057]Not Defined[/color]":
                    self.data_text=""
                elif self.data_text[-13:]=="[sup]-1[/sup]":
                    self.data_text=self.data_text[:-13]
                else:
                    self.data_text=self.data_text[0:-1]
                    
    def internetActivity(self,Url):
        webbrowser.open(Url)

    def inverseMode(self, button_click=0):
        if button_click==0:
            global mode_count
            mode_count+=1
            if mode_count%2!=0:
                self.button_sin_text="    sin[sup]-1[/sup]"
                self.button_cos_text="    cos[sup]-1[/sup]"
                self.button_tan_text="    tan[sup]-1[/sup]"
                self.button_ln_text="    e^"
                self.button_log_text="    10^"
            else:
                self.button_sin_text="    sin"
                self.button_cos_text="    cos"
                self.button_tan_text="    tan"
                self.button_ln_text="    ln"
                self.button_log_text="    log"
        elif button_click==1:
            if self.button_log_text=="    10^":
                self.valEnter(self.button_log_text[4:])
            elif self.button_log_text=="    log":
                self.valEnter(self.button_log_text[4:]+"(")
        elif button_click==2:
            if self.button_ln_text=="    e^":
                self.valEnter(self.button_ln_text[4:])
            elif self.button_ln_text=="    ln":
                self.valEnter(self.button_ln_text[4:]+"(")

    def angleChange(self):
        global angle_count
        global angle_check
        angle_check=False
        angle_count+=1
        if angle_count%2!=0:
            self.button_angle_text="    DEG"
            angle_check=True
        else:
            self.button_angle_text="    RAD"
            angle_check=False

    def calc(self,valToEval):
        if len(valToEval)>0:
            try:
                bool5=True
                while bool5:
                    if valToEval.find(u"\u221A")!=-1:
                        valToEval=valToEval[:valToEval.find(u"\u221A")]+"sqrt"+valToEval[valToEval.find(u"\u221A")+1:]
                    elif valToEval.find(u"\u03C0")!=-1:
                        valToEval=valToEval[:valToEval.find(u"\u03C0")]+'pi'+valToEval[valToEval.find(u"\u03C0")+1:]
                    else:
                        valToEval=str(valToEval)
                        bool5=False
                valToEval=changeInString(valToEval)
                if evalFunction(valToEval)=="inf":
                    self.data_text="[color=F50057]Infinity[/color]"
                else:
                    if angle_check:
                        valToEval=angleConversion(valToEval)
                    self.data_text=str(float(evalFunction(valToEval)))
            except ValueError:
                self.data_text="[color=F50057]Domian Error[/color]"
            except TypeError:
                self.data_text="[color=F50057]Not Defined[/color]"
            except ZeroDivisionError :
                self.data_text="[color=F50057]Can't Divide By Zero[/color]"
            except Exception:
                self.data_text="[color=F50057]Bad Expression[/color]"

#buildKV = Builder.load_file("calculator.kv")

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if "__main__" == __name__:
    CalculatorApp().run()

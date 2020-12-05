#! /usr/bin/python3

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from app.getemployeeFunction import getEmployee, getMenuList


class PopUpShow(FloatLayout):

    def show_popup_unknown():
        show = PopUpShow() 

        popupWindow = Popup(
            title="Identifiant introuvable", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        # Create the popup window

        popupWindow.open() # show the popup


class AskId(Widget):
    
    employeeId_DB  = ListProperty([])
    employeeId_DB = []
    
    getEmployeeId = getEmployee()

    for id in getEmployeeId:
        employeeId_DB.append(id)
        
    
        displayPOSid = StringProperty(str(employeeId_DB[0])) 
        
    def change_label_method(self):
        self.layout_widget.text = '0'

        if id == None:
            PopUpShow.show_popup_unknown()
            print('id nok')
        else:
            print('id ok')
            
            pos_app.screen_manager.current = "POS"
    def deleteLine(self, **kwargs):
        print('Delete Line')

class MyGridLayout(ScrollView):
    
    
    MyMenuId = ListProperty([])
    MyMenuId = []
    displayPOS = ListProperty([])
    displayPOS = []
  
    
    getMenuId = getMenuList()
  
    
    for menuid in getMenuId:
        MyMenuId.append(menuid)
  
        print('Menu:\n' + str(MyMenuId))

    
    def back(self):
        pos_app.screen_manager.current = "Connect"
    def add_user(self):
        print('Add User')

    def modify_user(self):
        print('Modify User')
        
    def add_menu(self):
        print('Add menu')
    
    def modify_menu(self):
        print('Modify menu')
        
class Calculator(Widget):
    label = ''
    
    def delete(self, instance):
        self.display.text = instance[:0]
    
    def del1(self, instance):
        self.display.text = instance[:-1]
    
    def calc(self, instance):
        try:
            self.display.text = str(eval(instance))
            self.result.text = str(eval(instance))
        except Exception:
            self.display.text = '0'
            self.result.text = 'ERROR'
            
class Meals(App):
    trigger = False
    triggerC = False
    triggerD = False
    
    Window.size = (1024, 768)
    Window.minimum_width, Window.minimum_height = Window.size
    # Window.borderless = True
    def on_start(self):
        getEmployee()

    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = AskId()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)
        
        self.pos_page = MyGridLayout()
        screen = Screen(name="POS")
        screen.add_widget(self.pos_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager
        
if __name__ == "__main__":
    pos_app  = Meals()
    pos_app.run()
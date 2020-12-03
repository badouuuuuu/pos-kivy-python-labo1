#! /usr/bin/python3

import kivy
import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from app.employee import getEmployee
from kivy.properties import ObjectProperty

'''
try:
    conn = sqlite3.connect(r'database/meals.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    query_result = cursor.fetchall()
except sqlite3.Error as error:
    print("Error while reading from cursor : ", error)
print(query_result)
'''

Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size
# Window.borderless = True
id = None

        
class PopUpShow(FloatLayout):

    def show_popup_unknown():
        show = PopUpShow() # Create a new instance of the P class 

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
    def change_label_method(self):
        show = PopUpShow() # Create a new instance of the P class 

        self.layout_widget.text = '0'

        if id == None:
            PopUpShow.show_popup_unknown()
            print('id nok')
        else:
            print('id ok')
    def deleteLine(self, **kwargs):
        print('Delete Line')

class MyGridLayout(Widget):
    calcResult = ObjectProperty(None)
    calcDisplay = ObjectProperty(None)
    def add_user(self):
        print('Add User')
    # Mise en place de class, mise au propre du fichier gui.py
    
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
    def on_start(self):
        getEmployee()

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    Meals().run()
#! /usr/bin/python3

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
# from app.getFunction import getEmployee, getMenuList
from app.meals_management_v1 import get_employee_id, get_id_list, get_menu_description, get_employee_name, get_purchase_id
from kivy.uix.recycleview import RecycleView 


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
    order = []
    def CheckId(self):
        displayPOSid  = ''
        employee_id_db = get_id_list('employee')
        displayPOSid = self.ids.askid_label.text 
        print(employee_id_db)    
        print('encodé : '+displayPOSid)
        
        intdisplayPOSid = int(displayPOSid)

        if intdisplayPOSid in employee_id_db:

                employeeName = get_employee_name(displayPOSid)
                print(employeeName)
                print('id ok')
                print(displayPOSid)
                pos_app.screen_manager.current = "POS"

        else:
            self.ids.askid_label.text   = ''
            PopUpShow.show_popup_unknown()
            print('id nok')
            print(displayPOSid)
            
                
        

            

            
    def deleteLine(self, **kwargs):
        print('Delete Line')
        self.ids.askid_label.text = ''

class MyGridLayout(ScrollView):
    menu_id_db = get_id_list('menu')
    getpurchase_id = get_purchase_id()
    order = []
    purchase_menu = {
        "id employee" : { # to change with id add by user in Connect Page
        getpurchase_id: order
                        }
                    }       
    print('------------')

    
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        label_backup = StringProperty('')

        
        for id_menu in self.menu_id_db:
                print('id : ' + str(id_menu))  
                self.descr = get_menu_description(id_menu)
                print('menu : ' + self.descr)
                self.ids.label_backup.text += self.descr + '\n'
        print('------------')   


        
    def list_menu(self):
        menuList = ListProperty([]) 
        menuList = []
        menu_id_db = get_id_list('menu')
        for id in menu_id_db:
            menu = get_menu_description(id)
            self.ids.label_backup.text += self.descr
            menuList.append(menu)
        
        displayLeft = self.ids.label.text 

        self.ids.label_backup.text = ''
    
        MenuDescription = get_menu_description(displayLeft) 
        
        self.order.append(MenuDescription)
        self.ids.label.text = ''
        test = self.purchase_menu["id employee"][23]
        print(test)
        
        self.data = [{'text': str(x)} for x in range(5)] 

        displayLabel = self.ids.label_backup.text 
        for i in test:
            print(i)
            self.ids.label_backup.text =  i + '\n'
            
            


        
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
    
    def delete(self, instance):
        self.display.text = str(eval(instance))
        self.display.text = instance[:0]
    
    def del1(self, instance):
        self.display.text = str(eval(instance))
        self.display.text = instance[:-1]
    
    def addition(self, instance):
        try:
            self.display.text = str(eval(instance))
            self.result.text = str(eval(instance))
            display = self.result.text
            total = [0, 0, 0]
            total.append(int(display))

            print(total)

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
        pass

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
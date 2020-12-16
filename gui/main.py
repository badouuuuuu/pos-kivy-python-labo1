#! /usr/bin/python3
# coding: utf-8
 
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
from app.meals_management_v1 import get_employee_id, get_id_list, get_menu_description, get_employee_name, get_purchase_id, get_menu_price, purchase
from kivy.uix.recycleview import RecycleView 
from app.menuPopup import PopUpShow,PopUpShow2
from kivy.config import Config
import datetime
from kivy.uix.vkeyboard import VKeyboard 
Config.set('kivy','window_icon','meals.ico')

class Test(VKeyboard): 
    player = VKeyboard() 
  
class AskId(Widget):

    def CheckId(self):
        displayPOSid  = ''
        employee_id_db = get_id_list('employee')
        displayPOSid = self.ids.askid_label.text 

        intdisplayPOSid = int(displayPOSid)

        if intdisplayPOSid in employee_id_db:
                employeeName = get_employee_name(displayPOSid)
                print('Employee Name:' + employeeName)
                pos_app.screen_manager.current = "POS"

        else:
            self.ids.askid_label.text   = ''
            PopUpShow.show_popup_askid()

class MyGridLayout(ScrollView):
    menu_id_db = get_id_list('menu')
    getpurchase_id = get_purchase_id()
    order = []
    order_price = []
    total = 0
    purchase_menu = {
        "id employee" : { # to change with id add by user in Connect Page
        getpurchase_id: order, 
        "prix" : order_price
                        }
                    }       
    confirm = 'n'
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        label_backup = StringProperty('')
        current_date = datetime.datetime.now()
        formated_date = current_date.strftime("%b %d %Y")
        formated_seconde = current_date.strftime("%H:%M:%S")
        self.ids.label_backup.text += f'{formated_date} - {formated_seconde}\n\nMenu:\n\n'
        for id_menu in self.menu_id_db:
                self.descr = get_menu_description(id_menu)
                self.price = str(get_menu_price(id_menu))
                self.ids.label_backup.text += f'{str(id_menu)} - {self.price}€ - ' + self.descr  + '\n' 


    def list_menu(self):          
        menuList = ListProperty([]) 
        menu_id_db = get_id_list('menu')
        menuList = []
        displayLeft = self.ids.label.text 
        
        if displayLeft == ' ' or displayLeft == '':
            print('ErrorMessage')
            PopUpShow.ErrorMessage()
            self.ids.label.text = ''
        else:
            if self.ids.label.text == '0000':
                self.confirm = 'y'
            if int(displayLeft) in menu_id_db or int(displayLeft) == 0000:
                
                for id in menu_id_db:
                    menu = get_menu_description(id)
                    self.ids.label_backup_addition.text = self.ids.label_backup.text + self.descr + '\n'
                    menuList.append(menu)
                if displayLeft == '0000':
                    pos_app.screen_manager.current = "Ticket"
                else:
                    MenuDescription = get_menu_description(displayLeft) 
                    MenuPrice = get_menu_price(displayLeft)
                    label_backup_addition = StringProperty('')
                    
                    self.order.append(MenuDescription)
                    self.order_price.append(MenuPrice)
                    self.ids.label.text = ''
                    order_of_employee = self.purchase_menu["id employee"][self.getpurchase_id]
                    order_of_employee_price = self.purchase_menu["id employee"]['prix']

                    self.ids.label_backup_addition.text = 'Votre menu: \n\n'
                    
                    order_price = []
                
                    for price in order_of_employee_price:
                
                        order_price.append(price)
                        print(order_price)
                    idmenulist = self.purchase_menu["id employee"][self.getpurchase_id]
                    compteur = 0
                    for nameMenuOrdered in order_of_employee:
                        print(nameMenuOrdered)
                        self.ids.label_backup_addition.text +=  nameMenuOrdered + '  ' + str(order_price[compteur]) + ' €\n'
                        self.ids.label.text = ''
                        index = idmenulist.index(idmenulist[compteur])
                        purchase(index, 3, self.confirm)  # A CORRIGER
                
                        compteur = compteur + 1
                        if self.ids.label.text == '.':
                            purchase(index, 3, self.confirm)

                        #purchase(self.purchase_menu["id employee"][self.getpurchase_id][2], 3, 'y')

                    total = sum(order_price)
                    addtexttotal = '\n\n-------------\n\nTotal: ' + str(total)  + ' €'
                    self.ids.label_backup_addition.text += addtexttotal

            else: 
                PopUpShow.show_popup_nomenu()
                self.ids.label.text = ''

    def back(self):
        pos_app.screen_manager.current = "Connect"
    def add_user(self):
        print('Add User')
        show = PopUpShow() 
        popupWindow = Popup(
            title="Ajouter un employée", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        # Create the popup window

        popupWindow.open() # show the popup
        
    def modify_user(self):
        print('Modify User')   
        show = PopUpShow2() 
        popupWindow = Popup(
            title="Modify Employee", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 

        popupWindow.open() # show the popup
        
    def add_menu(self):
        print('Add menu')
        show = PopUpShow() 
    
        popupWindow = Popup(
            title="Add Menu", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        popupWindow.open()

    def modify_menu(self):
        print('Modify menu')
        
        show = PopUpShow2() 
    
        popupWindow = Popup(
            title="Modify Menu", 
            content=show, 
            size_hint=(None,None),
            size=(600,400),
            background = 'atlas://data/images/defaulttheme/button_pressed',
            background_color = (0,0,0.1,0.75),
            opacity = 1
                            ) 
        popupWindow.open()

    def del1(self):
        self.purchase_menu["id employee"][self.getpurchase_id] = self.purchase_menu["id employee"][self.getpurchase_id][:-1]
        self.purchase_menu["id employee"]["prix"] = self.purchase_menu["id employee"]["prix"][:-1]
        self.total = sum(self.purchase_menu["id employee"]["prix"])
        print(self.purchase_menu["id employee"])
        
class DisplayTicket(Widget):
    print('OK')
    
class Meals(App):
    trigger = False
    triggerC = False
    triggerD = False
    Window.size = (1024, 768)
    Window.minimum_width, Window.minimum_height = Window.size
    #Window.borderless = True

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
        
        self.ticket_page = DisplayTicket()
        screen = Screen(name="Ticket")
        screen.add_widget(self.ticket_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager
        
if __name__ == "__main__":
    pos_app  = Meals()
    pos_app.run()
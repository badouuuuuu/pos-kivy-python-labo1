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
from app.menuPopup import PopUpShow,PopUpShow2, PopUpShowAddMenu, PopShowModifyMenu
from kivy.config import Config
import datetime
from kivy.uix.vkeyboard import VKeyboard 
from fpdf import FPDF

Config.set('kivy','window_icon','meals.ico')

class Test(VKeyboard): 
    player = VKeyboard() 
  
class AskId(Widget):

    pass

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

        self.ids.label_backup.text = 'Entrez votre id'
    dada = True
    def CheckId(self):
        displayPOSid  = 0
        employee_id_db = get_id_list('employee')
        displayPOSid = self.ids.label.text 
        if displayPOSid == '':
            self.ids.label.text   = ''
            PopUpShow.show_popup_askid()
        else:
            intdisplayPOSid = int(displayPOSid)
            
            if intdisplayPOSid in employee_id_db:
                    employeeName = get_employee_name(displayPOSid)
                    self.ids.label_backup.text = employeeName
                    self.ids.label.text   = ''

                    Meals.AskId_nOk = True
                    self.dada = False
                    
            else: 
                self.ids.label.text   = ''
                PopUpShow.show_popup_askid()

            
    def list_menu(self):          
        menuList = ListProperty([]) 
        menu_id_db = get_id_list('menu')
        menuList = []
        tata = self.ids.label.text 
        displayLeft = int(tata)

        if displayLeft in menu_id_db:
            
            self.ids.label_backup_addition.text = displayLeft+ '\n'
            menuList.append(displayLeft)
            
        if displayLeft == '0000':
            displayLeft = ''
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
               # purchase(index, 3, self.confirm)  # A CORRIGER
        
                compteur = compteur + 1
                if self.ids.label.text == '.':
                    pass

                #purchase(self.purchase_menu["id employee"][self.getpurchase_id][2], 3, 'y')

            total = sum(order_price)
            addtexttotal = '\n\n-------------\n\nTotal: ' + str(total)  + ' €'
            self.ids.label_backup_addition.text += addtexttotal

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
        show = PopUpShowAddMenu() 
    
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

        show = PopShowModifyMenu() 
    
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
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Purchase')
    pdf.output('bill.pdf', 'F')
    
class Meals(App):
    AskId_nOk = False
    trigger = False
    triggerC = False
    triggerD = False
    Window.size = (1024, 768)
    Window.minimum_width, Window.minimum_height = Window.size
    #Window.borderless = True

    def build(self):
        self.screen_manager = ScreenManager()
        
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
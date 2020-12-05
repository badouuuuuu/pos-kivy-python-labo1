from app.meals_management_v1 import get_id_list, get_employee_name, get_employee_id, get_id_list, get_menu_price, get_menu_description

def getEmployee():
    # Get Employee List on startup
    employee_list = get_id_list('employee')

    for list in employee_list:
        employee = get_employee_name(list)

        return employee_list
        
def getMenuList():
    menu_id_list = get_id_list('menu')
    mylist = []
    menudescription = []
    
    for i in menu_id_list:
        list = get_menu_price(i)
        menudescription = get_menu_description(i)
        mylist.append({i, list, menudescription})
        print(list)

    return mylist


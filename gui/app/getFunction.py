from app.meals_management_v1 import get_id_list, get_employee_name, get_employee_id, get_id_list, get_menu_price, get_menu_description, get_employee_name

def getEmployee():
    # Get Employee List on startup
    employee_id_list = get_id_list('employee')
    employee_list = []
    employee_name = []

    for i in employee_id_list:
        employee_name = get_employee_name(i)
        employee_list.append({i, employee_name})

    return employee_list
        
def getMenuList():
    menu_id_list = get_id_list('menu')
    menu_list = []
    menu_description = []
    
    for i in menu_id_list:
        list = get_menu_price(i)
        menu_description = get_menu_description(i)
        menu_list.append({i, list, menu_description})

    return menu_list


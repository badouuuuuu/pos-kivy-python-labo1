from app.meals_management_v1 import get_id_list, get_employee_name, get_employee_id


def getEmployee():
    # Get Employee List on startup
    employee_list = get_id_list('employee')

    for list in employee_list:
        employee = get_employee_name(list)
        print('------------')
        print('Name : ' + employee + '\nid : ' + str(list))
        

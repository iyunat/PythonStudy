from Employee_basa import empl_company
from Employee_salary import empl_sal


def output (data):
    for key, value in data.items():
        print (key, value)

def record_info_sal(name_file):
    with open(name_file, "w") as file:
        for key,value in empl_sal.items():
            file.write("{}:{}\n".format(key,value))

def record_info_com(name_file):
    with open(name_file, "w") as file:
        for key,value in empl_company.items():
            file.write("{}:{}\n".format(key,value))
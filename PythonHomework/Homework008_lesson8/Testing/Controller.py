
import U_i
from Employee_basa import empl_company
from Employee_salary import empl_sal


print("Сотрудники ООО 'Счастливый день':")
print()
U_i.output(empl_company)

print("*" *80)

print("Заработная плата сотрудников")
print()
U_i.output (empl_sal)

U_i.record_info_sal("salary_info.txt")
U_i.record_info_com("employee_basa_info.txt")

def my_key(empl_company, value):
    for k, v in empl_company.items():
        if v == value:
            return k

print(my_key(empl_company, "Яна"))
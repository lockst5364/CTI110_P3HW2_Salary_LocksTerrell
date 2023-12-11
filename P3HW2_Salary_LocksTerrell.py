#CTI-110
#P3HW2 - Salary
#Terrell Locks
#November 6, 2023
#

#user inputs employee information

name = (input("Enter Employee's name: "))
hours = float(input('Enter number of hours worked: '))
pay = float(input("Enter employee's pay rate: "))

#displays whether or not the employee gets overtime, based on the input

if hours > 40:
    overtime = hours - 40
    overtime_pay = overtime * pay * 1.5
    reghour_pay = pay * 40
    gross_pay = overtime_pay + reghour_pay
else:
    overtime = 0
    overtime_pay = 0
    reghour_pay = pay * hours
    gross_pay = reghour_pay
     
#the program displays the results    

print('------------------------------------------------')
print('Employee name:   ',   name)
print('')
print('Hours worked   Pay Rate  Overtime   Overtime Pay    RegHour Pay   Gross Pay')
print('-------------------------------------------------------------------------------')
print(f'{hours}           {pay}      {overtime}        {overtime_pay}          ${reghour_pay}        ${gross_pay}')

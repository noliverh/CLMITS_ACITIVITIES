"""
Making a simple payroll using the csv and prettytable.
"""
from prettytable import PrettyTable
import csv

compute = False
while not compute:

    empPtt = PrettyTable()

    empPtt.field_names = ["ID", "NAME", "DESIGNATION", "MONTHLY SALARY"]

    with open("employees.csv") as empFile:
        readCSV = csv.reader(empFile, delimiter=",")

        empID = []
        empName = []
        empDesig = []
        empSalary = []

        for emp in readCSV:
            empPtt.add_row(emp)
            empID.append(emp[0])
            empName.append(emp[1])
            empDesig.append(emp[2])
            empSalary.append(emp[3])

        print(empPtt)

        empIDS = input("Enter Employess ID: ")
        empIndex = empID.index(empIDS)
        theirName = empName[empIndex]
        theirDesig = empDesig[empIndex]
        theirSalary = int(empSalary[empIndex])


    perDay = int(theirSalary / 20)

    print(f"{theirName} with a designation: {theirDesig}")

    daysRendered = int(input("Days Rendered: "))

    netIncome = daysRendered * perDay

    print(f"Net Income: {netIncome}")

    compute_again = input("Compute Again? [yes/no]: ")

    if compute_again == "yes":
        compute = False
    else:
        print("Thank you!")
        break


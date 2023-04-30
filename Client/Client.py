import requests

isOpen = True

funcs = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeById,
    3: getEmployeeByName,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee
    7: importEmployeesFromCsv,
    8: exportEmployeesToCsv
    9: exit
}

def testServer():
    pass


def main():
    # print(requests.get("http://127.0.0.1:5000/test").text)
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())


if __name__ == "__main__":
    main()

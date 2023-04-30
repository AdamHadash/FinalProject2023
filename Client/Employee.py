class Employee:
    def __init__(self, id, first_name, last_name, email, salary):
        self.__id = id
        self.__first_name = first_name
        self.last_name = last_name
        self.__email = email
        self.__salary = salary

    def __setId__(self, id):
        self.__Id = id

    def __getId__(self):
        return self.__id

    def __setFirst_name__(self, first_name):
        self.__first_name = first_name

    def __getFirst_name__(self):
        return self.__first_name

    def __setLast_name__(self, last_name):
        self.__last_name = last_name

    def __getLast_name__(self):
        return self.__last_name


    def __setEmail__(self, email):
        self.__email = email

    def __getEmail__(self):
        return self.__email

    def __setSalary__(self, salary):
        self.__salary = salary

    def __getSalary__(self):
        return self.__salary

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.__name,self.__id,self.__position,self.__salary,self.__gender)

first = Employee("Adam", "5", "noob", "40k", "bro")
print(first)